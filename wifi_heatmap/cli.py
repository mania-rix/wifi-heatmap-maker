"""Command‑line interface for Wi‑Fi heat‑map creation."""
from __future__ import annotations
import argparse, csv, re, subprocess, sys, textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RSSI_RE = re.compile(r"signal: ([-\d.]+) dBm")

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _scan(interface: str = "wlan0") -> list[float]:
    """Return list of RSSI readings from `iw dev <iface> scan`. Linux‑only."""
    try:
        proc = subprocess.run(
            ["iw", "dev", interface, "scan"],
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError:
        sys.exit("[✗] `iw` not found – this tool supports Linux only.")

    return [float(m.group(1)) for m in RSSI_RE.finditer(proc.stdout)]


def _append_csv(csv_path: Path, x: float, y: float, rssi: float) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("a", newline="") as f:
        csv.writer(f).writerow([x, y, rssi])


def _render(csv_path: Path, svg_out: Path) -> None:
    """Generate a simple scatter‑plot heat‑map as SVG."""
    df = pd.read_csv(csv_path, names=["x", "y", "rssi"])
    fig, ax = plt.subplots()
    sc = ax.scatter(df.x, df.y, c=df.rssi, cmap="viridis", s=80)
    fig.colorbar(sc, label="RSSI (dBm)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Wi‑Fi signal strength heat‑map")
    fig.tight_layout()
    fig.savefig(svg_out)
    print(f"[✓] Heat‑map saved to {svg_out.relative_to(Path.cwd())}")

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

# wifi_heatmap/cli.py  – only the section below has changed
# ...
def main() -> None:
    ap = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """
            Wi‑Fi heat‑map CLI — turn RSSI samples into a coloured SVG.

            Workflow
            ```
            # 1 Walk the floor‑plan, press ENTER to log points
            python -m wifi_heatmap.cli parse --csv survey.csv

            # 2 Render SVG heat‑map
            python -m wifi_heatmap.cli render survey.csv heatmap.svg
            ```
            """
        ),
    )

    sub = ap.add_subparsers(dest="cmd", required=True)

    p_parse = sub.add_parser("parse", help="interactive point logger")
    p_parse.add_argument("--csv", required=True, type=Path)
    p_parse.add_argument("--iface", default="wlan0", help="Wi‑Fi interface name")

    p_render = sub.add_parser("render", help="render CSV → SVG heat‑map")
    p_render.add_argument("csv", type=Path)
    p_render.add_argument("svg_out", type=Path)

    args = ap.parse_args()

    if args.cmd == "parse":
        print("Move to a point on the floor‑plan, then press ENTER (CTRL+C to quit)")
        try:
            while True:
                input()
                rssi_list = _scan(args.iface)
                if not rssi_list:
                    print("[!] No RSSI found — try moving or check interface")
                    continue
                rssi = sum(rssi_list) / len(rssi_list)
                x = float(input("x coordinate: "))
                y = float(input("y coordinate: "))
                _append_csv(Path(args.csv), x, y, rssi)
                print(f"Logged ({x}, {y}) → {rssi:.1f} dBm")
        except KeyboardInterrupt:
            print("\n[✓] Survey saved →", args.csv)

    elif args.cmd == "render":
        _render(args.csv, args.svg_out)


if __name__ == "__main__":
    main()

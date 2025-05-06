"""Smoke test – ensures CLI imports & help flag work."""
import subprocess, sys
from importlib import import_module

def test_import():
    assert import_module("wifi_heatmap.cli")

def test_help():
    result = subprocess.run(
        [sys.executable, "-m", "wifi_heatmap.cli", "-h"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "Wi‑Fi heat‑map" in result.stdout

"""Placeholder for future advanced SVG interpolation utils."""
from pathlib import Path

__all__ = ["ensure_svg"]

def ensure_svg(path: Path) -> Path:
    if path.suffix.lower() != ".svg":
        raise ValueError("Only SVG floor-plans are supported right now.")
    return path

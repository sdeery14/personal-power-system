"""Show the PRELIMINARY Diesel Heater Module (002) model in the VS Code OCP CAD Viewer.

    uv run python preview.py                      # B1 Adjusted (default)
    uv run python preview.py --variant original   # A Original
    uv run python preview.py --variant compact    # B1 Compact

Open the viewer panel first (Command Palette: "OCP CAD Viewer: Open Viewer").
The script builds the same assembly as build.py and pushes it to the viewer
with every component under its identifier and colour, so the tree on the left
of the viewer lists U1, L2-W1, HX2, TR-lower, fuel_tank, and so on.

This script only displays. STEP, SVG, PNG, and the schedules come from build.py
and do not depend on the viewer. PRELIMINARY: NOT FOR FABRICATION.
"""

from __future__ import annotations

import argparse
import socket
import sys

import params as P
from model import BANNER, build_assembly


def viewer_reachable(port: int, host: str = "127.0.0.1") -> bool:
    try:
        with socket.create_connection((host, port), timeout=1.0):
            return True
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--variant", choices=list(P.VARIANTS), default=P.DEFAULT_VARIANT.key)
    args = ap.parse_args(argv)
    variant = P.VARIANTS[args.variant]

    try:
        from ocp_vscode import Camera, get_port, show
    except ImportError:
        print("ocp_vscode is not installed. Run `uv sync` in this directory.", file=sys.stderr)
        return 1

    port = get_port()
    if not viewer_reachable(port):
        print(
            f"No OCP CAD Viewer is listening on port {port}.\n"
            "In VS Code: Command Palette > \"OCP CAD Viewer: Open Viewer\", then rerun this script.",
            file=sys.stderr,
        )
        return 1

    assy = build_assembly(variant=variant)
    print(f"{BANNER} — {variant.title}")
    print(f"{P.LAYOUT_NOTE[variant.layout]}")
    print("Bounding-box placeholders; illustrative placement; gates G1-G5 closed.")
    # Reset the camera so every run frames the whole model. Z is up, as in the model.
    show(assy, axes=True, axes0=True, up="Z", reset_camera=Camera.RESET, progress="")
    print(f"Sent {len(assy.children)} named components ({variant.title}) to OCP CAD Viewer on port {port}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

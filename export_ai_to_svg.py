"""Export every .ai file under src to svg and png, preserving the folder structure."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recursively export Illustrator files from src to svg and png with VectorCraft."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT / "src",
        help="source directory (default: src beside this script)",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=ROOT / "svg",
        help="SVG destination directory (default: svg beside this script)",
    )
    parser.add_argument(
        "--png-destination",
        type=Path,
        default=ROOT / "png",
        help="PNG destination directory (default: png beside this script)",
    )
    parser.add_argument(
        "--vectorcraft-cli",
        default=os.environ.get("VECTORCRAFT_CLI"),
        help="VectorCraft CLI executable (default: VECTORCRAFT_CLI, PATH, or standard install location)",
    )
    return parser.parse_args()


def find_vectorcraft_cli(configured_path: str | None) -> str | None:
    if configured_path:
        executable = shutil.which(configured_path)
        if executable:
            return executable
        path = Path(configured_path).expanduser()
        return str(path.resolve()) if path.is_file() else None

    executable = shutil.which("vectorcraft-cli")
    if executable:
        return executable

    install_locations = [
        Path(os.environ[variable]) / "Documents" / "ArtCraft" / "vectorcraft" / "vectorcraft-cli.exe"
        for variable in ("OneDrive", "OneDriveCommercial")
        if os.environ.get(variable)
    ]
    install_locations.extend(
        (
            Path.home() / "OneDrive" / "Documents" / "ArtCraft" / "vectorcraft" / "vectorcraft-cli.exe",
            Path.home() / "Documents" / "ArtCraft" / "vectorcraft" / "vectorcraft-cli.exe",
        )
    )
    return next((str(path) for path in install_locations if path.is_file()), None)


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    destinations = {
        ".svg": args.destination.resolve(),
        ".png": args.png_destination.resolve(),
    }

    vectorcraft_cli = find_vectorcraft_cli(args.vectorcraft_cli)
    if vectorcraft_cli is None:
        print(
            "Could not find vectorcraft-cli. Add it to PATH, set VECTORCRAFT_CLI, "
            "or pass --vectorcraft-cli with the executable path.",
            file=sys.stderr,
        )
        return 1

    if not source.is_dir():
        print(f"Source directory does not exist: {source}", file=sys.stderr)
        return 1

    files = sorted(
        (path for path in source.rglob("*") if path.is_file() and path.suffix.lower() == ".ai"),
        key=lambda path: path.relative_to(source).as_posix().casefold(),
    )
    if not files:
        print(f"No .ai files found in {source}", file=sys.stderr)
        return 1

    failures = 0
    exports = len(files) * len(destinations)
    for input_path in files:
        for suffix, destination in destinations.items():
            output_path = destination / input_path.relative_to(source).with_suffix(suffix)
            try:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                result = subprocess.run(
                    [vectorcraft_cli, "convert", str(input_path), str(output_path)],
                    check=False,
                    capture_output=True,
                    text=True,
                )
            except OSError as error:
                print(f"Failed to run VectorCraft for {input_path}: {error}", file=sys.stderr)
                failures += 1
                continue

            if result.returncode:
                details = result.stderr.strip() or result.stdout.strip()
                print(f"Export failed: {input_path} -> {output_path}", file=sys.stderr)
                if details:
                    print(details, file=sys.stderr)
                failures += 1
            else:
                print(
                    f"Exported {input_path.relative_to(source)} -> "
                    f"{output_path.relative_to(destination)} ({suffix[1:]})"
                )

    succeeded = exports - failures
    print(f"Export complete: {succeeded}/{exports} exports succeeded.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

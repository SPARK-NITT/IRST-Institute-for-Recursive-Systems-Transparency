#!/usr/bin/env python3
"""
hash_utils.py

Simple SHA-256 helper for IRST-style repos.

Usage examples (from repo root):

  # Print hashes for key docs to the terminal
  python scripts/hash_utils.py docs/IRST_Governance_Charter_v1.1.md docs/IRST_Operational_Enforcement_v2.0.md

  # Hash a whole folder and append results to meta/HASHES.md
  python scripts/hash_utils.py docs meta/HASHES.md

The script is intentionally minimal: no external dependencies, plain Python 3.
"""

import hashlib
import sys
from pathlib import Path
from datetime import datetime

def sha256_file(path: Path) -> str:
    """Return the SHA-256 hex digest for a file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def iter_files(target: Path):
    """Yield files under target. If target is a file, yield it; if directory, walk it."""
    if target.is_file():
        yield target
    elif target.is_dir():
        for p in sorted(target.rglob("*")):
            if p.is_file():
                yield p

def main(argv):
    if len(argv) < 2:
        print("Usage:")
        print("  python scripts/hash_utils.py <file-or-dir> [<file-or-dir> ...]")
        print("  python scripts/hash_utils.py <file-or-dir> meta/HASHES.md")
        sys.exit(1)

    *targets, last = [Path(a) for a in argv[1:]]

    # If the last argument looks like a HASHES file (under meta/), treat it as output.
    output_path = None
    if last.name.upper().startswith("HASHES") or last.parent.name == "meta":
        output_path = last
        targets = targets or []
    else:
        targets.append(last)

    entries = []

    for t in targets:
        if not t.exists():
            print(f"[WARN] Does not exist, skipping: {t}")
            continue

        for f in iter_files(t):
            digest = sha256_file(f)
            rel = f.as_posix()
            line = f"SHA-256  {digest}  {rel}"
            print(line)
            entries.append(line)

    # If an output file was provided, append in a simple, human-readable format.
    if output_path and entries:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with output_path.open("a", encoding="utf-8") as out:
            out.write(f"\n# Hash batch {timestamp}\n")
            for line in entries:
                out.write(line + "\n")
        print(f"\n[INFO] Appended {len(entries)} hash entries to {output_path.as_posix()}")

if __name__ == "__main__":
    main(sys.argv)

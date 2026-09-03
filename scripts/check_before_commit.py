#!/usr/bin/env python3
"""Small pre-commit privacy and GitHub-size check for the result archive."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {
    ".csv", ".env", ".json", ".log", ".md", ".py", ".sh", ".tsv",
    ".txt", ".yaml", ".yml",
}

FATAL_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
}

REVIEW_PATTERNS = {
    "private IPv4 address": re.compile(
        r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
        r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
    ),
    "absolute home path": re.compile(r"/(?:home|homes)/[A-Za-z0-9._-]+/"),
    "password-like assignment": re.compile(
        r"(?i)\b(?:password|passwd|token|secret)\s*[:=]\s*['\"]?[^\s'\"]{6,}"
    ),
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    fatals: list[str] = []
    reviews: list[str] = []

    for path in iter_files(root):
        rel = path.relative_to(root)
        size = path.stat().st_size
        if size >= 95 * 1024 * 1024:
            fatals.append(f"GitHub-sized file ({size} bytes): {rel}")
        elif size >= 25 * 1024 * 1024:
            reviews.append(f"large file ({size} bytes): {rel}")

        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            reviews.append(f"could not read {rel}: {exc}")
            continue
        for label, pattern in FATAL_PATTERNS.items():
            if pattern.search(text):
                fatals.append(f"{label}: {rel}")
        for label, pattern in REVIEW_PATTERNS.items():
            if pattern.search(text):
                reviews.append(f"{label}: {rel}")

    print("PRE_COMMIT_ARCHIVE_CHECK")
    print(f"root={root}")
    print(f"fatal={len(fatals)} review={len(reviews)}")
    for item in sorted(set(fatals)):
        print(f"ERROR  {item}")
    for item in sorted(set(reviews)):
        print(f"REVIEW {item}")

    if fatals:
        print("RESULT=BLOCKED")
        return 1
    print("RESULT=PASS_WITH_REVIEW" if reviews else "RESULT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())


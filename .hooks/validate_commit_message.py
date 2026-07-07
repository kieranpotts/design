#!/usr/bin/env python3
"""
Validate commit message format.

Enforces commit messages follow the format:
  <type>: <description>

Where <type> is one of the allowed revision types: a subset of the standard
TS-9 revision types, plus prefixes specific to this repository.

Keep VALID_TYPES in sync with the CI workflow at
.github/workflows/validate-commit-messages.yaml.
"""

import re
import sys

VALID_TYPES = [
    # Subset of standard commit types:
    "chore",
    "fix",
    "maintenance",
    "refactor",
    "revert",
    "style",

    # Repository-specific commit types:
    "audit",
    "design",
]

PATTERN = rf"^({'|'.join(VALID_TYPES)}): [a-z0-9].*"


def validate_commit_message(message: str) -> bool:
    """Check if commit message matches the required format."""
    return bool(re.match(PATTERN, message))


def main() -> int:
    """Validate commit message from file."""
    if not sys.argv[1:]:
        print("Error: no commit message file provided")
        return 1

    commit_msg_file = sys.argv[1]

    try:
        with open(commit_msg_file) as f:
            commit_msg = ""
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    commit_msg = line
                    break
    except OSError as e:
        print(f"Error reading commit message file: {e}")
        return 1

    if not commit_msg:
        print("Error: commit message is empty")
        return 1

    if not validate_commit_message(commit_msg):
        print(f'Invalid commit message format: "{commit_msg}"')
        print("Expected format: <type>: <description>")
        print(f"Valid types: {', '.join(VALID_TYPES)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

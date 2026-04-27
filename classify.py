#!/usr/bin/env python3
"""
classify.py — Dewey classification for a single file using Claude Haiku.

Usage:
    python classify.py <file_path>
    python classify.py <file_path> --raw          # JSON output

The script reads the file, sends its content and a description of the
Dewey classification rules to Claude Haiku, and prints the result.

Requirements:
    pip install anthropic

Environment:
    ANTHROPIC_API_KEY — your Anthropic API key
"""

import argparse
import json
import os
import sys

import anthropic

SKILL_PATH = os.path.join(os.path.dirname(__file__), "skill", "deweygraph-file-organizer.skill.v3.md")
CLASSIFICATION_MANUAL_PATH = os.path.join(os.path.dirname(__file__), "docs", "classification-manual.md")

DEWEY_CLASSES = """\
000 Systems, information, archives, computing
100 Philosophy, mind, perception, ethics
200 Belief, ritual, mythology, spirituality
300 Society, politics, institutions, culture
400 Language, communication, symbols
500 Natural science, maths, formal systems
600 Applied science, engineering, medicine, making
700 Art, design, image, object, performance
800 Literature, rhetoric, writing, narrative
900 History, geography, biography, memory

Common subclasses:
  001.CYB  Cybernetics
  006.3.AI Artificial Intelligence
  170.ETH  Ethics
  260.RIT  Ritual
  621.3.CIRC Circuit/Electronics
  700.STUDIO Studio Practice
  740.1.TYPO Typography
  808.02.ESS Essays
  821.POET Poetry
  920.MEM  Memory/Biography

Material roles: source | process | reference | output | residue | duplicate-candidate
Format markers (NOT subject): BK | ESS | ART | PDF | NOTE | NB | IMG | AUD | VID | PROJ
"""

SYSTEM_PROMPT = """\
You are a Dewey Decimal Classification assistant for the DeweyGraph archive system.
Your job is to read a file's content and classify it with a single anchor code.

Rules (from the DeweyGraph skill):
- One item, one anchor. Never assign two primary codes.
- Subject is not lens. Format is not subject.
- Classify by dominant function, not incidental themes.
- Archival worthiness first: not everything deserves a note.
- Notebooks: classify by role in the archive, not internal content mix.
- Clarity over completeness.

Respond ONLY with valid JSON — no explanation outside the JSON block:
{
  "anchor_code": "<Dewey class code, e.g. 006.3.AI>",
  "material_role": "<one of: source | process | reference | output | residue | duplicate-candidate>",
  "archival_worthy": true | false,
  "decision_note": "<one or two sentences explaining the classification>"
}
"""


def load_text(path: str) -> str:
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError as e:
        return f"[could not read: {e}]"


def classify_file(file_path: str) -> dict:
    file_content = load_text(file_path)
    filename = os.path.basename(file_path)

    # Truncate very large files — Haiku has a 200K context window,
    # but we keep the payload small for speed and cost.
    max_chars = 12_000
    if len(file_content) > max_chars:
        file_content = file_content[:max_chars] + f"\n\n[...truncated at {max_chars} chars]"

    user_message = (
        f"File name: {filename}\n\n"
        f"Dewey classes and material roles available:\n{DEWEY_CLASSES}\n\n"
        f"File content:\n```\n{file_content}\n```\n\n"
        "Classify this file."
    )

    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    raw = response.content[0].text.strip()

    # Strip markdown code fences if present
    if raw.startswith("```"):
        lines = raw.splitlines()
        raw = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

    return json.loads(raw)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classify a file using the DeweyGraph Dewey Decimal system."
    )
    parser.add_argument("file", help="Path to the file to classify")
    parser.add_argument("--raw", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: '{args.file}' is not a file.", file=sys.stderr)
        sys.exit(1)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    try:
        result = classify_file(args.file)
    except json.JSONDecodeError as e:
        print(f"Error: Claude returned non-JSON output: {e}", file=sys.stderr)
        sys.exit(1)
    except anthropic.APIError as e:
        print(f"API error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.raw:
        print(json.dumps(result, indent=2))
        return

    # Human-readable output
    worthy = "yes" if result.get("archival_worthy") else "no"
    print(f"\nFile:          {os.path.basename(args.file)}")
    print(f"Anchor code:   {result.get('anchor_code', '?')}")
    print(f"Material role: {result.get('material_role', '?')}")
    print(f"Archival:      {worthy}")
    print(f"Note:          {result.get('decision_note', '')}\n")


if __name__ == "__main__":
    main()

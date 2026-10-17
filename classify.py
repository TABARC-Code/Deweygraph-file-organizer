#!/usr/bin/env python3
"""
classify.py — DeweyGraph modular classifier with heat-weighted bilateral links.

Skills a–f are a toolkit, not a pipeline. Any subset, any order, any revisit.
  a,d          — simple reference doc
  a,c,d,e      — source material worth linking
  a,c,d,e,b,a  — revisit typology after seeing content

Heat tracks pheromone accumulation on two levels:
  class_heat   — how often a Dewey class appears across the archive
  path_heat    — how often each skill→skill transition is taken

Every class link is bilateral: A→B also writes B→A with the reverse relation.

Skills:
  a  typology   — filing context (intake|project|archive|reference|export|dump|mixed)
  b  filter     — archival worthiness gate
  c  role       — material role (source|process|reference|output|residue|duplicate-candidate)
  d  classify   — Dewey anchor + secondary domains + lens tags
  e  link       — typed bilateral relations, heat values 1–10
  f  note       — Obsidian-ready YAML frontmatter + body

Usage:
    python classify.py <file>           classify one file, update graph
    python classify.py --scan <dir>     scan a folder + synthesise cross-links
    python classify.py --graph          show the link graph
    python classify.py --heat           show class + skill-path heat maps
    python classify.py <file> --raw     raw JSON output

State: dewey_graph.json in this directory.
Requires: pip install anthropic  |  ANTHROPIC_API_KEY env var
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic

ROOT = Path(__file__).parent
GRAPH_PATH = ROOT / "dewey_graph.json"

# ─── Skill registry ──────────────────────────────────────────────────────────
# Each skill has a letter ID, a name, a description, and discrete functions.
# The queen (Haiku) picks which skills and which functions to invoke per file.
# Not all functions are needed every time — partial invocation is the norm.

SKILLS: dict[str, dict] = {
    "a": {
        "name": "typology",
        "desc": "Determine filing context: intake|project|archive|reference|export|dump|mixed",
        "functions": ["folder_type", "context_assess"],
    },
    "b": {
        "name": "filter",
        "desc": "Archival worthiness gate — does this item deserve a structured note?",
        "functions": ["worthy", "residue", "duplicate_flag"],
    },
    "c": {
        "name": "role",
        "desc": "Material role: source|process|reference|output|residue|duplicate-candidate",
        "functions": ["assign"],
    },
    "d": {
        "name": "classify",
        "desc": "Dewey anchor code + secondary domains + lens tags",
        "functions": ["anchor", "secondary", "lens"],
    },
    "e": {
        "name": "link",
        "desc": "Typed bilateral relations. Every link needs a heat (1–10). Every link gets a reverse.",
        "functions": ["class_link", "file_link", "heat_score", "bilateral"],
    },
    "f": {
        "name": "note",
        "desc": "Obsidian-ready YAML frontmatter + note body",
        "functions": ["frontmatter", "body", "index_entry"],
    },
}

# ─── Bilateral relation map ───────────────────────────────────────────────────
# Symmetric relations reverse to themselves.
# Every forward link written by Haiku generates a reverse link automatically.

REVERSE: dict[str, str] = {
    "influenced-by":          "influences",
    "influences":             "influenced-by",
    "critique-of":            "critiqued-by",
    "critiqued-by":           "critique-of",
    "subset-of":              "has-subset",
    "has-subset":             "subset-of",
    "part-of":                "has-part",
    "has-part":               "part-of",
    "applies-to":             "has-application-in",
    "has-application-in":     "applies-to",
    "uses-methods-from":      "methods-used-in",
    "methods-used-in":        "uses-methods-from",
    "documents":              "documented-by",
    "documented-by":          "documents",
    "derived-from":           "gives-rise-to",
    "gives-rise-to":          "derived-from",
    "references":             "referenced-by",
    "referenced-by":          "references",
    # symmetric — same in both directions
    "related-to":                  "related-to",
    "contrasts-with":              "contrasts-with",
    "overlaps-with":               "overlaps-with",
    "parallel-to":                 "parallel-to",
    "same-topic-different-lens":   "same-topic-different-lens",
}

DEWEY = """\
000 Systems/computing   001.CYB Cybernetics     006.3.AI Artificial Intelligence
100 Philosophy/mind     170.ETH Ethics          100.MIND Mind/Cognition
200 Belief/ritual       260.RIT Ritual          200.MYTH Mythology
300 Society/culture     350.GOV Governance      305.SOC  Social groups
400 Language/symbols    410.LING Linguistics    400.SEM  Semiotics
500 Science/maths       510.MATH Mathematics    500.FORMAL Formal systems
600 Applied/making      621.3.CIRC Electronics  600.MAKE Making/Craft
700 Art/design          700.STUDIO Studio       740.1.TYPO Typography   720.ARCH Architecture
800 Literature/writing  808.02.ESS Essays       821.POET Poetry         800.NARR Narrative
900 History/memory      920.MEM Memory          900.HIST History
"""

# ─── Graph I/O ────────────────────────────────────────────────────────────────

def load_graph() -> dict:
    if GRAPH_PATH.exists():
        with open(GRAPH_PATH) as f:
            return json.load(f)
    return {
        "version": 2,
        "nodes": {},        # path → classification result
        "class_heat": {},   # Dewey class → accumulated heat (float)
        "path_heat": {},    # "a.fn→b.fn" → count (int) — pheromone on skill transitions
        "file_links": [],   # bilateral file-to-file links
    }


def save_graph(g: dict) -> None:
    with open(GRAPH_PATH, "w") as f:
        json.dump(g, f, indent=2)


def _update_path_heat(g: dict, skill_path: list[str]) -> None:
    """Increment pheromone on every consecutive skill-function transition."""
    for i in range(len(skill_path) - 1):
        key = f"{skill_path[i]}→{skill_path[i + 1]}"
        g["path_heat"][key] = g["path_heat"].get(key, 0) + 1


def add_node(g: dict, rel_path: str, result: dict) -> None:
    """Store a classification result and accumulate class heat."""
    g["nodes"][rel_path] = {
        "anchor":          result.get("anchor_code", ""),
        "secondary":       result.get("secondary_domains", []),
        "role":            result.get("material_role", ""),
        "archival_worthy": result.get("archival_worthy", True),
        "note":            result.get("decision_note", ""),
        "skill_path":      result.get("skill_path", []),
        "class_links":     result.get("class_links", []),
        "classified_at":   datetime.now(timezone.utc).isoformat(),
    }
    anchor = result.get("anchor_code", "")
    if anchor:
        g["class_heat"][anchor] = g["class_heat"].get(anchor, 0.0) + 1.0
    for lk in result.get("class_links", []):
        cls = lk["target_class"]
        g["class_heat"][cls] = g["class_heat"].get(cls, 0.0) + float(lk.get("heat", 1))
    _update_path_heat(g, result.get("skill_path", []))


def add_file_links(g: dict, links: list[dict]) -> None:
    """
    Insert bilateral file-to-file links.
    Each forward link automatically generates its reverse using REVERSE map.
    Duplicate (from, to, relation) triples are silently skipped.
    """
    seen = {(l["from"], l["to"], l["relation"]) for l in g["file_links"]}
    for lk in links:
        fwd = (lk["from"], lk["to"], lk["relation"])
        if fwd not in seen:
            g["file_links"].append(lk)
            seen.add(fwd)
        rev_rel = REVERSE.get(lk["relation"], "related-to")
        rev = (lk["to"], lk["from"], rev_rel)
        if rev not in seen:
            g["file_links"].append({
                "from":     lk["to"],
                "to":       lk["from"],
                "relation": rev_rel,
                "heat":     lk["heat"],
                "reason":   f"[↩ reverse] {lk.get('reason', '')}",
            })
            seen.add(rev)


# ─── Haiku prompts ────────────────────────────────────────────────────────────

def _skill_menu() -> str:
    lines = []
    for k, v in SKILLS.items():
        fns = " | ".join(v["functions"])
        lines.append(f"  {k} ({v['name']}): {v['desc']}\n      functions: {fns}")
    return "\n".join(lines)


# The system prompt is stable — it gets cached after the first call.
CLASSIFY_SYSTEM = f"""\
You are the DeweyGraph queen ant: a modular classifier using skills a–f.

Skills are a toolkit, not a pipeline. Pick any subset, any order, revisit freely.
  A simple note might need only: a.context_assess, d.anchor
  A rich source doc might need: a.context_assess, b.worthy, c.assign, d.anchor, d.secondary, e.class_link, e.bilateral
  A notebook might revisit: a.folder_type, d.anchor, a.context_assess, d.anchor (after seeing content)

SKILLS:
{_skill_menu()}

DEWEY CLASSES:
{DEWEY}

RELATION TYPES (every forward link gets a bilateral reverse automatically):
  influenced-by / influences
  critique-of / critiqued-by
  subset-of / has-subset
  part-of / has-part
  applies-to / has-application-in
  uses-methods-from / methods-used-in
  documents / documented-by
  derived-from / gives-rise-to
  references / referenced-by
  related-to (symmetric)
  contrasts-with (symmetric)
  overlaps-with (symmetric)
  parallel-to (symmetric)
  same-topic-different-lens (symmetric)

HEAT SCALE 1–10 (pheromone strength):
  1–3  cold  — tangential, weak connection
  4–6  warm  — meaningful, worth following
  7–9  hot   — strong, important path
  10   burning — inseparable, core dependency

RULES:
  - One anchor only. Subject ≠ lens. Format ≠ subject.
  - Only classify what is worth remembering (b.filter guards this).
  - Explain difficult choices in decision_note.
  - skill_path must list every skill.function you invoked, in order.

Return ONLY valid JSON — no prose, no markdown fences:
{{
  "skill_path":        ["a.context_assess", "d.anchor"],
  "anchor_code":       "NNN.X",
  "secondary_domains": ["NNN.X"],
  "material_role":     "source|process|reference|output|residue|duplicate-candidate",
  "archival_worthy":   true|false,
  "decision_note":     "one or two sentences",
  "class_links": [
    {{"target_class":"NNN.X","relation":"...","heat":N,"reason":"..."}}
  ]
}}
"""

SYNTHESIS_SYSTEM = """\
You are a DeweyGraph link synthesiser.
Given classified files, identify meaningful file-to-file connections.
Every link you emit is automatically made bilateral — only emit forward links.
Omit links with heat < 4. Prefer fewer hot links over many cold ones.

HEAT: 1–3 cold | 4–6 warm | 7–9 hot | 10 burning

RELATIONS: influenced-by, critique-of, subset-of, part-of, applies-to,
uses-methods-from, documents, derived-from, references, related-to,
contrasts-with, overlaps-with, parallel-to, same-topic-different-lens

Return ONLY valid JSON:
{"file_links":[{"from":"path","to":"path","relation":"...","heat":N,"reason":"..."}]}
"""


# ─── API calls ────────────────────────────────────────────────────────────────

_CLIENT: anthropic.Anthropic | None = None


def _client() -> anthropic.Anthropic:
    global _CLIENT
    if _CLIENT is None:
        _CLIENT = anthropic.Anthropic()
    return _CLIENT


def _call(system: str, user_msg: str, max_tokens: int = 768) -> dict:
    """Call Claude Haiku. System prompt is cache-pinned (stable content)."""
    resp = _client().messages.create(
        model="claude-haiku-4-5",
        max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = resp.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        lines = raw.splitlines()
        raw = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])
    return json.loads(raw)


def classify_file(fp: Path) -> dict:
    content = fp.read_text(encoding="utf-8", errors="replace")
    if len(content) > 10_000:
        content = content[:10_000] + "\n\n[…truncated at 10 000 chars]"
    msg = (
        f"File: {fp.name}\n\n"
        f"Content:\n```\n{content}\n```\n\n"
        "Choose which skills and functions to invoke, then classify."
    )
    return _call(CLASSIFY_SYSTEM, msg)


def synthesise_links(results: list[dict]) -> list[dict]:
    summary = json.dumps(
        [
            {
                "path":   r["_path"],
                "anchor": r.get("anchor_code"),
                "role":   r.get("material_role"),
                "note":   (r.get("decision_note") or "")[:120],
            }
            for r in results
        ],
        indent=2,
    )
    resp = _call(
        SYNTHESIS_SYSTEM,
        f"Classified files:\n{summary}\n\nFind meaningful file-to-file connections.",
        max_tokens=1024,
    )
    return resp.get("file_links", [])


# ─── Display ──────────────────────────────────────────────────────────────────

def _bar(value: float, width: int = 10) -> str:
    filled = min(int(value), width)
    return "█" * filled + "░" * (width - filled)


def show_graph(g: dict) -> None:
    nodes = g["nodes"]
    links = g["file_links"]
    print(f"\n╔══ DeweyGraph  {len(nodes)} nodes · {len(links)} file-links ══╗\n")
    for path, n in sorted(nodes.items()):
        marker = "✓" if n["archival_worthy"] else "✗"
        path_str = " → ".join(n.get("skill_path", []))
        print(f"  {marker}  {path}")
        print(f"      anchor={n['anchor']}  role={n['role']}")
        if path_str:
            print(f"      skills: {path_str}")
        for cl in n.get("class_links", []):
            print(
                f"      ⟶ {cl['target_class']:20s} [{cl['relation']}]"
                f"  {_bar(cl['heat'])} {cl['heat']}/10"
            )
        print()
    hot_links = [l for l in links if l["heat"] >= 4]
    if hot_links:
        print("  File links (heat ≥ 4):")
        for lk in sorted(hot_links, key=lambda x: -x["heat"]):
            print(
                f"    {lk['from']}\n"
                f"      ⟶ [{lk['relation']}  {_bar(lk['heat'])} {lk['heat']}/10]\n"
                f"    {lk['to']}"
            )
    print()


def show_heat(g: dict) -> None:
    print("\n╔══ Class Heat (Dewey pheromone trails) ══╗\n")
    class_h = g.get("class_heat", {})
    if class_h:
        for cls, h in sorted(class_h.items(), key=lambda x: -x[1])[:20]:
            print(f"  {cls:30s}  {h:6.1f}  {_bar(h, 20)}")
    else:
        print("  (empty — classify some files first)")

    print("\n╔══ Skill Path Heat (transition pheromones) ══╗\n")
    path_h = g.get("path_heat", {})
    if path_h:
        for seg, h in sorted(path_h.items(), key=lambda x: -x[1])[:20]:
            print(f"  {seg:45s}  {h:4d}  {_bar(h)}")
    else:
        print("  (empty — classify some files first)")
    print()


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("file",   nargs="?",       help="File to classify")
    parser.add_argument("--scan", metavar="DIR",   help="Classify every file in DIR")
    parser.add_argument("--graph",action="store_true", help="Show the link graph")
    parser.add_argument("--heat", action="store_true", help="Show heat maps")
    parser.add_argument("--raw",  action="store_true", help="Raw JSON output (single file only)")
    args = parser.parse_args()

    if not any([args.file, args.scan, args.graph, args.heat]):
        parser.print_help()
        return

    g = load_graph()

    if args.graph:
        show_graph(g)
        return
    if args.heat:
        show_heat(g)
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    # ── single file ──────────────────────────────────────────────────────────
    if args.file:
        fp = Path(args.file).resolve()
        if not fp.is_file():
            print(f"Error: '{args.file}' is not a file.", file=sys.stderr)
            sys.exit(1)

        try:
            result = classify_file(fp)
        except (json.JSONDecodeError, anthropic.APIError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        rel = str(fp.relative_to(ROOT)) if fp.is_relative_to(ROOT) else fp.name
        result["_path"] = rel
        add_node(g, rel, result)
        save_graph(g)

        if args.raw:
            print(json.dumps(result, indent=2))
            return

        path_str = " → ".join(result.get("skill_path", []))
        print(f"\n  File:      {fp.name}")
        print(f"  Anchor:    {result.get('anchor_code', '?')}")
        print(f"  Secondary: {', '.join(result.get('secondary_domains', []))}")
        print(f"  Role:      {result.get('material_role', '?')}")
        print(f"  Archival:  {'yes' if result.get('archival_worthy') else 'no'}")
        print(f"  Note:      {result.get('decision_note', '')}")
        print(f"  Skills:    {path_str}")
        for cl in result.get("class_links", []):
            print(
                f"  ⟶         {cl['target_class']:20s} [{cl['relation']}]"
                f"  {_bar(cl['heat'])} {cl['heat']}/10"
            )
        print()

    # ── folder scan ──────────────────────────────────────────────────────────
    elif args.scan:
        folder = Path(args.scan).resolve()
        if not folder.is_dir():
            print(f"Error: '{args.scan}' is not a directory.", file=sys.stderr)
            sys.exit(1)

        skip_ext = {".py", ".json", ".lock", ".env", ".gitignore", ".DS_Store"}
        files = sorted(
            p for p in folder.rglob("*")
            if p.is_file()
            and not any(part.startswith(".") for part in p.relative_to(folder).parts)
            and p.suffix not in skip_ext
            and p != GRAPH_PATH
        )

        if not files:
            print(f"No files found in '{args.scan}'.")
            return

        print(f"\n  Scanning {len(files)} file(s) in '{args.scan}' …\n")
        results: list[dict] = []

        for fp in files:
            rel = str(fp.relative_to(ROOT)) if fp.is_relative_to(ROOT) else fp.name
            print(f"  {rel} … ", end="", flush=True)
            try:
                result = classify_file(fp)
                result["_path"] = rel
                add_node(g, rel, result)
                results.append(result)
                path_str = "→".join(result.get("skill_path", []))
                print(f"{result.get('anchor_code', '?')}  [{path_str}]")
            except (json.JSONDecodeError, anthropic.APIError) as e:
                print(f"error: {e}")

        # Synthesis: find file-to-file cross-links across all classified items
        if len(results) > 1:
            print("\n  synthesising cross-links … ", end="", flush=True)
            try:
                raw_links = synthesise_links(results)
                add_file_links(g, raw_links)
                print(f"{len(raw_links)} forward → {len(g['file_links'])} bilateral")
            except (json.JSONDecodeError, anthropic.APIError) as e:
                print(f"warning: synthesis failed: {e}")

        save_graph(g)
        print()
        show_heat(g)


if __name__ == "__main__":
    main()

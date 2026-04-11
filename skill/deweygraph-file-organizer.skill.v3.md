# DeweyGraph File Organizer (v3)

## Author
TABARC-Code

## Purpose

Analyse folders, triage material, classify meaningful items with a single anchor, assign material roles, build typed bi-directional links, and generate Obsidian-ready notes.

---

## System context

Part of the TABARC-Code ecosystem.

This is a reasoning layer. It does not execute filesystem actions unless paired with external tooling.

---

## Core flow

1. Folder Typology
2. Archival Worthiness Filter
3. Material Role Assignment
4. Classification (anchor)
5. Relation linking
6. Note generation

---

## Folder types

- intake
- project
- archive
- reference
- export
- dump
- mixed

---

## Archival rule

Do not classify everything.
Only classify what is worth remembering.

---

## Material roles

- source
- process
- reference
- output
- residue
- duplicate-candidate

---

## Classification rules

- one item, one anchor
- subject is not lens
- format is not subject

---

## Notebook rule

Classify notebooks by role in archive, not internal mix.

---

## Duplicate rule

Duplicate decisions are advisory unless supported by real evidence.

---

## Output

Each item includes:
- anchor_code
- material_role
- relations
- decision_note

---

## Final rule

Clarity over completeness.

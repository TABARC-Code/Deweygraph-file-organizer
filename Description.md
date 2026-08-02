# Description

Author: TABARC-Code
Package: `deweygraph-file-organizer`
Version: 2.0.0
Identity code: `020.DGR` — library and information organisation

---

## One line

A Claude skill that triages, classifies, and graphs messy folders using Dewey-style anchors, material roles, and verified bi-directional relations.

## One paragraph

DeweyGraph turns unstructured folders into navigable archives. It types the folder, decides what's worth keeping before deciding how to classify it, gives each surviving item exactly one anchor code and one material role, builds typed relations that are verified to work in both directions, and emits Obsidian-ready notes and indices. It keeps a decision register so recurring edge cases get the same answer twice. It proposes structural changes; it doesn't make them.

---
My thinking is with everyone develping Obsidian secoond brains tis can be used to help organise and enable that secnd brain use flders like memories and sub skills wit better organisation. But like future thinking.
---

## Problem it addresses

Two failure modes, and most tools pick one and fall into the other.

**Tidy but meaningless.** Files sorted into type folders. Everything has a place, nothing has a reason. You can find `.pdf` files. You can't find the argument you were making in March.

**Linked but unfindable.** Everything tagged, everything cross-referenced, no canonical location. Six months in, the graph is dense and useless, and the answer to "where does this live" is "everywhere".

The gap between them is a system with **one address and many relationships**. Address first, relationships second — because relationships without addresses is just tagging, and addresses without relationships is just a filing cabinet.

---

## What makes it different

**The worthiness gate runs first.** Before any classification, each item is triaged: archival, reference, process, temporary, residue, duplicate candidate. Most systems classify everything and end up cataloguing installers and duplicate screenshots. This one refuses to, and says why.

**Anchor and role are separate axes.** *What it's about* and *what it's doing here* are different questions. Conflating them makes a draft and a final export look equally important.

**Reverse links are verified, not assumed.** Every relation must have a matching reverse. The verification is match-checking — flatten every triple, compute its required reverse, look it up, report a numeric ratio — not presence-checking, which is what everyone actually does and which passes broken graphs.

**Uncertainty is a first-class output.** `000` and `low` confidence are correct answers. The system is built so doubt gets recorded and reviewed rather than smoothed into a confident guess.

**It admits what it can't do.** Duplicate calls without hash or size evidence are marked advisory, out loud, every time.

---

## Architecture

Router root plus load-on-demand phases. `SKILL.md` routes; one phase file loads at a time; vocabulary references load only during classification and linking. Nothing holds the whole system in context.

**Sequential thinking** — numbered steps within each phase, explicit statement when one is skipped and why.

**Bidirectional flow** — later phases correct earlier ones. Phase 2's distribution check against phase 1's typology is the primary mechanism; a folder typed `archive` that produces 60% residue gets retyped, and the pipeline restarts from the corrected call.

**Feedback loops** — every phase declares positive signals that reinforce a pattern and negative signals that trigger a Kaizen pass. A user re-anchoring one item triggers re-examination of everything classified by the same reasoning, not a spot fix.

**Cross-fertilisation** — checks installed skills before inventing procedure. Supersedes two, defers to one for lighter jobs.

---

## Phases

| # | Phase | Question |
| --- | --- | --- |
| 0 | Inventory | What's actually here? (read-only scanner) |
| 1 | Folder typology | What kind of folder is this? |
| 2 | Archival worthiness | Is this worth keeping? |
| 3 | Material roles | What is it doing here? |
| 4 | Anchor classification | What is it about? |
| 5 | Relation graph | What does it connect to, both ways? |
| 6 | Note generation | What does the output look like? |
| 7 | Duplicate review | Sidecar. Evidence-tiered. |
| 8 | Decision register | Sidecar. Consulted before deciding. |

---

## Triggers

Fires on: organise a folder, tidy Downloads or Documents, classify or catalogue files, decide what's worth keeping, find duplicates, build a file inventory or organisation report, restructure a project or archive, generate Obsidian notes or folder indices or graph maps.

Also on looser phrasing: "what's in this folder", "what should I archive", "make sense of this mess", "sort my archive", "build me a vault from this", "which of these files matter".

---

## Constraints

- Reasoning layer. One read-only executable component. No filesystem mutation.
- Duplicate detection is advisory without hash, size, or timestamp evidence.
- Anchor vocabulary is Dewey-*inspired*, not DDC-conformant. It borrows the shape because the shape works and because numeric prefixes sort correctly. It does not claim library-standard compliance.
- Worthiness classes and material roles share three value names. Documented, not renamed — the names are the ones already in use. A known wart.

---

## Supersedes

`dewey-codebase-organiser` (scanner and report standard absorbed as phase 0) and `dewey-inspired-repository-organisation` (naming convention absorbed into phase 6). Retire both after install.

---

## Status

Production. Rebuilt 31 July 2026 from an eighteen-defect Kaizen audit, retained in-package as `KAIZEN-AUDIT.md`.

One outstanding item: `scripts/dewey_inventory.py` requires a manual copy, documented with its reason in `scripts/README.md`.

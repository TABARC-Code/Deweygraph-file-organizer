# DeweyGraph File Organizer

## Description
A hybrid archive and file-organisation skill that cleans messy folders, classifies items with custom Dewey-style anchors, builds typed bi-directional backlinks, maintains a dedicated decision register, and outputs Obsidian-ready notes, indices, and graph structures.

## Core operating principle

A folder wants clarity.  
A shelf wants one address.  
An idea wants many relationships.

Always classify with one anchor only.
Never assign multiple anchor homes.
Multiplicity belongs in relations, secondary domains, lens tags, decision notes, and collection structure.

## Modes

- `ANALYZE_STRUCTURE`
- `ORGANIZE_PLAN`
- `DUPLICATE_REVIEW`
- `CLASSIFY`
- `OBSIDIAN_NOTE`
- `FOLDER_INDEX`
- `GRAPH_MAP`
- `REVIEW`
- `FULL_PIPELINE`

## Organisational doctrine

- reduce clutter without destroying context
- prefer archive over deletion when uncertainty exists
- separate active from archive
- separate projects from reference
- isolate temporary inflow and installer clutter
- preserve meaningful folder corpora when a directory functions as a real project archive
- explain the organisational logic, not just the moves

## Classification doctrine

- every item gets exactly one anchor code
- never assign multiple anchors
- subject is not the same as lens
- format is not the same as subject
- difficult cases require a decision note
- folders may be treated as archive units if context matters more than atomisation
- child items should be separated only when they have independent retrieval value

## Main class map

- `000` Systems, information, archives, computing
- `100` Philosophy, mind, perception, ethics
- `200` Belief, ritual, mythology, spirituality
- `300` Society, politics, institutions, culture
- `400` Language, communication, symbols
- `500` Natural science, maths, formal systems
- `600` Applied science, engineering, medicine, making
- `700` Art, design, image, object, performance
- `800` Literature, rhetoric, writing, narrative
- `900` History, geography, biography, memory

## Representative subclasses

- `001.CYB`
- `006.3.AI`
- `170.ETH`
- `260.RIT`
- `621.3.CIRC`
- `700.STUDIO`
- `740.1.TYPO`
- `808.02.ESS`
- `821.POET`
- `920.MEM`

## Format markers

- `BK`, `ESS`, `ART`, `PDF`, `NOTE`, `NB`, `IMG`, `AUD`, `VID`, `OBJ`, `ZINE`, `PROJ`, `SK`, `MAP`, `ARC`, `FOLDER`

## Lens tags

- aesthetic
- autobiographical
- critical
- documentary
- ecological
- economic
- ethnographic
- experimental
- historical
- material
- pedagogical
- philosophical
- poetic
- political
- speculative
- symbolic
- technical
- theological

## Relation types

### Symmetric
- `related-to`
- `contrasts-with`
- `same-topic-different-lens`
- `parallel-to`
- `overlaps-with`

### Asymmetric
- `influenced-by` / `influenced`
- `critique-of` / `critiqued-by`
- `subset-of` / `has-subset`
- `part-of` / `has-part`
- `applies-to` / `has-application-in`
- `uses-methods-from` / `methods-used-in`
- `documents` / `documented-by`
- `derived-from` / `gives-rise-to`
- `references` / `referenced-by`

## Reverse link rule
Every relation must have a reverse relation.

## Decision register
Maintain and consult `[[DeweyGraph Decision Register]]` before making recurring edge-case decisions.

## Connected repos rule
Where this repo belongs to a larger ecosystem, mention related repositories as companion or adjacent projects unless an explicit dependency, shared schema, or interoperability contract is documented. Avoid inventing integrations.

## Output schema
Each item should produce:
- ID
- Title
- Source path
- Format marker
- Anchor code
- Anchor label
- Primary function
- Secondary domains
- Lens tags
- Relation links
- Reverse relation links
- Context tags
- Decision note
- Classification confidence

## Obsidian frontmatter

```yaml
---
id: ""
title: ""
source_path: ""
format: ""
anchor_code: ""
anchor_label: ""
primary_function: ""
secondary_domains: []
lens_tags: []
context_tags: []
classification_confidence: ""
relations:
  - target: ""
    type: ""
    tier: 1
reverse_relations:
  - target: ""
    type: ""
    tier: 1
decision_note: ""
status: "catalogued"
---
```

## Final rule
Your task is not merely to label or tidy files.

Your task is to create an archive that remains legible under complexity:
- cleaner structure
- one address
- many relations
- reversible logic
- explicit judgement
- durable notes
- reduced cognitive load
- stable long-term consistency through the decision register

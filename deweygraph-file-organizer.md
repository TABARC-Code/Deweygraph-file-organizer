---
name: deweygraph-file-organizer
description: Organise, triage, classify, and graph messy folders and archives using Dewey-style anchors, material roles, and typed bi-directional relations. Use when asked to organise or tidy a folder, clean up Downloads or Documents, classify or catalogue files, decide what is worth keeping, find duplicates, build a file inventory or organisation report, restructure a project or archive directory, or generate Obsidian notes, folder indices, and graph maps from a set of files. Also triggers on "what's in this folder", "what should I archive", "make sense of this mess", "sort my archive", "build me a vault from this", "which of these files matter", and any request to catalogue, index, or impose structure on unstructured material.
---

# DeweyGraph File Organizer

Author: TABARC-Code
Identity code: `020.DGR`
Version: 2.0.0

A folder wants clarity.
A shelf wants one address.
An idea wants many relationships.

---

## Overview

This skill turns messy folders into navigable archives. It does not move, rename, or delete anything on its own — every structural change is a proposal. Its core model:

1. **Folder typology** — what kind of folder is this? Knowing that changes everything that follows.
2. **Archival worthiness** — is this worth cataloguing at all? This gate runs *before* classification.
3. **Material role** — what is it doing in the archive? Source, process, reference, output, residue, duplicate-candidate.
4. **One anchor per item** — exactly one Dewey-style classification. Multiplicity lives in relations, secondary domains, and lens tags.
5. **Typed, reversible relations** — every link works both ways, verified by matching.
6. **Decision register** — a persistent record so recurring edge cases get the same answer twice.

---

## How to use it

Point it at a folder:

> organise my Downloads
> what's worth keeping in this archive
> classify these files and build me an Obsidian vault
> find duplicates
> make sense of this mess

The skill routes internally and does the work stage by stage. You don't name phases.

---

## The six-phase pipeline

### Phase 1 — Folder Typology

**Question:** what kind of folder is this?

**Types:**
- **intake** — unsorted incoming material. Downloads, scans, exports awaiting review. Don't classify deeply; most won't survive phase 2.
- **project** — coherent working set. Preserve structure. The folder itself may be the archival unit.
- **archive** — completed, stable material. This is what the system is for. Classify deeply.
- **reference** — external material only. Papers, manuals, downloads someone else authored. Classify lightly.
- **export** — machine-generated outputs. Renders, builds, conversions. Usually don't need individual records.
- **dump** — no structure, no coherence. Organise before classifying.
- **mixed** — genuinely two or more types. Split conceptually first, then type each part.

**Steps:**
1. List the folder — top level first, one level deep.
2. Read local context if present: README, AGENTS.md, folder-info.md, manifests, project notes.
3. Check date spread — tight clustering suggests a project; wide scatter suggests a dump.
4. Check naming coherence — consistent names suggest intent; final_v2 (1) copy.pdf suggests otherwise.
5. Assign one type and state the evidence.

**Upstream returns:** Phase 2's distribution check will send you back here if the typology was wrong. That's the main bidirectional mechanism.

---

### Phase 2 — Archival Worthiness

**Question:** is this worth keeping at all?

**The five questions:**
1. Does this item have ongoing value?
2. Is it part of a meaningful project or corpus?
3. Would I want to find this again *on purpose*?
4. Does it contain original thought, process, evidence, or finished output?
5. Is it merely transient — download residue, export duplicate, byproduct?

Question three does most of the work.

**Worthiness classes:**
- **archival** — clear long-term value. Core project notes, source files, meaningful drafts, technical notebooks, original research, final outputs, project-defining references.
- **reference** — matters, but as support. External papers, manuals, standards, inspiration images, copied articles.
- **process** — captures active making. Work-in-progress sketches, prototype photos, lab notes, iteration exports with traceable value.
- **temporary/intake** — hasn't earned archival status yet. Downloads awaiting triage, unreviewed exports, unsorted scans, installers.
- **residue** — noise. Cache artefacts, redundant exports, accidental duplicates, empty placeholders, screenshots with no enduring relevance.
- **duplicate-candidate** — appears to duplicate another item or version.

**Hard rule:** Do not dignify every file with metadata. Some files are just files. Some are litter. A decent system knows the difference.

**Minimum threshold for a full record:** passes at least one of these:
- it is original work
- it belongs to a meaningful project corpus
- it has clear future retrieval value
- it is a significant reference
- it records process that will be useful later

**Distribution sanity check:** compare against the phase 1 typology. Archive should produce mostly archival and reference. Project should produce mostly source and process. Intake should produce mostly temporary and residue. If the distribution contradicts the typology, return to phase 1 and re-type.

---

### Phase 3 — Material Roles

**Question:** what is it doing in the archive?

Classification tells you what something is *about*. Role tells you what it's *doing here*.

**The six roles:**
- **source** — origin of thought, design, or data. Original documents, primary datasets, authored text, master design files.
- **process** — intermediate work. Sketches, drafts, test outputs, lab notes. Process material from finished work is where reasoning is preserved.
- **reference** — external or supporting material. Papers, manuals, standards, inspiration images.
- **output** — finalised or exported artefacts. PDFs of finished work, rendered images, published versions.
- **residue** — low-value leftovers, noise, artefacts. If you're assigning this, phase 2 was too generous.
- **duplicate-candidate** — suspected duplicate or unstable version. Hands off to phase 7.

**Rules:**
- Each item takes exactly one role.
- Roles do not replace anchors. Both are assigned.
- Roles set note depth: source and process earn full records; output and reference earn short ones; residue earns none.

**The collection test:** if an item won't take one role — a folder containing a master file, three drafts, and a render — it isn't an item. It's a collection. Collections get their own record with role `source`, a folder index note, and `has-part` relations to children with independent retrieval value.

---

### Phase 4 — Anchor Classification

**Question:** what is it about?

One item, one anchor. This is the rule the whole system rests on.

**Selection discipline:**

- **Dominant function, not incidental theme.** A circuit diagram in a mythology book is still a circuit diagram if the diagram is the point.
- **Subject is not lens.** A political reading of a poem anchors under poetry with lens `political`, not under politics.
- **Format is not subject.** A PDF is not a subject. A video essay about ecology anchors under ecology, format marker `VID`.
- **Prefer the most specific useful code**, not the most specific available. `800` is better than inventing `808.02.ESS.SUB`.
- **When evidence is weak, use `000`.** Unclassified is an honest answer. Inventing certainty is worse than recording doubt.

**The Notebook Rule (resolved):**

Classify a notebook by its dominant role in the archive, not by its internal content mix.

| Notebook | Anchor |
| --- | --- |
| Studio or project notebook | `700.STUDIO` |
| Electronics or lab notebook | `621.3.CIRC` |
| Drawing-dominant sketchbook | `741.SKETCH` |
| Poetry or literary notebook | `821.POET` |
| Personal journal | `920.MEM` |
| Research notebook for a defined project | the project's dominant class |

When no role dominates, treat the notebook as a parent collection.

**Legal anchor vocabulary:**

| Code | Label |
| --- | --- |
| `000` | General works and unclassified |
| `001.CYB` | Cybernetics and systems theory |
| `005` | Software and programming |
| `006.3.AI` | Artificial intelligence and machine learning |
| `020` | Library and information organisation |
| `020.DGR` | DeweyGraph system itself |
| `030` | Reference documentation |
| `100` | Philosophy and psychology |
| `170.ETH` | Ethics and moral reasoning |
| `200` | Belief, ritual, mythology, spirituality |
| `260.RIT` | Ritual and practice |
| `291.MYTH` | Comparative mythology and symbolic systems |
| `300` | Society, politics, institutions, culture |
| `320.POL` | Politics and governance |
| `330.ECON` | Economics and trade |
| `400` | Language, communication, symbols |
| `410.LING` | Linguistics and terminology |
| `500` | Natural science, maths, formal systems |
| `510.MATH` | Mathematics and formal systems |
| `519.STAT` | Statistics and probability |
| `570.BIO` | Biology and ecology |
| `600` | Applied science, engineering, medicine, making |
| `621.3.CIRC` | Electronics and circuits |
| `621.9.FAB` | Fabrication, machining, 3D printing |
| `629.AUTO` | Automation and control systems |
| `640.CRAFT` | Craft, making, domestic technology |
| `700` | Art, design, image, object, performance |
| `700.STUDIO` | Studio practice and project archives |
| `740.1.TYPO` | Typography and lettering |
| `741.SKETCH` | Drawing and sketchbooks |
| `760.PRINT` | Printmaking and reproduction |
| `770.PHOTO` | Photography |
| `780.AUD` | Music and audio |
| `791.VID` | Film, video, moving image |
| `793.GAME` | Games, rules, and recreation |
| `800` | Literature, rhetoric, writing, narrative |
| `808.02.ESS` | Essays and non-fiction craft |
| `809.CRIT` | Criticism and commentary |
| `813.FIC` | Fiction and narrative prose |
| `821.POET` | Poetry |
| `822.DRAM` | Drama and script |
| `900` | History, geography, biography, memory |
| `910.GEO` | Geography, places, gazetteers |
| `909.TIME` | Chronology and timelines |
| `920.MEM` | Biography, memoir, personal journals |

**Format markers** (recorded separately from anchor):

BK · ESS · ART · PDF · NOTE · NB · IMG · AUD · VID · OBJ · ZINE · PROJ · SK · MAP · ARC · FOLDER · CODE · DATA

**Lens tags** (perspective, not subject, 0–4 per item):

aesthetic · autobiographical · critical · documentary · ecological · economic · ethnographic · experimental · historical · material · pedagogical · philosophical · poetic · political · speculative · symbolic · technical · theological

---

### Phase 5 — Relation Graph

**Question:** what does it connect to, both ways?

The anchor gives an item one address. Relations give it everything else.

**Symmetric relations** (both sides must be written):

| Type | Use for |
| --- | --- |
| `related-to` | General association. Fallback only. |
| `contrasts-with` | Deliberate opposition or counter-example |
| `same-topic-different-lens` | Same subject, different perspective |
| `parallel-to` | Independent works developed alongside each other |
| `overlaps-with` | Partial subject overlap without dependency |

**Asymmetric relations** (both sides must be written, but different types):

| Forward | Reverse | Use for |
| --- | --- | --- |
| `influenced-by` | `influenced` | Intellectual or aesthetic debt |
| `critique-of` | `critiqued-by` | Direct critical engagement |
| `subset-of` | `has-subset` | Conceptual containment |
| `part-of` | `has-part` | Physical or structural containment |
| `applies-to` | `has-application-in` | Method or theory applied to a domain |
| `uses-methods-from` | `methods-used-in` | Borrowed technique |
| `documents` | `documented-by` | Record of process, object, or event |
| `derived-from` | `gives-rise-to` | Versions, adaptations, descendants |
| `references` | `referenced-by` | Explicit citation |

**Tiers:**

| Tier | Meaning |
| --- | --- |
| 1 | Structural. Removing it misrepresents the archive. Containment, direct derivation, explicit citation. |
| 2 | Substantive. A real connection, but the archive survives without it. |
| 3 | Associative. Loose thematic link. Hidden by default, surfaced on request. |

**Verification by match-checking (not presence-checking):**

This is the procedure. It is mandatory.

1. Flatten every relation into `(source, type, target)` triples.
2. For each triple, compute the required reverse: `(target, reverse(type), source)`.
3. Look up that exact triple in the flattened list.
4. Check every target exists as a node.
5. Report numerically: `n/m matched, x missing, y dangling`.

A graph with any missing reverse or dangling target is **FAIL**. Say FAIL. Don't soften it.

**Discipline:**

- `related-to` is the last resort. It's the vaguest type and most over-used.
- Containment is `part-of`, never `related-to`.
- Cap at roughly six per item. More usually means the item is a collection.
- No forward references. Don't relate to an item not yet classified.
- Reference material gets few relations. Restrict to edges you'd actually traverse.

---

### Phase 6 — Note Generation

**Question:** what does the output look like?

**Note depth by role:**

| Role | Depth |
| --- | --- |
| source | Full note — summary, classification, all relations, context, decision note |
| process | Full note if part of a project corpus; short note with `part-of` link otherwise |
| reference | Short note — classification, one-line summary, minimal relations |
| output | Short note, or fold into the parent collection's index |
| residue | No note. It failed phase 2 for a reason. |
| duplicate-candidate | No note until phase 7 resolves it. |

**Naming convention:**

Folders: `DDD-kebab-case` — three-digit class, hyphen, lowercase kebab.
Item notes: `<anchor>-<kebab-title>.md`
Folder indices: `README.md` at folder root, `folder-info.md` for structured frontmatter.

**Frontmatter (every field present, even if empty):**

```yaml
---
id: ""
title: ""
source_path: ""
format: ""
anchor_code: ""
anchor_label: ""
material_role: ""
primary_function: ""
secondary_domains: []
lens_tags: []
context_tags: []
classification_confidence: ""
relations:
  - target: ""
    type: ""
    tier: 2
reverse_relations:
  - target: ""
    type: ""
    tier: 2
decision_note: ""
worthiness_class: ""
status: "catalogued"
---
```

**Confidence scale:**

| Value | Meaning | Test |
| --- | --- | --- |
| high | Content inspected, anchor unambiguous | You'd defend this without hedging |
| medium | Content inspected, some ambiguity, or strong contextual evidence without inspection | You'd defend it but note an alternative |
| low | Weak evidence. Named, extension, neighbours only. | You'd want it reviewed |
| provisional | Content not inspectable. Placeholder. | Not really a classification yet |

**Validation before writing:**

1. All required fields present
2. `anchor_code` exists in the vocabulary
3. `anchor_label` matches that entry
4. `format` is a legal marker
5. `material_role` is one of six
6. `worthiness_class` is one of six
7. `classification_confidence` uses the scale above
8. Every `lens_tags` entry is legal
9. Every relation `type` is legal with a tier of 1, 2, or 3
10. `reverse_relations` non-empty if `relations` non-empty
11. Every relation target resolves to an existing record

A note that fails validation doesn't get written. Fix the record, then generate.

---

### Phase 7 — Duplicate Review (optional sidecar)

**Question:** which files are actually duplicates?

**The honesty clause:** this skill is reasoning only. Without evidence — hashes, byte sizes, timestamps, content comparison — every duplicate call is advisory, permanently, by construction. Say "advisory" out loud.

**Evidence tiers:**

| Tier | Evidence | Strength |
| --- | --- | --- |
| Confirmed | Matching hash | Authoritative. These are the same file. |
| Strong | Identical size + compatible timestamps + same extension | Near-certain. Safe to recommend a keeper. |
| Probable | Identical size, or content comparison | Recommend, but flag residual doubt. |
| Advisory | Filename pattern only — `file (1).pdf`, `_copy`, `_v2`, `final_final` | Suggest review. Recommend nothing. |
| Speculative | Similar names, different sizes | Report observation. Draw no conclusion. |

**For each group:**
- Assign an evidence tier per group
- Nominate a keeper — only at Probable or above
- Recommend an action

**Actions:**

| Action | When |
| --- | --- |
| Keep | The nominated keeper |
| Archive | Any copy with residual doubt. Default under uncertainty. |
| Review | Advisory and Speculative tiers |
| Delete | Only at Confirmed tier, only with explicit user approval, never on the skill's initiative |

Archive beats delete. Storage is cheap.

---

### Phase 8 — Decision Register (optional sidecar)

**Question:** have we solved this before?

This is the system's memory. **Consult before deciding, not after.** A register you only write to is a diary. A register you read first is a policy.

**When to write an entry:**

- the same edge case has now come up twice
- a tie-break needed reasoning that would be tedious to reconstruct
- a vocabulary extension was proposed
- a user correction revealed a systemic misreading
- the answer is non-obvious and future-you will disagree with present-you

**Entry template:**

```markdown
## Entry <nnn>

### Rule
<one sentence, imperative>

### Reason
<why this rule and not the obvious alternative>

### Trigger pattern
<what material this fires on>

### Anchor guidance
<specific code mappings>

### Link guidance
<relation types this case tends to need>

### Organisation guidance
<what to do with the files themselves>

### Example
<one concrete case>

### Supersedes
<entry numbers or documents this replaces, or "nothing">

### Status
active | superseded | retired

### Reviewed
<date> — <what triggered the review>
```

**Consistency pass before publishing any entry:**

1. Entry vs subskills — does it contradict a rule stated above? Subskills win.
2. Entry vs entry — do two entries give different answers to the same trigger? Merge or mark older superseded.
3. Entry vs vocabulary — does it reference an anchor code absent from the vocabulary above? Add the code or fix the entry.
4. Orphan check — any entry whose trigger hasn't fired in a long time? Mark for review, not deletion.

---

## Feedback loops

Every classification decision emits a signal.

**Positive — reinforce:**
- User accepts an anchor without amendment → that anchor-for-that-evidence pattern is confirmed
- A relation gets traversed later → that relation earned its place
- A folder stays organised at next review → the typology call was right
- An entry applied cleanly to a new case → the trigger pattern is drawn at the right level of generality

**Negative — trigger a Kaizen pass:**
- User re-anchors an item → find everything classified under the same reasoning and re-examine it
- Same edge case adjudicated twice without a register entry → the register has a gap
- `low` confidence appears more than twice in one folder → the vocabulary doesn't fit
- Any reverse link fails match-verification → re-verify the whole graph, not one edge
- An entry needs amending on its second application → it was written too specifically

---

## Hard rules

1. **One anchor per item.** Multiplicity lives in relations, secondary domains, and lens tags.
2. **Worthiness before classification.** Decide *whether* to catalogue before deciding *how*.
3. **Every relation has a matching reverse.** Verified by matching, not by presence.
4. **Nothing deleted on the skill's initiative.** Archive beats delete under uncertainty.
5. **Duplicate calls are advisory** unless hashes, timestamps, or content comparison support them.
6. **Difficult calls get a decision note.** If it took thought, record the thought.
7. **Uncertainty is stated, not hidden.** `000` and `low` confidence are real answers.

---

## Working example — five-file folder

Input:
```
Downloads/
├── IMG_0847.png
├── IMG_0847 (1).png
├── attention-is-all-you-need.pdf
├── notes.txt
└── installer.dmg
```

**Phase 1 — typology:** `intake` — mixed-origin, no structure, download artefacts.

**Phase 2 — worthiness:**
- IMG_0847.png → residue (screenshot, no enduring relevance)
- IMG_0847 (1).png → duplicate-candidate
- attention-is-all-you-need.pdf → reference (external paper)
- notes.txt → process (original thought)
- installer.dmg → residue (archetypal thing not to catalogue)

**Result:** 2 worth cataloguing (reference + process), 2 residue, 1 duplicate candidate. Distribution check passes (intake expects mostly temp/residue).

**Phase 3 — roles:**
- attention-is-all-you-need.pdf → `reference`
- notes.txt → `process`

**Phase 4 — anchors:**
- attention-is-all-you-need.pdf → `006.3.AI` (high confidence)
- notes.txt → `000` (low confidence — no subject evidence, sits beside unrelated items)

**Phase 5 — relations:**
No relations. notes.txt is `000` and links nowhere honest.

**Phase 6 — notes:**
- attention-is-all-you-need.pdf → short note
- notes.txt → short note, status `pending-review`

**Result:** 54 files in, 2 notes out. Residue ignored. Duplicates flagged for review, not resolved yet.

---

## Sequential thinking protocol

Within each phase, number the steps and do them in order. If a step is skipped, say so and say why. No silent skips.

State which phase you're in when you start it. The user should never have to guess whether you're still triaging or already classifying.

---

## Bidirectional flow

The pipeline is not a one-way conveyor. Later phases correct earlier ones.

| Discovery | Returns to | What happens |
| --- | --- | --- |
| Most items fail the worthiness gate | Phase 1 | Folder was probably `dump`, not `project`. Re-type it. |
| Anchors scatter across five unrelated classes | Phase 1 | Folder is `mixed`. Split before continuing. |
| Item resists a single anchor | Phase 3 | Likely a collection. Handle as one. |
| Relations all point outside the folder | Phase 1 | This is `reference`, not `archive`. |
| Same edge case appears three times | Phase 8 | Stop. Write a register rule. Then resume. |

When you return upstream, say so out loud and say what triggered it.

---

## Token limit protocol

If response limit is reached mid-task: stop at a clean item or section boundary, write `CONTINUATION POINT: [what's next]`, and preserve structure. On continuation, resume exactly there without restating completed work.

For large folders: batch by top-level directory, complete each batch fully, carry only the register and anchor tally forward.

---

## Expected output

Depending on what was asked:

1. A folder typology call with evidence
2. A worthiness triage with counts per class
3. Classified item records conforming to the schema above
4. A relation graph with every reverse link match-verified
5. Obsidian notes and folder indices
6. A duplicate report, marked advisory or evidenced
7. New or amended register entries
8. A short Kaizen note when a negative signal fired

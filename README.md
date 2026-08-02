# DeweyGraph File Organizer

**A Claude skill for turning messy folders into archives you can still navigate in five years.**

Author: TABARC-Code
Version: 2.0.0
Identity code: `020.DGR`

---

A folder wants clarity.
A shelf wants one address.
An idea wants many relationships.

Most file organisation tools solve the first line and ignore the other two. You end up with tidy folders and no idea why anything is where it is. Most knowledge-management systems do the reverse — infinite tagging, infinite linking, and no shelf. Six months in, everything is tagged and nothing is findable.

This one does both, and it does them in that order, because order matters.

---

## What it actually does

Point it at a folder. It will:

1. Work out what kind of folder it is — because a project folder is not Downloads, and treating them the same produces bad decisions in both.
2. Decide what's worth keeping. **Before** classifying. This gate is the whole point.
3. Assign each surviving item one anchor code, and one material role.
4. Build typed relations that work in both directions, and verify they actually do.
5. Generate Obsidian-ready notes, folder indices, and a graph map.
6. Record its own difficult judgement calls so it doesn't contradict itself next month.

What it won't do is move, rename, or delete anything on its own initiative. Everything structural is a proposal. There's one executable component, a read-only inventory scanner, and it only reads.

---

## The idea in one paragraph

Every item gets exactly one anchor — one address, one shelf, one place it lives. Multiplicity is real and it goes into relations, secondary domains, and lens tags. Allow two anchors and within a month you have tagging with extra steps and nothing has a home.

Separately from *what it's about*, every item gets a **material role**: what it's actually doing in the archive. Source, process, reference, output, residue. Without that axis a draft and a final export look equally important, and they aren't.

And before either of those questions, there's a gate: **is this worth cataloguing at all?** Plenty of systems skip it and end up lovingly indexing installer packages and duplicate screenshots. That isn't sophistication. It's administrative cosplay.

---

## Install

Drop the folder into your skills directory:

```text
~/.claude/skills/deweygraph-file-organizer/
```

or on Windows:

```text
%USERPROFILE%\.codex\skills\deweygraph-file-organizer\
```

Claude picks it up from the frontmatter in `SKILL.md`. No configuration.

One outstanding step: `scripts/dewey_inventory.py` needs copying in. See `scripts/README.md` — there's a reason it isn't bundled and the reason is honest.

---

## Use

Just ask. The description is written to fire on natural phrasing:

> organise my Downloads folder
> what's actually worth keeping in here
> classify these files and build me an Obsidian vault
> find the duplicates in this archive
> make sense of this mess

You don't need to name phases or modes. It routes internally.

If you want a specific phase, ask for it:

> just do the worthiness triage, don't classify yet
> run a duplicate audit on this folder
> check the reverse links in my existing graph

---

## Structure

```text
SKILL.md                  router root — read this, pick a phase, load one file
subskills/
  01-folder-typology      what kind of folder is this
  02-archival-worthiness  the gate. is this worth keeping
  03-material-roles       what is it doing here
  04-anchor-classification what is it about. one anchor, no exceptions
  05-relation-graph       typed links, and the verification that makes them real
  06-note-generation      Obsidian output
  07-duplicate-review     sidecar. evidence tiers, honest about its limits
  08-decision-register    sidecar. the memory that stops it contradicting itself
references/
  anchor-vocabulary       the legal class map
  relation-vocabulary     relation types, reverses, tiers
  schema                  field definitions, confidence scale, validation
templates/                item note, folder index, decision register
examples/                 worked pipeline, verified graph map
scripts/                  read-only inventory scanner
```

Token discipline: the root routes, and one phase file loads at a time. Vocabulary references load only when you're actually classifying. Nothing holds the whole system in context, because the whole system doesn't fit and pretending otherwise degrades everything.

---

## What changed in 2.0

The previous version had a good model and a broken package (I messedup tired.). Eighteen defects, four critical. The audit is preserved as `KAIZEN-AUDIT.md` because deleting your own defect list is how you repeat it.

The interesting one: the file demonstrating the reverse-link rule broke that rule in four of five relations, with two links pointing at nodes nobody had written. It survived review because reviewers check whether links are *present*, not whether they *match*. Presence-checking passes that file. Match-checking fails it 80%.

So phase 5 now specifies match-checking as a procedure with a numeric output, rather than stating the rule and hoping. Rules everybody agrees with are exactly the rules that get quietly broken, because nobody thinks to check something so obvious.

Also: three competing versions collapsed into one — and the newest had been the thinnest, dropping the class map, relation vocabulary, lens tags, and mode list, so anyone following version numbers got the weakest system. Notebooks had three contradictory rules across four documents, one of them in the register built to prevent contradictions. And the repository about deduplication was shipping `material-roles.md` alongside `material-roles-v2.md` with no precedence rule, which by its own taxonomy was a `duplicate-candidate` requiring a decision note.

Full list in `CHANGELOG.md`.

---

## Supersedes

Two earlier skills fold into this one:

- **dewey-codebase-organiser** — had the working scanner and a solid report standard, no relations or roles or worthiness gate. Its scanner is now phase 0.
- **dewey-inspired-repository-organisation** — eight lines, and a description field reading `"Imported local Codex skill from SKILL.md."`, which would never have triggered on anything. Its `DDD-kebab-case` naming convention was worth keeping and is absorbed into phase 6.

Retire both once the scanner copy is done.

---

## Design commitments

Things this deliberately won't do, in case they look like oversights: They're not...

- **No auto-delete.** Archive beats delete under uncertainty. Storage is cheap; the file you needed isn't.
- **No confident duplicate calls without evidence.** Filename patterns get you *advisory*, and it says "advisory" out loud. A confident-sounding recommendation backed by nothing is how people delete the wrong copy.
- **No "miscellaneous" category.** `000` is the honest bucket and it's meant to be visibly uncomfortable, so it gets reviewed. Comfortable catch-alls fill up and never empty.
- **No inherited guesses.** An item whose contents can't be inspected gets `000` and `low` confidence, not an anchor borrowed from whatever it happened to sit beside. Confident wrong answers don't get reviewed. That's what makes them expensive.

---

## Spelling

"Organizer" in the repo name, "organisation" in the prose. The repo name is effectively locked; the prose is UK English. It's inconsistent and it's staying that way, so here's the note saying it's deliberate rather than sloppy.

---

## Licence

See repository. Companion projects listed in the repo description — companions, not dependencies. Nothing here requires anything there.

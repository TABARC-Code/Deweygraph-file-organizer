---
name: managing-writing-projects
description: Use when organizing a writing project's files, managing draft versions, working on multiple story variants simultaneously, or setting up a new novel project structure
---

# Managing Writing Projects

## Overview

A well-organized writing project prevents lost work, enables clean version management, and makes it possible to work on multiple threads without confusion.

**Core principle:** Files are drafts, not decisions. Version your work so you can always go back.

## Standard Project Structure

For any novel or major writing project, use this directory structure:

```
[project-root]/
  docs/
    novel-superpowers/
      bibles/
        YYYY-MM-DD-[title]-bible.md       ← story bible
      outlines/
        YYYY-MM-DD-[title]-outline.md     ← chapter/scene outline
      characters/
        [character-name]-profile.md       ← one profile per character
      world/
        [world-name]-worldbook.md         ← world-building documents
      continuity-log.md                   ← running continuity log
  drafts/
    [title]/
      ch01-[chapter-title].md             ← one file per chapter
      ch02-[chapter-title].md
      ...
  manuscripts/
    [title]-draft-v1-YYYY-MM-DD.md        ← compiled drafts
    [title]-draft-v2-YYYY-MM-DD.md
  archives/
    [title]/
      draft-v1-YYYY-MM-DD/                ← versioned archives
      draft-v2-YYYY-MM-DD/
  submissions/
    [title]-submission-YYYY-MM-DD.md      ← submission-formatted manuscript
```

## Draft Version Management

### When to Create a New Version

Create a new version (`draft-v2`, `draft-v3`) when:
- Beginning a structural revision (acts, major plot changes)
- Starting a new pass after receiving significant editorial feedback
- Branching to explore a different story direction

Do NOT create new versions for:
- Line edits on an existing draft
- Scene-level revisions within the same structural pass
- Continuity fixes

### Naming Conventions

| File type | Convention | Example |
|-----------|-----------|---------|
| Chapter draft | `ch[NN]-[slug].md` | `ch03-the-crossing.md` |
| Compiled manuscript | `[title]-draft-v[N]-YYYY-MM-DD.md` | `ember-road-draft-v2-2026-05-03.md` |
| Story bible | `YYYY-MM-DD-[title]-bible.md` | `2026-05-03-ember-road-bible.md` |
| Outline | `YYYY-MM-DD-[title]-outline.md` | `2026-05-03-ember-road-outline.md` |
| Character profile | `[character-name]-profile.md` | `elara-profile.md` |

### Using Git for Writing Projects

Git is not just for code. For writing projects:

```bash
# Initialize a writing repo
git init [project-name]
cd [project-name]

# Create the structure
mkdir -p docs/novel-superpowers/{bibles,outlines,characters,world}
mkdir -p drafts/[title] manuscripts archives submissions

# Commit the story bible when approved
git add docs/novel-superpowers/bibles/
git commit -m "feat: add story bible for [title]"

# Commit the outline when approved
git add docs/novel-superpowers/outlines/
git commit -m "feat: add outline for [title]"

# Commit each chapter as it completes
git add drafts/[title]/ch01-*.md
git commit -m "draft: complete chapter 1 - [chapter title]"
```

**Commit messages for writing:**
- `feat: add [story bible / outline / character profile]`
- `draft: complete chapter N — [chapter title]`
- `revise: [what changed and why]`
- `fix: continuity — [what was fixed]`

### Branching for Story Variants

When exploring a story direction that might not work:

```bash
# Create a branch for the experimental variant
git checkout -b [title]-variant-[description]

# Write the variant in this branch
# If it works: merge back
git checkout main
git merge [title]-variant-[description]

# If it doesn't: simply delete the branch and return to main
git checkout main
git branch -d [title]-variant-[description]
```

Use branches for:
- "What if the story started here instead?"
- "What if this character dies in Chapter 5?"
- Testing a different structural approach (e.g., linear vs. non-linear timeline)

## Multi-Book Projects

For series or multi-book projects:

```
[series-root]/
  series-bible.md                         ← overarching series facts, timeline, world
  docs/
    novel-superpowers/
      world/                              ← shared world documents
      characters/                         ← shared character profiles
  book-01-[title]/
    docs/novel-superpowers/
      bibles/                             ← book-specific bible
      outlines/                           ← book-specific outline
      continuity-log.md
    drafts/
    manuscripts/
  book-02-[title]/
    ...
```

**Series continuity log:** Maintain a separate continuity log at the series level that tracks facts that must persist across all books: character states at the end of each book, world-changing events, promises made to the reader.

## Project Setup Checklist

When starting a new novel project:

- [ ] Create directory structure
- [ ] Initialize git repository
- [ ] Complete story brainstorming → story bible saved to `docs/novel-superpowers/bibles/`
- [ ] Create `docs/novel-superpowers/continuity-log.md`
- [ ] Create character profiles for all significant characters
- [ ] Create world documents for all required world systems
- [ ] Complete story outlining → outline saved to `docs/novel-superpowers/outlines/`
- [ ] Begin drafting

## Finding Your Way in a Large Project

When returning to a project after a break or working on a long manuscript:

1. Read `docs/novel-superpowers/continuity-log.md` — this tells you the current story state
2. Read the most recent chapter in `drafts/[title]/` — this gives you the voice and where you left off
3. Check `docs/novel-superpowers/outlines/` — this tells you where the story is going next
4. Check character profiles for any characters appearing in the next chapter

Do not read the entire manuscript from the beginning. Use the documents.

---
name: story-outlining
description: Use when you have an approved story bible or narrative concept and need to create a structured writing plan before drafting begins
---

# Story Outlining

## Overview

Write comprehensive story outlines assuming the drafter has the story bible but needs granular scene-by-scene guidance. Document everything they need to know: which characters appear in each scene, what happens and why, what emotional beats land, how scenes connect, what continuity must be tracked, and how each scene advances the story.

Assume they are a skilled writer, but know almost nothing about this specific story's internal logic.

**Announce at start:** "I'm using the story-outlining skill to create the story outline."

**Context:** This should be run after brainstorming is complete and the story bible has been approved.

**Save outlines to:** `docs/novel-superpowers/outlines/YYYY-MM-DD-<title>-outline.md`

## Scope Check

If the bible covers multiple volumes, a complete series, or more than one independent narrative arc, it should have been decomposed during brainstorming. If it wasn't, suggest breaking this into separate outlines — one per volume or arc. Each outline should produce a complete, satisfying narrative unit on its own.

## Structure Architecture

Before defining scenes, map out the narrative architecture:

- **Act structure:** Identify act breaks and the major turning points (inciting incident, midpoint reversal, all-is-lost moment, climax, resolution)
- **Character arcs:** Map how each main character changes from opening to close
- **Thematic throughline:** Identify the story's central question and how each act moves toward its answer
- **POV structure:** Which character(s) carry which sections; note any POV shifts

For nonfiction: map chapter clusters by concept, skill level, or chronological phase.

## Scene-Level Granularity

**Each scene entry should contain:**
- Scene number and chapter assignment
- Location and time (when in story-world timeline)
- POV character (if applicable)
- Characters present
- Scene goal: what does the POV character want in this scene?
- Scene conflict: what opposes them?
- Scene outcome: do they get it (yes, but / no, and worse / yes, and better)?
- Key story information revealed or withheld
- Continuity flags: facts established that later scenes must honor
- Emotional beat: what should the reader feel?
- Transition note: how does this scene connect to the next?

For nonfiction chapters: replace scene goal/conflict/outcome with learning objective, key concepts introduced, exercises or case studies included, and connection to next chapter.

## Outline Document Header

**Every outline MUST start with this header:**

```markdown
# [Title] Story Outline

> **For agentic drafters:** REQUIRED SUB-SKILL: Use novel-superpowers:subagent-driven-drafting (recommended) or novel-superpowers:drafting-scenes to draft this outline scene-by-scene. Scenes use checkbox (`- [ ]`) syntax for tracking.

**Premise:** [One sentence describing the story]

**Structure:** [Act structure and POV approach]

**Total Scope:** [Chapter count, estimated word count per chapter, total target word count]

---
```

## Chapter and Scene Structure

```markdown
## Chapter N: [Chapter Title]

**Act Position:** [Act 1 / Act 2A / Midpoint / Act 2B / Act 3]
**POV:** [Character name or "Omniscient"]
**Word Count Target:** [e.g., 3,000–4,000 words]
**Emotional Register:** [e.g., tension building, revelation, grief, dark humor]

### Scene N.1: [Scene Name]

**Location:** [Where and when]
**Characters:** [Who is present]
**Scene Goal:** [What does the POV character want?]
**Scene Conflict:** [What opposes them?]
**Outcome:** [Yes-and / Yes-but / No-and / No-but]
**Key Reveals:** [Story information surfaced in this scene]
**Continuity Flags:** [Facts established here that must be honored later]
**Emotional Beat:** [What should the reader feel?]
**Transition:** [How this connects to the next scene]

- [ ] **Draft Scene N.1**

  Write this scene. Opening line should [specific guidance]. The scene must establish [specific fact]. Close by [specific transition or image].

- [ ] **Verify continuity** — confirm [specific continuity check from Continuity Flags]
- [ ] **Commit draft**
```

## No Placeholders

Every scene entry must contain the actual guidance a drafter needs. These are **outline failures** — never write them:
- "TBD", "TODO", "figure out later", "work out in draft"
- "Scene goes here"
- "Similar to Scene N.1" (repeat the entry — the drafter may be reading scenes out of order)
- Vague emotional beats: "something emotional happens"
- Vague reveals: "learns something important"
- Scene goals without specific stakes: "character does something"

## Outline Self-Review

After writing the complete outline, review it against the story bible:

**1. Bible coverage:** Does every major story beat from the bible appear in a scene? List any gaps.

**2. Arc tracking:** Does each character's arc show measurable change from their first scene to their last? Mark scenes where no arc progress occurs.

**3. Placeholder scan:** Any of the "No Placeholders" failures above? Fix them.

**4. Continuity consistency:** Do Continuity Flags in early scenes match what later scenes assume? A character who loses their map in Scene 3 shouldn't have it in Scene 7.

**5. Pacing check:** Are there 3+ consecutive scenes with the same emotional register? Flag them — pacing requires variation.

Fix issues inline. No need to re-review — just fix and move on.

## Drafting Handoff

After saving the outline, offer the author a choice:

**"Outline complete and saved to `docs/novel-superpowers/outlines/<filename>.md`. Two drafting options:**

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per chapter or scene cluster, with continuity review and prose quality review between each. Faster iteration, higher consistency.

**2. Inline Drafting** — Write scenes in this session using drafting-scenes, with checkpoint reviews.

**Which approach?"**

**If Subagent-Driven chosen:**
- **REQUIRED SUB-SKILL:** Use novel-superpowers:subagent-driven-drafting
- Fresh subagent per chapter/scene + two-stage review

**If Inline Drafting chosen:**
- **REQUIRED SUB-SKILL:** Use novel-superpowers:drafting-scenes
- Sequential drafting with continuity checkpoints

## Nonfiction Adaptation

For biography, memoir, self-help, workbook, textbook, or technical manual:

**Replace scene structure with chapter structure:**
- Chapter goal (what the reader learns or experiences)
- Key concepts or events covered
- Exercises, case studies, or examples included
- Prerequisites (what the reader must know from prior chapters)
- Continuity flags (terms, frameworks, or facts introduced here)
- Chapter summary/takeaway
- Bridge to next chapter

The same "no placeholders" and self-review standards apply.

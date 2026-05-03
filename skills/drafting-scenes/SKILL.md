---
name: drafting-scenes
description: Use when you have a written story outline to execute in a session, drafting chapter by chapter with continuity checkpoints
---

# Drafting Scenes

## Overview

Load outline, review critically, draft all scenes in sequence, verify continuity before each completion claim.

**Announce at start:** "I'm using the drafting-scenes skill to write this manuscript."

**Note:** Novel Superpowers works much better with access to subagents. The quality and consistency of the draft will be significantly higher if run on a platform with subagent support (such as Claude Code). If subagents are available, use `novel-superpowers:subagent-driven-drafting` instead of this skill.

## The Process

### Step 1: Load and Review Outline

1. Read the outline file
2. Read the story bible (if present)
3. Review critically — identify any gaps, contradictions, or questions before starting
4. If concerns: raise them with the author before beginning
5. If no concerns: create TodoWrite (one item per scene or chapter cluster) and proceed

### Step 2: Draft Each Scene

For each scene or chapter:

1. Mark as in_progress
2. Read the scene entry completely — understand goal, conflict, outcome, continuity flags, emotional beat
3. Draft the scene according to the outline specifications
4. Run the **Continuity Gate** (see below) before marking complete
5. Mark as completed

**Draft quality targets:**
- Scene goal met or meaningfully failed (outcomes matter)
- POV maintained consistently throughout
- All Continuity Flags honored
- Emotional beat lands — reader should feel what the entry specified
- Transition into the next scene set up

### Step 3: Continuity Gate

**Before marking any scene complete, verify:**

```
1. IDENTIFY: What continuity facts were established in this scene?
2. CHECK: Do any facts contradict what earlier scenes established?
3. VERIFY: Do scenes ahead in the outline assume anything this scene now changes?
4. CONFIRM: Are all character names, locations, and timeline positions consistent?
```

If continuity fails: fix the scene. Do not mark complete with known continuity errors.

**REQUIRED SUB-SKILL:** Use `novel-superpowers:continuity-verification` for the full continuity verification process.

### Step 4: Complete the Manuscript

After all scenes drafted and verified:
- Announce: "I'm using the finishing-a-manuscript skill to complete this work."
- **REQUIRED SUB-SKILL:** Use `novel-superpowers:finishing-a-manuscript`
- Follow that skill to verify the draft, present options, and execute the author's choice

## When to Stop and Ask for Help

**STOP drafting immediately when:**
- A continuity conflict cannot be resolved without changing the outline
- A character's motivation doesn't support their outlined action
- The outline has a critical gap preventing a scene from being written
- The story bible and outline contradict each other in a way that can't be fixed locally
- A scene calls for research or world detail not yet established

**Ask the author for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to outline review when:**
- Author updates the outline based on your feedback
- A scene mid-draft reveals a structural problem
- A character's arc doesn't track across scenes as written

**Don't force through story problems** — stop and ask.

## Draft Voice and Style

- Write in the narrative voice established in the story bible and opening chapters
- Don't introduce new character traits, relationships, or world facts not established in the bible or outline — flag them instead
- Show, don't tell, for emotional beats — trust the scene structure to carry the meaning
- Maintain consistent tense and POV unless the outline specifies a shift

## Remember

- Review outline and bible before drafting
- Follow scene entries exactly — the outline is the contract
- Run the Continuity Gate before marking each scene done
- Stop when stuck, don't invent solutions that contradict established story facts
- Never claim a scene is complete without running verification

## Integration

**Required workflow skills:**
- **novel-superpowers:story-outlining** — Creates the outline this skill executes
- **novel-superpowers:continuity-verification** — Full continuity check process
- **novel-superpowers:finishing-a-manuscript** — Completes manuscript after all scenes drafted

**Alternative workflow:**
- **novel-superpowers:subagent-driven-drafting** — Use for higher-quality parallel drafting with review gates between chapters

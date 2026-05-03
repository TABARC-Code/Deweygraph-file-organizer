---
name: receiving-manuscript-feedback
description: Use when processing feedback on a manuscript, chapter, or scene from an editor, beta reader, or reviewer agent — guides triage, prioritization, and revision without losing the author's voice or original vision
---

# Receiving Manuscript Feedback

## Overview

Feedback is data. Not every piece of feedback is correct. Not every piece of feedback is wrong. The author's job is to triage it, understand what it's pointing at, and decide what to do.

**Core principle:** Understand what the feedback is responding to before deciding whether to act on it.

**The author is always in control.** Feedback informs decisions; it doesn't make them.

## The Process

### Step 1: Receive Without Reacting

Read all feedback before doing anything else. Do not:
- Immediately agree with every note
- Immediately dismiss every note
- Start revising during the first read

Your goal in the first pass is only to understand what the reviewer experienced. Not whether they were right.

### Step 2: Triage

Sort feedback into three buckets:

**Signal:** Feedback that points at a real problem in the manuscript — even if the reviewer's proposed solution is wrong.

**Noise:** Feedback that reflects the reviewer's personal preference rather than a story problem. Valid data about one reader's experience, but not necessarily something to change.

**Misread:** Feedback that indicates the reviewer misunderstood the story's intent. Before dismissing: is this misread possible for other readers? If yes, it's signal.

**Sorting framework:**

```
"Multiple reviewers noted the same problem"  → Almost certainly signal
"One reviewer didn't like this choice"        → May be noise; look for underlying reason
"Reviewer suggested a fix, not a problem"     → Ignore the fix; diagnose the problem they experienced
"Reviewer didn't understand the theme"        → Could be misread or could mean the theme isn't landing
```

### Step 3: Diagnose, Don't Prescribe

For each piece of signal: what is the underlying story problem?

**Important:** Reviewers identify symptoms; the author diagnoses causes.

- "This chapter felt slow" → What scene function is not being served? Is the scene-sequel ratio off?
- "I didn't understand why she did that" → Is the motivation unclear, or is it clear and the reviewer missed it?
- "The villain doesn't feel threatening" → Has the villain been shown winning? Is the consequence of failure concrete?
- "I didn't care about the protagonist" → Is their want legible? Is their wound visible?

Diagnose before revising.

### Step 4: Prioritize Revisions

**High priority:**
- Structural issues (problems with acts, character arcs, central conflict)
- Character motivation that doesn't track
- Continuity errors
- Moments where a significant percentage of reviewers were confused or lost

**Medium priority:**
- Scene-level pacing and effectiveness
- Dialogue naturalness
- POV consistency

**Low priority (save for later revision pass):**
- Line-level prose notes (unless they point to voice drift)
- Personal preference notes
- Notes on scenes that reviewers liked but the author knows are structurally weak

**Never revise out of guilt** — only revise when you understand what problem you're solving.

### Step 5: Revision Plan

Before touching any draft, write a brief revision plan:

```markdown
# Revision Plan — [Title], [Chapter/Draft version]

## Structural revisions
- [What is changing and why]

## Scene-level revisions
- [What scenes are being rewritten or restructured and why]

## Prose and voice revisions
- [What craft notes are being addressed and where]

## Feedback being deferred
- [Feedback received but not acted on in this pass, and why]

## Feedback being ignored
- [Feedback received and dismissed, and why]
```

Commit this plan before beginning revisions.

### Step 6: Revise

Work through the revision plan in priority order:

1. Structural revisions first — these may eliminate scene-level problems downstream
2. Scene-level revisions second
3. Prose revisions last

Run `novel-superpowers:continuity-verification` after any structural revision to ensure changes haven't introduced new continuity conflicts.

### Step 7: Flag Author's Vision

When a note conflicts with a deliberate authorial choice:

- Document the choice in the story bible: "Deliberate choice: Kael's motivation in Chapter 6 is intentionally ambiguous — readers are not meant to know whether he acted from loyalty or self-preservation until Chapter 14."
- This protects the choice from future revision passes that might accidentally resolve the ambiguity
- If multiple reviewers hit the same ambiguity, consider whether it's intentional complexity or insufficient setup

## What Not to Do

**Never:**
- Rewrite a scene immediately after receiving feedback without diagnosing the problem
- Give in to all feedback to please the reviewer
- Dismiss feedback because it was delivered harshly
- Revise toward the reviewer's taste rather than the story's needs
- Lose the author's voice trying to satisfy every note

**Reviewer's job:** Report their experience.
**Author's job:** Decide what to do about it.

## Receiving Feedback from Subagent Reviewers

When a continuity reviewer or prose quality reviewer subagent (from subagent-driven-drafting) returns notes:

1. Read all notes before acting
2. Continuity issues: fix before moving to next chapter — non-negotiable
3. Prose quality issues: triage using the framework above
4. Document any deferred notes in the continuity log or revision plan

Continuity errors from subagent review are signal. Fix them.
Prose notes from subagent review may be noise — use your judgment.

---
name: requesting-manuscript-feedback
description: Use when requesting editorial or reader feedback on a manuscript, chapter, or scene — structures the feedback request to produce useful, actionable notes rather than vague praise or undirected criticism
---

# Requesting Manuscript Feedback

## Overview

Vague feedback wastes everyone's time. "I liked it" and "it felt slow" are not actionable. Structured feedback requests produce editorial notes you can actually use.

**Core principle:** Ask for the feedback you need, not the feedback that will make you feel good.

## When to Use

- Sending a draft to a beta reader, editor, or reviewer agent
- Requesting feedback from a reviewer subagent in subagent-driven-drafting
- Preparing a manuscript for editorial review
- Asking for focused feedback on a specific craft problem

## The Feedback Request Template

Every feedback request must include:

```markdown
# Manuscript Feedback Request — [Title], [Chapter/Section]

## What you're reading
[Brief summary of what the reader is about to read: the story's premise, where this chapter falls in the narrative, and what has happened so far in the story. 3-5 sentences max.]

## The draft's known issues
[What do you already know isn't working? Listing known issues prevents the reviewer from spending time telling you things you already know. Be honest.]

## What I need feedback on
[Specific questions the reviewer should answer. Choose 2-4. Examples below.]

## Please do NOT focus on
[Anything you're deliberately setting aside for later revision — line edits on a structural draft, for instance.]
```

## Feedback Question Bank

Choose 2-4 questions matched to the draft's stage and known needs:

**Story level:**
- Does the central conflict feel clear and urgent?
- Is the protagonist's want legible? Did you understand why they're doing what they're doing?
- Where did your attention wander or break?
- Which character felt most real? Which felt least real, and why?
- Did the ending feel earned?
- Were there any moments where you lost the thread of the story?

**Scene level:**
- What is the emotional payoff of this scene? Did it land?
- Where did the pacing feel too slow or too fast?
- Did the dialogue feel natural and character-specific?
- Was there any moment where you felt the author was working too hard to make something happen?

**World and continuity level:**
- Were there any moments where the world felt inconsistent or unclear?
- Were there any facts established in this chapter that you believe contradict earlier chapters?
- Did the setting feel inhabited or described-from-outside?

**Voice and prose level:**
- Was the voice consistent throughout?
- Were there any sentences you had to re-read to understand?
- Were there any sections where the prose felt overwritten or underwritten?

**Nonfiction level:**
- Was the central argument or framework clear?
- Were there any concepts that felt underdeveloped or assumed?
- Did the examples make the abstract principles concrete?
- Was there anything you wanted to know that the chapter didn't address?

## Feedback Types

Match your request to what you actually need:

| Stage | Request type |
|-------|-------------|
| Early draft | Big-picture structural feedback only — "don't line-edit this" |
| Mid-draft | Scene-level effectiveness and character coherence |
| Late draft | Prose quality, dialogue, pacing |
| Near-final | Line editing, continuity check, consistency review |

## Dispatching a Reviewer Subagent

When using a subagent as a reviewer (in subagent-driven-drafting or after a chapter):

Provide the subagent with:
1. The full feedback request template (filled in)
2. The chapter text
3. The continuity log up to this chapter
4. The story bible (summary form)
5. Clear instructions: provide structured feedback using the questions above; do NOT rewrite the prose

Reviewer subagents should return:
- Answers to each specific question
- A list of specific continuity conflicts (if any)
- A list of specific moments where they were confused or lost
- No unsolicited rewrites

## What Good Feedback Looks Like

**Useful:**
- "I lost track of the protagonist's goal in the second half of this chapter. Her motivation in Scene 2 seems to contradict what she said in Scene 1."
- "The dialogue in the tavern scene feels expository — both characters seem to be explaining the world to each other rather than having a conversation."
- "Page 7, the word 'lambent' stopped me. It felt like it came from a different register than the rest of the chapter."

**Not useful:**
- "It was good."
- "I liked the character."
- "The writing felt slow in places."

Ask for useful. Ask for specific. If a reviewer gives you unuseful feedback, follow up: "Can you point to the specific moment where the pacing felt slow?"

## Acting on Feedback

**REQUIRED SUB-SKILL:** Use `novel-superpowers:receiving-manuscript-feedback` when you receive feedback and need to process and integrate it.

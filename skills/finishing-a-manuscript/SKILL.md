---
name: finishing-a-manuscript
description: Use when all scenes or chapters are drafted and verified, and the manuscript needs to be compiled, reviewed for completeness, and prepared for its next stage
---

# Finishing a Manuscript

## Overview

Guide completion of a drafted manuscript by presenting clear options and handling the chosen workflow.

**Core principle:** Verify completeness → Present options → Execute choice → Archive or deliver.

**Announce at start:** "I'm using the finishing-a-manuscript skill to complete this work."

## The Process

### Step 1: Verify Completeness

**Before presenting options, verify the draft is complete:**

- All scenes/chapters in the outline are marked complete
- No outstanding continuity flags are unresolved
- No scenes are marked as drafts-in-progress or placeholders
- Word count is within range of the target (if specified in the outline)

**If incomplete:**
```
Draft incomplete. The following remain unfinished before this manuscript can move forward:

[List incomplete scenes or chapters]
[List unresolved continuity flags]

Cannot proceed with delivery or submission until these are resolved.
```

Stop. Don't proceed to Step 2.

**If complete:** Continue to Step 2.

### Step 2: Run Final Continuity Pass

Before presenting options, run a final end-to-end continuity check across the complete manuscript:

- Character states at end of story match their arc as defined in the bible
- No dangling plot threads from the outline were dropped without resolution
- World rules were applied consistently throughout
- Timeline is internally consistent

Report results. Fix critical issues before proceeding.

**REQUIRED SUB-SKILL:** Use `novel-superpowers:continuity-verification` for the full verification process.

### Step 3: Present Options

Present exactly these 4 options:

```
Manuscript complete. What would you like to do?

1. Compile and export — assemble all chapters into a single document
2. Prepare for submission — format for editorial or publishing workflow
3. Keep as-is — I'll handle the next steps manually
4. Archive this draft — save as a versioned draft and start a new revision

Which option?
```

**Don't add explanation** — keep options concise.

### Step 4: Execute Choice

#### Option 1: Compile and Export

Assemble all chapter files into a single manuscript document:

```
[Title]
by [Author]

---

Chapter 1: [Title]
[Content]

---

Chapter 2: [Title]
[Content]

...
```

Save to: `manuscripts/[title]-draft-[version]-[YYYY-MM-DD].md` (or .docx if requested)

#### Option 2: Prepare for Submission

Format the manuscript according to standard submission guidelines:

- Standard manuscript format: double-spaced, 12pt font note, 1-inch margins note, running header with author name / title / page number
- Title page: title, author name, contact information, word count
- Chapter breaks formatted consistently
- Any submission-specific requirements noted by the author

Save to: `submissions/[title]-submission-[YYYY-MM-DD].md`

#### Option 3: Keep As-Is

Report: "Keeping draft files as-is. All chapter files remain in `drafts/[title]/`."

#### Option 4: Archive Draft

Save the current draft as a versioned archive:

```
archives/[title]/
  draft-v[N]-[YYYY-MM-DD]/
    [all chapter files]
    story-bible.md
    outline.md
    continuity-log.md
```

Then: confirm with author what the next revision cycle targets (new draft, revisions, structural changes).

### Step 5: Post-Completion Notes

After executing the author's choice, provide a brief completion summary:

```
Manuscript [title] — Draft Complete

Word count: [total]
Chapters: [N]
Story bible: [path]
Outline: [path]
Draft location: [path]

Next steps (optional):
- [ ] Editorial review
- [ ] Beta readers
- [ ] Query letter / synopsis
- [ ] Second draft revision pass
```

## Quick Reference

| Option | Compile | Format | Archive | Keep Files |
|--------|---------|--------|---------|------------|
| 1. Compile & Export | ✓ | - | - | ✓ |
| 2. Prepare for Submission | ✓ | ✓ | - | ✓ |
| 3. Keep As-Is | - | - | - | ✓ |
| 4. Archive Draft | - | - | ✓ | ✓ |

## Common Mistakes

**Skipping completeness verification**
- **Problem:** Incomplete draft delivered as finished
- **Fix:** Always verify all scenes/chapters marked complete before offering options

**Skipping final continuity pass**
- **Problem:** Unresolved contradictions shipped in final manuscript
- **Fix:** Always run continuity pass before options are presented

**Open-ended questions**
- **Problem:** "What should I do next?" → ambiguous
- **Fix:** Present exactly 4 structured options

## Red Flags

**Never:**
- Deliver a manuscript with unresolved continuity issues
- Skip the completeness check
- Offer options before verifying the draft is actually done

**Always:**
- Verify completeness before presenting options
- Run final continuity pass
- Present exactly 4 options

## Integration

**Called by:**
- **subagent-driven-drafting** — After all chapters complete and reviewed
- **drafting-scenes** — After all scenes drafted and verified

**Pairs with:**
- **continuity-verification** — Final manuscript-level continuity check
- **managing-writing-projects** — For archiving and version control

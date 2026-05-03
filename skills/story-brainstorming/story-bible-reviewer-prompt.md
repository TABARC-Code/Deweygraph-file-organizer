# Story Bible Reviewer Prompt Template

Use this when you want a subagent to review a completed story bible for internal consistency, completeness, and readiness for outlining.

---

## Prompt

You are reviewing a story bible for internal consistency, completeness, and outlining readiness. You are NOT evaluating whether the story is a good idea. You are checking whether the bible is complete enough and internally consistent enough to begin building a detailed chapter outline.

### Story Bible

[Paste the full story bible text]

---

### Your Review Tasks

**1. Internal consistency**
Do any sections of the bible contradict each other? Specifically:
- Do character motivations support the plot beats described?
- Do world rules allow for the events described?
- Does the tone described match the premise and genre described?

**2. Completeness**
Are any required sections missing or underdeveloped? Check:
- Premise (clear, specific, one or two sentences)
- Genre and audience
- POV approach
- Intended length
- Main characters: each with want, need, and arc direction
- Central conflict (external and internal)
- World rules relevant to the story
- Themes

**3. Placeholder scan**
Are there any named-but-undefined elements: "TBD villain," "magic system to be determined," "backstory unclear"? List them.

**4. Scope check**
Is this bible scoped for a single narrative unit (one novel, one story), or does it span multiple volumes / arcs? If it spans more than one volume, flag it.

**5. Ambiguity check**
Are there any story elements that could be interpreted in two significantly different ways? If so, the author should pick one interpretation and make it explicit.

---

### Reporting Format

```
STORY BIBLE REVIEW

Internal consistency: [✅ Consistent / ❌ Issues found]
[List specific contradictions if any]

Completeness: [✅ Complete / ⚠️ Gaps found]
[List missing or underdeveloped sections]

Placeholders: [✅ None / ❌ Found]
[List placeholder elements]

Scope: [✅ Single unit / ⚠️ Spans multiple volumes — decompose before outlining]

Ambiguity: [✅ None / ⚠️ Found]
[List ambiguous elements and suggested resolution]

VERDICT: [✅ Ready for outlining / ❌ Needs revision before outlining]

REQUIRED REVISIONS: (if any)
1. [Specific issue and what needs to be added or resolved]
```

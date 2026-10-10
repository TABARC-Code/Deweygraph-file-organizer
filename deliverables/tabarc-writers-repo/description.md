# TABARC Writers — What This Actually Is

*A description of the plugin, written honestly.*

---

Writing tools have a problem. They are almost always built by people who are not writers, for people who are, and the gap shows in every interaction. The menus are in the wrong place. The terminology is borrowed from somewhere else. The features that would help — the ones a working author actually needs on a Tuesday afternoon when a chapter isn't landing — are buried three levels deep or absent entirely.

TABARC Writers starts from a different position. It was built for the writing workflow as it actually exists: non-linear, stage-dependent, emotionally variable, and prone to derailing at exactly the moment when forward momentum matters most.

---

## The Core Idea

Most writing assistants give you a blank prompt and wait.

TABARC Writers gives you a system. Thirty-seven skills, each one covering a specific phase of the writing process in depth, all of them wired together so that the output of one feeds cleanly into the input of the next. The skills don't sit in a list — they form a network. Bidirectional. Verified. When a skill routes you somewhere, the destination knows you're coming.

The entry point is a single skill called `novel-writing-hub`. It reads your situation and dispatches you. You don't need to know what the other skills are called. You describe what you're working on — "I need to make this scene scarier", "the dialogue feels flat", "help me structure the second act" — and the hub works out the rest.

It is not magic. It is routing logic applied thoughtfully. The difference is meaningful.

---

## What It Does to Your Session

The plugin injects itself quietly into every conversation. Before you type a word, your current project context is already in the system prompt. Your active stage. Your prose directives. The things you've told it matter.

The prose directives are worth dwelling on. They fire automatically, every turn, whether you remember to ask for them or not. No em dashes used as stylistic connectors — a genuine stylistic bad habit that has infected AI-generated prose to the point of becoming a tell. No ellipsis spam. Strong verbs over weak ones propped up by adverbs. Sentence variety, because monotone rhythm is the fastest way to make technically correct prose feel dead on the page.

These aren't suggestions the model is politely considering. They're injected into the system prompt via `prompt.compose` on every single request. The prose directives are load-bearing.

---

## The Seven Stages

Fiction writing is not one activity. It is seven, at minimum, and each one requires a different kind of thinking.

Brainstorming is generative and loose. Outlining is structural and constraining. Drafting is forward momentum at the expense of quality. Prose polish is the opposite: slow, obsessive, sentence-level. Editorial review requires genuine detachment. Continuity verification is almost mechanical — facts, timelines, names. Finishing is something else entirely: the discipline to stop improving and ship.

The system maps to each of these stages and routes to the appropriate specialist skill. When you switch stages — when you move from drafting into editorial, or when the chapter you thought was done turns out to have a continuity problem — the status line updates and the context shifts. It doesn't ask you to explicitly announce the transition. It reads what you're saying and adjusts.

This is not clever. It is simply necessary, and most systems don't do it.

---

## The Humaniser

The humaniser skill deserves its own mention because it represents something the broader system is oriented around.

AI writing has patterns. Structural, lexical, rhythmic patterns that trained readers — and increasingly untrained ones — have learned to recognise. The em dash thing. The rule of three applied to everything. The positive negative negative structure. The specific vocabulary: "delve", "tapestry", "testament", "crucial". The opening gambit of acknowledging the question before actually answering it.

The humaniser skill applies a comprehensive detection pass against these patterns and rewrites accordingly. It doesn't soften them or reduce their frequency. It removes them and replaces them with something that sounds like a person actually wrote it.

It runs well with the prose-craft and human-prose-style skills when you want to go deeper. The three of them together constitute a serious prose audit pass.

---

## On the Bidirectionality

There is a version of "interconnected skills" that is purely cosmetic. You put arrows between boxes in a diagram and call it a system. The arrows don't actually do anything.

This is not that.

Every skill in the network has a cross-reference table. Structured columns: what it receives, from whom, when. What it sends, to whom, under what circumstances. The system was verified at zero missing back-links across all thirty-seven skills — meaning if skill A claims to route to skill B, skill B has been updated to acknowledge it. The context actually passes between them.

Whether this matters to you depends on how you use the system. If you stay in one skill for a whole session it doesn't. If you follow the routing — if you start in brainstorming, move to outlining, move to drafting, and use the editorial skills at the end — you'll notice that the skills know about each other. They refer to each other correctly. The handoffs are clean.

---

## Who This Is For

Authors who are serious about using AI assistance as a professional tool rather than a novelty. People who have already discovered that raw prompting produces raw results, and who want a more considered approach.

It is not for people who want a completely automated writing experience. TABARC Writers is a system that augments a human writer. It handles the routing, the context, the skill selection, and the prose discipline. The writing is still yours.

That is, incidentally, the only version worth doing.

---

## What It Is Not

TABARC Writers will not write your novel for you.

It will not make a bad story idea into a good one. It will not replace the judgement developed over years of reading and writing carefully. It will not do the structural thinking that good plotting requires, or the emotional intelligence that good character work demands.

What it will do is get out of the way of those things. It handles the friction. The skill selection. The prompt engineering. The context management. The prose directives that you would otherwise have to include manually every single time and would inevitably forget half of.

The boring operational parts of writing with an AI assistant. Done properly, they matter more than most people expect.

---

## A Note on the Prose Directives

The em dash prohibition is in there because em dashes have become the single most reliable marker of AI-generated prose. Not because the dash itself is wrong — it is a perfectly fine piece of punctuation with legitimate uses — but because language models have been trained on text that uses it as a stylistic connector in a specific, overreaching way that human writers largely do not.

The ellipsis rule is in there for the same reason. Restraint. Two per scene maximum.

The vocabulary bans exist because certain words — "delve" being the canonical example — have become so strongly associated with AI output that their presence immediately colours how a reader perceives everything around them.

None of this is about making AI writing undetectable. It is about making the writing better by removing the habits that make it worse. Those happen to be largely the same thing.

---

*TABARC-Code. Version 1.0.0.*

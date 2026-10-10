# TABARC Writers

**Professional novel-writing plugin for Claude Code.**

Thirty-seven skills. One entry point. Zero guessing about which skill to invoke.

---

## What This Is

TABARC Writers is a Claude Code plugin that turns your writing sessions into something resembling a coherent workflow rather than a series of increasingly desperate prompts. It ships with 37 interconnected writing skills — covering brainstorming, outlining, drafting, prose polish, editorial review, continuity checking, and manuscript finishing — wired together in a bidirectional cross-reference network so that when one skill hands off to another, the context actually travels with it.

There is a unified entry point called `novel-writing-hub`. It reads what you are working on, identifies your current stage, and routes you to the right skill. You do not need to know the skill names. You do not need to remember the routing table. You describe what you are doing, and the system works out the rest.

It also injects prose directives into every session automatically. No em dashes. No ellipsis spam. Strong verbs. Sentence variety. These fire whether you remember to ask for them or not, which is rather the point.

---

## Installation

Extract into your Claude Code plugins folder:

```bash
tar -xzf tabarc-writers-plugin.tar.gz -C ~/.claude/plugins/
```

Restart Claude Code. The plugin loads automatically on session start.

Alternatively, if you are developing or want hot reloading, place the `tabarc-writers/` folder under `~/.claude/dev-mods/` and enable hot reloading when prompted.

---

## What Happens When It Loads

On session start, the plugin registers five slash commands, opens a writing dashboard pane, and sets the status line to `TABARC Writers ready`. It injects your current project context and prose directives into the system prompt on every turn — silently, without being asked.

The band above the prompt shows your active project name and current workflow stage. When you type a message, the plugin reads it for stage-detection keywords and silently updates the status line if your intent has changed.

It is, in short, quietly present without making itself the centre of attention. Which is more than can be said for most writing tools.

---

## Slash Commands

| Command | What it does |
|---|---|
| `/hub` | Opens the TABARC-Code novel-writing hub entry point |
| `/brainstorm` | Sets stage to Ideation, routes to `story-brainstorming` |
| `/draft` | Sets stage to Drafting, routes to `drafting-scenes` |
| `/outline` | Sets stage to Outlining, routes to `story-outlining` |
| `/writers` | Opens the project dashboard pane |

---

## Workflow Stages

The system recognises seven stages and routes to the correct skill for each.

| Stage | Skill | Trigger keywords |
|---|---|---|
| 💡 Ideation | `story-brainstorming` | "I have an idea", "help me brainstorm" |
| 📐 Outlining | `story-outlining` | "outline", "structure", "plot", "chapter list" |
| ✍️ Drafting | `drafting-scenes` | "write the next scene", "draft this chapter" |
| ✨ Prose | `humanizer` | "polish", "too formal", "sounds robotic" |
| 🔍 Editorial | `requesting-manuscript-feedback` | "review", "feedback", "critique" |
| 🔗 Continuity | `continuity-verification` | "contradiction", "timeline", "consistency" |
| 🏁 Finishing | `finishing-a-manuscript` | "final pass", "done drafting", "ready to submit" |

The stage detection is keyword-based and runs silently. No confirmation dialog, no friction. It simply updates and moves on.

---

## Always-Active Prose Directives

These fire on every session, every turn, automatically:

- **No em dashes** as stylistic connectors. If you catch yourself reaching for one, restructure the sentence instead.
- **Ellipsis maximum: two per scene.** For genuine trailing off or interrupted thought only.
- **Contractions are natural** in dialogue and informal prose. Avoid stiff formality.
- **Strong precise verbs** over weak verb + adverb. "He sprinted" beats "He ran quickly".
- **Sentence variety.** Short punchy statements mixed with longer flowing ones. Monotone rhythm is prose death.

These are not suggestions. They are directives injected into the system prompt on every turn via the `prompt.compose` hook.

---

## The 37 Skills

### Entry Point
`novel-writing-hub` — unified router combining session bootstrap and craft dispatch intelligence

### Core Workflow
`story-brainstorming` · `story-outlining` · `plot-architecture` · `outline-driven-writing` · `drafting-scenes` · `scene-construction-engine` · `subagent-driven-drafting` · `finishing-a-draft-branch` · `finishing-a-manuscript`

### Character & Psychology
`character-development` · `character-depth-engine` · `character-psychology-engine`

### Prose & Voice
`prose-craft` · `human-prose-style` · `humanizer` · `pov-and-voice-engine`

### Tension & Emotion
`hook-and-tension-system` · `fear-and-emotion-system`

### Genre Specialists
`genre-craft` · `horror-craft-module` · `mystery-crime-module` · `military-gothic-voice` · `western-fiction-master` · `historical-fiction-master`

### World & Setting
`world-building` · `worldbuilding-naming-engine`

### Editorial
`requesting-manuscript-feedback` · `requesting-editorial-review` · `receiving-manuscript-feedback` · `receiving-editorial-feedback` · `systematic-scene-diagnosis` · `continuity-verification`

### Craft Reference
`author-craft-compass` · `using-novel-superpowers`

### Project Management
`managing-writing-projects` · `managing-draft-branches`

---

## Bidirectional Cross-Reference Network

Every skill in this system has a structured cross-reference network. If Skill A routes to Skill B, Skill B has a back-link to A. No orphan skills. No dead ends. The network has been verified at zero missing back-links across all 37 skills.

This matters because most skill collections are a flat list of prompts dressed up as a system. This one actually routes, returns, and passes context in both directions.

---

## Plugin Architecture

```
tabarc-writers/
├── .claude-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json
│   └── register.tsx     ← The hooks module
└── types/
    └── index.d.ts       ← WritingProject state contract
```

The hooks module registers on: `session.start`, `prompt.compose`, `prompt.submit`, `command.run` (×5), `ui.render{AbovePrompt}`, `ui.render{Pane}`.

State is held in `$.state` under the `tabarc-writers.project` key: `{ title, genre, stage, branch }`. It persists across hot reloads.

---

## The Skills Archive

The full 37-skill set is also available as individual `.skill` files for the Claude cloud skill registry, and as `TABARC-Code.tar.gz` — the complete plugin package including all skill SKILL.md files, slash commands, and the `SessionStart` hook.

Both are in `deliverables/` in the [Deweygraph-file-organizer](https://github.com/TABARC-Code/Deweygraph-file-organizer) repository.

---

## Requirements

- Claude Code CLI or desktop app
- Skills in `~/.claude/plugins/TABARC-Code/` (the 37-skill set) for full routing functionality

---

## Licence

MIT

---

*Built by TABARC-Code. Because writing is hard enough without the tooling getting in the way.*

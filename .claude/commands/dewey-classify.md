# /dewey-classify

Classify a file using the DeweyGraph modular skill toolkit.

Claude Haiku (`claude-haiku-4-5`) acts as the "queen ant" — it picks which skills (a–f) and which discrete functions within each skill to invoke for this specific file. Not every skill is used every time; partial invocation is the norm.

Skills available:
- **a** typology — filing context (intake / project / archive / reference / export / dump / mixed)
- **b** filter — archival worthiness gate
- **c** role — material role (source / process / reference / output / residue / duplicate-candidate)
- **d** classify — Dewey anchor + secondary domains + lens tags
- **e** link — typed bilateral relations, heat values 1–10
- **f** note — Obsidian-ready YAML frontmatter + body

The skill path taken is recorded (e.g. `a.context_assess → d.anchor → e.class_link`) and heat accumulates on each transition — building a pheromone map of how this archive reasons.

Every class link is bilateral: A→B automatically writes the typed reverse B→A.

## Usage

```
/dewey-classify <file_path>
```

## What to do

Run the following shell command, substituting `$ARGUMENTS` for the file path the user provided:

```bash
python classify.py $ARGUMENTS
```

If `$ARGUMENTS` is empty, ask the user which file they want to classify.

If the command fails because `anthropic` is not installed, tell the user to run:
```bash
pip install anthropic
```

If `ANTHROPIC_API_KEY` is missing, tell the user to set it:
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

## After the result is printed

1. Explain the **anchor code** in plain English (e.g. "006.3.AI is the Dewey class for Artificial Intelligence")
2. Note the **skill path** taken — which skills and functions Haiku chose for this file and why that path makes sense for this material
3. If heat bars are shown, briefly explain which Dewey classes are warming up across the archive

Heat scale: 1–3 cold · 4–6 warm · 7–9 hot · 10 burning

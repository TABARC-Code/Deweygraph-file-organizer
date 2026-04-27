# /dewey-classify

Classify a file using the DeweyGraph Dewey Decimal system.

Runs `classify.py` with Claude Haiku (`claude-haiku-4-5`) to assign:
- **Anchor code** — one Dewey class (e.g. `006.3.AI`, `700.STUDIO`)
- **Material role** — source / process / reference / output / residue / duplicate-candidate
- **Archival worthiness** — whether the file deserves a note at all
- **Decision note** — a plain-English explanation of the choice

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

After the result is printed, briefly explain what the anchor code means in plain English (e.g. "006.3.AI is the Dewey class for Artificial Intelligence") so the user understands the classification.

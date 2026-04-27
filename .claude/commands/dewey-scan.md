# /dewey-scan

Scan a folder with the DeweyGraph modular classifier and synthesise cross-links.

Each file is classified using Claude Haiku (`claude-haiku-4-5`) via a modular skill toolkit (a–f). After all files are classified, a second Haiku call synthesises file-to-file cross-links across the whole folder.

Heat accumulates on two levels:
- **class_heat** — pheromone weight per Dewey class, growing with each classification
- **path_heat** — pheromone weight per skill-transition (e.g. `a.context_assess→d.anchor`), revealing the archive's dominant reasoning patterns over time

Every relation is bilateral: A→B automatically writes the typed reverse B→A.

## Usage

```
/dewey-scan <folder_path>
```

## What to do

Run the following shell command, substituting `$ARGUMENTS` for the folder path the user provided:

```bash
python classify.py --scan $ARGUMENTS
```

If `$ARGUMENTS` is empty, ask the user which folder they want to scan.

If the command fails because `anthropic` is not installed, tell the user to run:
```bash
pip install anthropic
```

If `ANTHROPIC_API_KEY` is missing, tell the user to set it:
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

## After the scan

After results are printed:
1. Briefly summarise the folder's dominant Dewey classes (the hottest class_heat entries)
2. Note the most-used skill path (hottest path_heat transitions) — this reveals how the archive's material tends to be reasoned about
3. Mention any cross-links the synthesis step found between files

Use plain English. The user should understand what the archive looks like as a whole, not just individual files.

# /dewey-graph

Show the DeweyGraph link graph and heat maps for the current archive.

Displays accumulated knowledge from all previous `/dewey-classify` and `/dewey-scan` runs. Two views are available:

- **graph** — all classified nodes with their anchor codes, material roles, and bilateral class links
- **heat** — pheromone heat bars showing which Dewey classes and skill-path transitions are hottest

## Usage

```
/dewey-graph          show the full link graph
/dewey-graph heat     show class heat + skill-path heat maps
```

## What to do

For `/dewey-graph` with no argument:
```bash
python classify.py --graph
```

For `/dewey-graph heat`:
```bash
python classify.py --heat
```

If `$ARGUMENTS` is `heat`, run the `--heat` command. Otherwise run `--graph`.

If the command fails because `anthropic` is not installed, tell the user to run:
```bash
pip install anthropic
```

If `dewey_graph.json` does not exist yet (no files classified), tell the user to first classify a file:
```
/dewey-classify <file_path>
```
or scan a folder:
```
/dewey-scan <folder_path>
```

## After the output

After displaying the graph or heat map:

- **Graph view**: Highlight the most connected nodes — files with many bilateral links are the archive's "knowledge hubs"
- **Heat view**: Explain what the hottest Dewey class represents in plain English (e.g. "006.3.AI is Artificial Intelligence — this archive skews heavily technical"). Also note the dominant skill-path transition, which reveals the typical reasoning pattern the queen ant takes when processing this archive's material.

Heat values use the pheromone scale:
- 1–3 — cold / tangential
- 4–6 — warm / meaningful
- 7–9 — hot / important
- 10 — burning / inseparable

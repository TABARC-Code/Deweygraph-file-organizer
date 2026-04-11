# Repo Map

This exists so you don’t have to guess what lives where.

## Root

- `README.md` → overview and entry point
- `.gitignore` → keeps noise out of the repo

---

## skill/

Core logic for Claude.

- `deweygraph-file-organizer.skill.md` → original version
- `deweygraph-file-organizer.strict.skill.md` → stricter, cleaner version

---

## prompts/

How you actually run the system.

- `full-pipeline.md` → everything
- `obsidian-ingest.md` → notes and graph
- `duplicate-audit.md` → clean-up and structure

---

## templates/

Reusable output structures.

- item note template
- folder index template
- decision register template

---

## docs/

Human-readable guidance.

- `getting-started.md` → step-by-step
- `idiots-guide.md` → short version
- `classification-manual.md` → rules
- `connected-repos.md` → ecosystem logic
- `repo-map.md` → this file

---

## examples/

Concrete outputs.

- sample graph map

---

## How it fits together

```text
folder → prompt → skill → output → Obsidian
```

If that loop breaks, something’s wrong.

---

## If you’re lost

Start here:

1. `docs/getting-started.md`
2. `prompts/full-pipeline.md`
3. one folder only

Then come back.

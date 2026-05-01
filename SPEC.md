# Project name

> One sentence. What does this do and who is it for?

---

## Problem

What problem does this solve? Why does it exist?
Write 2–4 sentences from the perspective of the person who would use it.
Avoid technical language here — focus on the pain, not the solution.

---

## Goals

What does success look like? List 3–5 concrete outcomes.

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Non-goals

What is this explicitly NOT trying to do?
This section prevents scope creep and keeps Claude Code focused.

- Not trying to...
- Not trying to...

---

## Users & context

Who uses this? How do they interact with it?
(CLI tool? Web app? Script someone runs once? API another system calls?)

---

## Inputs & outputs

**Inputs:**
| Input | Type | Example | Required? |
|-------|------|---------|-----------|
| | | | |

**Outputs:**
| Output | Format | Example |
|--------|--------|---------|
| | | |

---

## Core behavior

Walk through the happy path step by step.
Number each step. Be specific — this is what Claude Code will implement.

1. User does X
2. System does Y
3. Output is Z

### Edge cases & errors

What should happen when things go wrong?

- If input is missing → ...
- If API call fails → ...
- If file not found → ...

---

## Technical approach

**Language / runtime:** Python 3.12

**Key dependencies:**
| Library | Purpose | Why this one |
|---------|---------|-------------|
| | | |

**Architecture notes:**
How is the code structured? Class-based? Functional? Any design patterns worth noting?

---

## File structure

```
project-name/
├── main.py          # entry point
├── .env             # secrets (gitignored)
├── .env.example     # committed, shows required keys
├── requirements.txt
├── README.md
└── SPEC.md          # this file
```

---

## Environment variables

| Variable | Purpose | Where to get it |
|----------|---------|-----------------|
| | | |

---

## Out of scope / future ideas

Things you thought of but are deliberately leaving out for now.
Parking lot for v2 features.

- Could add...
- Could extend to...

---

## Definition of done

This project is complete when:

- [ ] Core behavior works end-to-end
- [ ] Edge cases handled with clear error messages
- [ ] README explains what it does and how to run it
- [ ] `.env.example` committed (never `.env`)
- [ ] Committed to GitHub with a clean commit history
- [ ] Business value is clear in the README intro

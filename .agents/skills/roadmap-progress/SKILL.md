---
name: roadmap-progress
description: Maintain the learner's persistent progress in IARoadmap. Use during teaching, study, quizzes, exercises, or any request where prior learning state changes what should happen next.
---

# Roadmap progress

Use this skill together with the teaching method. Its job is persistence, not pedagogy.

## Canonical state

Before teaching or evaluating, read:

- `Mi-progreso/Mi seguimiento.md`
- `Mi-progreso/Conocimientos.md`
- `Mi-progreso/README.md` when the update rules are needed

Treat those files as the source of truth for prior learning state.

## Loop

Follow this loop for substantive learning sessions:

```text
load state -> teach/practice -> observe evidence -> update concept state -> append next step
```

### 1. Load state

Read the current topic, last `Cómo sigo`, concept states, and their evidence. Reuse that information so the learner does not repeat already-proven work unnecessarily.

### 2. Teach or practice

Apply the active teaching skill, lesson, exercise, or quiz. Do not change progress merely because content was presented.

### 3. Observe evidence

Evidence must come from what the learner actually does: predicts an output, explains a concept, solves an exercise, identifies an error, creates a correct variant, or otherwise demonstrates understanding.

Do not infer evidence from statements such as `lo leí`, `ya lo vi`, `entiendo`, or from your own explanation alone.

### 4. Update concept state

The only valid states are:

- `pendiente`: not yet sufficiently checked.
- `en aprendizaje`: partial understanding, uncertainty, or relevant errors are visible.
- `demostrado`: a meaningful check was completed correctly without copying the solution.

Never promote a concept to `demostrado` from explanation alone.

For each changed concept, update the row in `Mi-progreso/Conocimientos.md` with:

- the new state;
- one short, concrete evidence sentence;
- the date in `YYYY-MM-DD`.

If new evidence contradicts an earlier `demostrado`, changing it back to `en aprendizaje` is allowed and preferred over preserving a stale status.

### 5. Append next step

After a substantive session, append one short entry to `Mi-progreso/Mi seguimiento.md`:

```markdown
### YYYY-MM-DD — Pi

- Hice: <what was actually worked on>
- Me costó: <main gap, or "nada en particular">
- Cómo sigo: <one small concrete next action>
```

Update `Estoy estudiando` only when the current topic materially changes.

## Boundaries

- Do not duplicate full quiz answers, explanations, or exercise solutions into the progress files.
- Do not overwrite the learner's answers in `08-Ejercicios/`.
- Do not edit `.pi/` to persist state.
- Keep evidence concise and factual.
- Do not store credentials, secrets, patient data, or unnecessary sensitive personal information.

## Git synchronization

Project-level `AGENTS.md` defines the Git synchronization policy. When the progress files change, follow it so GitHub remains the shared state used by Pi and ChatGPT.

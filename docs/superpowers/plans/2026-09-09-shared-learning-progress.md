# Shared Learning Progress Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the private `IARoadmap` repository the shared source of truth for learning progress used by Pi and ChatGPT.

**Architecture:** Keep the existing minimal session log, add one persistent concept-state file, and expose project instructions/skill metadata so Pi reads and updates the same files ChatGPT can edit through GitHub. Avoid modifying the Amos `.pi` package so upstream teaching behavior remains independent.

**Tech Stack:** Markdown, Git/GitHub, Pi project instructions (`AGENTS.md`), Pi project skills (`.agents/skills/`).

**Spec:** `docs/superpowers/specs/2026-09-09-shared-learning-progress-design.md`

## Global Constraints

- GitHub is the source of truth for `Mi-progreso/`.
- Do not store credentials, secrets, patient data, or unnecessary sensitive personal information.
- Do not add dependencies, services, databases, plugins, or generated state.
- Do not modify the teaching implementation under `.pi/`.
- A concept reaches `demostrado` only with observed evidence, never because material was merely presented or read.
- Initial JavaScript concepts are `pendiente`: variables, tipos, condicionales, bucles, funciones, arrays, objetos.

---

### Task 1: Version the progress directory

**Files:**
- Modify: `.gitignore`
- Create: `Mi-progreso/Mi seguimiento.md`
- Create: `Mi-progreso/Conocimientos.md`
- Create: `Mi-progreso/README.md`

**Interfaces:**
- Consumes: existing progress template conventions.
- Produces: canonical progress files readable by humans, Pi, and ChatGPT.

- [ ] **Step 1: Remove only the `Mi-progreso/` ignore rule**

Keep all other ignore rules unchanged.

- [ ] **Step 2: Create the canonical session log**

Use:

```markdown
# Mi seguimiento

## Ahora

Estoy estudiando: JavaScript — fundamentos

## Registro
```

Session entries append below `## Registro` using:

```markdown
### YYYY-MM-DD — Pi|ChatGPT|manual

- Hice:
- Me costó:
- Cómo sigo:
```

- [ ] **Step 3: Create the concept-state table**

Use columns `Área`, `Concepto`, `Estado`, `Evidencia`, `Última comprobación` and seed the seven JavaScript concepts as `pendiente`, with evidence `—` and date `—`.

- [ ] **Step 4: Create the progress contract README**

Document the three states exactly: `pendiente`, `en aprendizaje`, `demostrado`; require evidence before promotion; explain pull-before-Pi and push-after-Pi; explain that ChatGPT edits GitHub directly.

- [ ] **Step 5: Verify**

Run locally after pulling:

```bash
git check-ignore -v Mi-progreso/Conocimientos.md || true
git status --short
```

Expected: `Mi-progreso/Conocimientos.md` is not ignored, and the new files appear as tracked/untracked changes ready to commit.

- [ ] **Step 6: Commit**

```bash
git add .gitignore Mi-progreso/
git commit -m "feat: track shared learning progress"
```

### Task 2: Teach Pi how to use the shared state

**Files:**
- Create: `AGENTS.md`
- Create: `.agents/skills/roadmap-progress/SKILL.md`

**Interfaces:**
- Consumes: `Mi-progreso/Mi seguimiento.md`, `Mi-progreso/Conocimientos.md`.
- Produces: deterministic project-level instructions for Pi learning sessions.

- [ ] **Step 1: Create `AGENTS.md`**

Require Pi, for learning/teaching requests, to read the two canonical files first, reuse existing evidence, update only observed concepts, append a short session entry after substantive work, preserve exercise answers, and keep `.pi/` independent.

- [ ] **Step 2: Create the `roadmap-progress` skill**

Frontmatter:

```yaml
---
name: roadmap-progress
description: Maintain the learner's persistent progress in IARoadmap. Use during teaching, study, quizzes, exercises, or any request where prior learning state changes what should happen next.
---
```

The body must define this loop:

```text
load state -> teach/practice -> observe evidence -> update concept state -> append next step
```

It must explicitly forbid promoting a concept from explanation alone.

- [ ] **Step 3: Verify discoverability and references**

Run:

```bash
test -f AGENTS.md
test -f .agents/skills/roadmap-progress/SKILL.md
grep -n "Mi-progreso/Conocimientos.md" AGENTS.md .agents/skills/roadmap-progress/SKILL.md
```

Expected: both files exist and both reference the canonical concept-state file.

- [ ] **Step 4: Commit**

```bash
git add AGENTS.md .agents/skills/roadmap-progress/SKILL.md
git commit -m "feat: add shared progress instructions for Pi"
```

### Task 3: Align roadmap documentation

**Files:**
- Modify: `00-MOC/Estado actual.md`
- Modify: `05-Plantillas/Plantilla de progreso.md`

**Interfaces:**
- Consumes: shared-state contract from Task 1.
- Produces: user-facing docs that no longer claim progress is excluded from Git.

- [ ] **Step 1: Update `Estado actual.md`**

Replace the one-time setup that tells the learner to create an ignored local folder with instructions stating that `Mi-progreso/` is already the canonical versioned folder. Preserve the existing minimal two-minute workflow and privacy warning. Add the Pi sync rule:

```bash
git pull --rebase
# estudiar con Pi
git add Mi-progreso
git commit -m "progress: update learning state"
git push
```

Do not require a commit when nothing changed.

- [ ] **Step 2: Update the progress template**

Keep it minimal, but set the session-entry format to the canonical date/source structure and mention that concept-level evidence belongs in `Mi-progreso/Conocimientos.md` rather than duplicating it in the session log.

- [ ] **Step 3: Verify stale guidance is gone**

Run:

```bash
grep -Rni "Mi-progreso/.*exclu\|excluida de Git\|no respalda estas notas" 00-MOC 05-Plantillas || true
```

Expected: no active documentation says `Mi-progreso/` is excluded from Git.

- [ ] **Step 4: Commit**

```bash
git add "00-MOC/Estado actual.md" "05-Plantillas/Plantilla de progreso.md"
git commit -m "docs: document shared learning progress workflow"
```

### Task 4: End-to-end consistency check

**Files:**
- Read/verify all files changed in Tasks 1–3.

**Interfaces:**
- Consumes: completed shared-progress implementation.
- Produces: a verified workflow usable by both Pi and ChatGPT.

- [ ] **Step 1: Validate required files**

```bash
test -f "Mi-progreso/Mi seguimiento.md"
test -f "Mi-progreso/Conocimientos.md"
test -f "Mi-progreso/README.md"
test -f AGENTS.md
test -f .agents/skills/roadmap-progress/SKILL.md
```

- [ ] **Step 2: Validate JavaScript seed state**

```bash
for concept in variables tipos condicionales bucles funciones arrays objetos; do
  grep -i "$concept" "Mi-progreso/Conocimientos.md" >/dev/null || exit 1
done
```

Expected: all seven concepts are present and initially `pendiente`.

- [ ] **Step 3: Validate state vocabulary**

Inspect `Mi-progreso/README.md`, `Conocimientos.md`, `AGENTS.md`, and the skill. The only learning-state values used as statuses must be `pendiente`, `en aprendizaje`, and `demostrado`.

- [ ] **Step 4: Validate Git tracking behavior**

```bash
git check-ignore Mi-progreso/Conocimientos.md && exit 1 || true
git status --short
```

Expected: the progress file is not ignored.

- [ ] **Step 5: Final review**

Confirm no file instructs Pi to modify `.pi/`, no sensitive fields were introduced, and both Pi and ChatGPT are directed to the same two canonical state files.

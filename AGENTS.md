# Instrucciones del proyecto IARoadmap

Este repositorio es el roadmap personal de aprendizaje. GitHub es la fuente de verdad compartida entre la copia local, Pi y ChatGPT.

## Progreso persistente

Cuando la tarea sea estudiar, enseñar, practicar, hacer un quiz, resolver ejercicios o decidir qué aprender después:

1. Antes de enseñar, leé completos:
   - `Mi-progreso/Mi seguimiento.md`
   - `Mi-progreso/Conocimientos.md`
2. Usá la evidencia existente para continuar desde el nivel ya comprobado. No repitas diagnóstico que ya esté respaldado por evidencia salvo que haga falta comprobar retención o una contradicción nueva.
3. Durante la sesión, distinguí entre contenido explicado y aprendizaje demostrado.
4. Actualizá `Mi-progreso/Conocimientos.md` únicamente cuando aparezca evidencia observable en una respuesta, explicación, ejercicio o variante del usuario.
5. Nunca marques un concepto como `demostrado` solo porque fue explicado, leído o mostrado.
6. Después de una sesión sustantiva, agregá una entrada breve a `Mi-progreso/Mi seguimiento.md` con `Hice`, `Me costó` y `Cómo sigo`.
7. No sobrescribas las respuestas del usuario en `08-Ejercicios/` ni su código de práctica. El seguimiento resume; las respuestas y artefactos quedan donde corresponden.

Los únicos estados de concepto son:

- `pendiente`
- `en aprendizaje`
- `demostrado`

El contrato completo está en `Mi-progreso/README.md`.

## Repaso espaciado

El calendario de repaso lo lleva el plugin Obsidian Spaced Repetition, sobre `Repaso/`. No agregues columnas ni fechas de repaso a `Conocimientos.md`, y no toques `.obsidian/`.

- El repaso lo hace el usuario con el plugin. Nunca edites ni borres los comentarios `<!--SR:...-->` que agrega el plugin.
- Cuando un concepto pasa a `demostrado`, agregá su tarjeta en `Repaso/` en la misma sesión, siguiendo el formato de `Mi-progreso/README.md`.
- Si el usuario cuenta al empezar la sesión que falló una tarjeta, hacele una pregunta nueva sobre ese concepto. Si confirma la dificultad, bajalo a `en aprendizaje` con la evidencia. Si acierta, no cambies nada.
- Los repasos no generan una entrada en `Mi seguimiento.md`, salvo que cambien un estado.

Cuando una sesión cambie `Repaso/`, incluí esa carpeta en el commit de progreso junto con `Mi-progreso/`.

## Sincronización con Git

Al iniciar una sesión de aprendizaje, si el árbol de trabajo está limpio, actualizá primero la copia local:

```bash
git pull --rebase
```

Si hay cambios locales sin confirmar, no hagas pull ni descartes nada automáticamente: trabajá con cuidado y avisá del posible conflicto.

Si la sesión cambió archivos de `Mi-progreso/`, al finalizar sincronizalos:

```bash
git add Mi-progreso
git commit -m "progress: update learning state"
git push
```

No crees un commit si no hubo cambios. No incluyas otros archivos en ese commit salvo que el usuario haya pedido explícitamente modificarlos como parte de la misma tarea.

## Skills de enseñanza

La configuración de enseñanza de `amosblomqvist/learn` puede vivir en `.pi/`. Tratala como un sistema independiente: no la edites para guardar progreso.

La persistencia del roadmap vive en `.agents/skills/roadmap-progress/` y `Mi-progreso/`. Si una sesión usa la skill `teach`, combiná su metodología pedagógica con la skill `roadmap-progress` para cargar y guardar el estado.

## Privacidad

No guardes credenciales, secretos, datos de pacientes ni información personal sensible innecesaria en el progreso.

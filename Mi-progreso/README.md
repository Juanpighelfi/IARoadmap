# Progreso compartido

Esta carpeta es la fuente de verdad del progreso de aprendizaje de este roadmap. La usan la edición manual, Pi y ChatGPT.

## Archivos canónicos

- `Mi seguimiento.md`: tema actual y registro breve de sesiones.
- `Conocimientos.md`: estado persistente por concepto y evidencia observada.

No dupliques este estado en otros archivos salvo que una actividad tenga su propia respuesta o código.

## Estados permitidos

Usá únicamente estos tres estados en `Conocimientos.md`:

- `pendiente`: todavía no hay evidencia suficiente para evaluar el concepto.
- `en aprendizaje`: hay comprensión parcial, dudas o errores relevantes que todavía conviene trabajar.
- `demostrado`: el concepto fue comprobado mediante una respuesta, explicación, ejercicio o variante resuelta sin depender de copiar la solución.

`demostrado` no significa dominio permanente. Si una comprobación posterior muestra una dificultad relevante, puede volver a `en aprendizaje`.

## Regla de evidencia

Nunca cambies un concepto a `demostrado` porque fue explicado, leído o mostrado. Promovelo solo cuando exista evidencia observable del usuario.

La columna `Evidencia` debe contener una frase breve y concreta, por ejemplo:

- `Distingue let y const y predice una reasignación inválida.`
- `Resuelve un for simple pero confunde for...of con índices.`

La columna `Última comprobación` usa `YYYY-MM-DD`.

## Registro de sesión

Las entradas nuevas en `Mi seguimiento.md` usan este formato:

```markdown
### YYYY-MM-DD — Pi|ChatGPT|manual

- Hice:
- Me costó:
- Cómo sigo:
```

Solo agregá una entrada cuando la sesión haya producido aprendizaje, práctica o una decisión concreta sobre el próximo paso.

## Repaso espaciado

El calendario de repaso lo lleva el plugin Obsidian Spaced Repetition, sobre las tarjetas de `Repaso/`. `Conocimientos.md` sigue guardando solo estado y evidencia: no lleva columnas ni fechas de repaso.

- El repaso lo hace el usuario con el plugin. Los agentes nunca editan ni borran los comentarios `<!--SR:...-->` que agrega el plugin.
- Cuando un concepto pasa a `demostrado`, el agente agrega su tarjeta en `Repaso/` en la misma sesión.
- Si el usuario falla una tarjeta, lo cuenta al empezar la sesión siguiente. El agente le hace una pregunta nueva sobre ese concepto y, si confirma la dificultad, lo baja a `en aprendizaje` con la evidencia. Si acierta, no cambia nada.
- Los repasos no generan una entrada en `Mi seguimiento.md`, salvo que cambien un estado.

Formato de las tarjetas:

- Un archivo por área (`Repaso/JavaScript.md`, `Repaso/TypeScript.md`, `Repaso/Node.js.md`, …) con la etiqueta `#flashcards` en la primera línea.
- Una tarjeta por concepto `demostrado`; los conceptos `en aprendizaje` todavía no llevan tarjeta.
- Tarjeta multilínea: pregunta arriba, una línea con solo `?` y la respuesta abajo. Una línea en blanco separa las tarjetas, así que no puede haber líneas en blanco dentro de una tarjeta (tampoco antes de un bloque de código).
- Preguntas de predecir o explicar, nunca de recitar una definición. La respuesta da el resultado y el porqué en una o dos líneas.
- Si la tarjeta tiene código, su salida se comprueba ejecutándolo con Node antes de escribir la respuesta.
- No usar `::` ni `==` fuera de los bloques de código: el plugin los interpreta como otro tipo de tarjeta.

## Flujo con Pi

Antes de empezar una sesión en la copia local:

```bash
git pull --rebase
```

Pi debe leer `Mi seguimiento.md` y `Conocimientos.md` antes de decidir qué enseñar o evaluar.

Si al terminar cambió el progreso:

```bash
git add Mi-progreso
git commit -m "progress: update learning state"
git push
```

Si no cambió nada, no hace falta crear un commit.

## Flujo con ChatGPT

ChatGPT debe leer estos mismos dos archivos desde GitHub cuando el pedido dependa del progreso previo. Si durante la conversación aparece evidencia nueva, puede actualizar directamente estos archivos en el repositorio privado.

## Privacidad

No guardes credenciales, secretos, datos de pacientes ni información personal sensible que no sea necesaria para aprender. El repositorio es privado, pero el seguimiento debe seguir siendo mínimo.

# Mi seguimiento

## Ahora

Estoy estudiando: Node.js — asincronía (hilo único, bloqueo, promesas, async/await) antes de leer archivos en un script real

## Registro

### 2026-09-10 — ChatGPT

- Hice: Diagnóstico y práctica de fundamentos de JavaScript: tipos, truthy/falsy, `let`/`const`, referencias, funciones y `return`, arrays, objetos, `break` y `continue`; cerré con un ejercicio integrador escrito desde cero sobre inventario. Después avancé al ejercicio aplicado de horarios del módulo 01.
- Me costó: Al inicio hubo dudas con `typeof null`, truthy/falsy, reasignación de `const`, referencias compartidas, propiedades dinámicas y diferencia entre `break` y `continue`. En el integrador corregí `const`/`let` y `return`. En la primera versión de `cabeTurno` usé una comparación matemática encadenada que JavaScript no interpreta como esperaba y acepté duración `0` aunque el contrato la declara inválida.
- Cómo sigo: Corregir `cabeTurno`, comprobar casos borde y después pasar la misma lógica a TypeScript y Node.js.

### 2026-09-17 — ChatGPT

- Hice: Cerré el bloque de JSON y datos externos: distinguí JSON malformado de datos inválidos para el contrato, practiqué `try/catch`, entendí que `as` no valida ni transforma valores y validé `Turno` en runtime incluyendo números finitos.
- Me costó: Al principio confundí la causa de un JSON inválido y el comportamiento de `try/catch`; también asumí que `typeof x === "number"` alcanzaba para aceptar cualquier número, hasta distinguir `NaN`/`Infinity` de valores finitos.
- Cómo sigo: Leer una lista JSON ficticia desde un archivo, validar sus elementos y producir un resumen de turnos válidos e inválidos; después practicar la variante con archivo ausente y JSON malformado en un script real.

### 2026-09-21 — Claude

- Hice: Probe de lectura de archivos en Node: la raíz de los errores era no tener la noción de «operación que empezó y todavía no terminó». Trabajé los nodos 1 (hilo único), 2 (esperar no es trabajar, pero puede bloquear) y 3 (por qué `readFile` tiene que devolver una promesa) del plan de asincronía.
- Me costó: Creía que Node atendía pedidos en otro hilo y que `async` hacía correr código en paralelo; también pensaba que esperar una respuesta de red ocupaba al hilo siempre, y no solo cuando bloquea.
- Cómo sigo: Nodo 4: cómo engancharle a la promesa lo que depende del resultado. Después `await`/`async` y errores asíncronos. Revisar si `async` ≠ paralelo quedó firme.

### 2026-09-24 — Claude

- Hice: Nodos 4 (la «nota» que depende del resultado es una función: callbacks y `.then`) y 5 (`await` pausa la función y suelta el hilo; `async` es el permiso para pausar).
- Me costó: Primero pensé que la nota podía ser un `if`; después dudé si `then(nota())` y `then(nota)` eran distintos. Al principio creí que con `await` el hilo se quedaba esperando.
- Cómo sigo: Nodo 6: errores asíncronos (por qué `try/catch` necesita `await`, qué es `ENOENT`) y recomprobar que `async` no evita bloquear con un cálculo largo. Después, el script real que lee `turnos.json`.

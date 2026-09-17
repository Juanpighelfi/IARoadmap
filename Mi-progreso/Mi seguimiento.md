# Mi seguimiento

## Ahora

Estoy estudiando: Node.js / JSON — lectura de archivos y procesamiento de datos externos

## Registro

### 2026-09-10 — ChatGPT

- Hice: Diagnóstico y práctica de fundamentos de JavaScript: tipos, truthy/falsy, `let`/`const`, referencias, funciones y `return`, arrays, objetos, `break` y `continue`; cerré con un ejercicio integrador escrito desde cero sobre inventario. Después avancé al ejercicio aplicado de horarios del módulo 01.
- Me costó: Al inicio hubo dudas con `typeof null`, truthy/falsy, reasignación de `const`, referencias compartidas, propiedades dinámicas y diferencia entre `break` y `continue`. En el integrador corregí `const`/`let` y `return`. En la primera versión de `cabeTurno` usé una comparación matemática encadenada que JavaScript no interpreta como esperaba y acepté duración `0` aunque el contrato la declara inválida.
- Cómo sigo: Corregir `cabeTurno`, comprobar casos borde y después pasar la misma lógica a TypeScript y Node.js.

### 2026-09-17 — ChatGPT

- Hice: Cerré el bloque de JSON y datos externos: distinguí JSON malformado de datos inválidos para el contrato, practiqué `try/catch`, entendí que `as` no valida ni transforma valores y validé `Turno` en runtime incluyendo números finitos.
- Me costó: Al principio confundí la causa de un JSON inválido y el comportamiento de `try/catch`; también asumí que `typeof x === "number"` alcanzaba para aceptar cualquier número, hasta distinguir `NaN`/`Infinity` de valores finitos.
- Cómo sigo: Leer una lista JSON ficticia desde un archivo, validar sus elementos y producir un resumen de turnos válidos e inválidos; después practicar la variante con archivo ausente y JSON malformado en un script real.

# Conocimientos

Este archivo guarda el estado persistente por concepto. No es una calificación: sirve para decidir qué practicar o revisar después.

| Área | Concepto | Estado | Evidencia | Última comprobación |
| --- | --- | --- | --- | --- |
| JavaScript | variables | demostrado | Distingue `let` de `const`, comprende que `const` impide reasignar la referencia pero no mutar el objeto y, tras detectar el error en un ejercicio propio, corrigió el acumulador a `let` cuando necesitaba reasignarlo. | 2026-09-10 |
| JavaScript | tipos | demostrado | Distingue `number`, `string`, `boolean`, `undefined` y `null`; comprende que el tipo pertenece al valor, que una variable puede cambiar de tipo y recuerda la rareza `typeof null === "object"`. | 2026-09-10 |
| JavaScript | condicionales | demostrado | Predice correctamente `if/else`, `else if`, `&&`, `||` y coerción booleana; identificó que `"false"` y `[]` son truthy mientras `""` y `null` son falsy. | 2026-09-10 |
| JavaScript | bucles | demostrado | Predice correctamente `for`, `for...of`, filtrado y acumulación; distingue `continue` como salto de la iteración actual y `break` como terminación completa del bucle. | 2026-09-10 |
| JavaScript | funciones | demostrado | Distingue parámetros de argumentos y comprende que `return` devuelve un valor y termina la ejecución de la función; en un ejercicio propio corrigió la omisión de `return` y devolvió correctamente el acumulado. | 2026-09-10 |
| JavaScript | arrays | demostrado | Comprende que `b = a` comparte la misma referencia y que `b = [...a]` crea un array independiente con los mismos elementos; predijo correctamente el efecto de `push` en ambos casos. | 2026-09-10 |
| JavaScript | objetos | demostrado | Distingue acceso literal con punto de acceso dinámico con corchetes; predijo correctamente `undefined` para propiedades inexistentes y el valor esperado para `obj[clave]`. | 2026-09-10 |
| JavaScript aplicado | validación de entradas y límites | demostrado | Implementó validación de enteros, rangos 0–1440, duración positiva y franja con inicio menor que fin; corrigió comparaciones y verificó correctamente que un turno que termina exactamente en el límite sigue siendo válido. | 2026-09-11 |
| JavaScript aplicado | composición de funciones y búsqueda en colecciones | demostrado | Escribió una función que recorre franjas y reutiliza `cabeTurno`; comprendió que `return true` termina toda la función y que `return false` debe quedar después del bucle para no cortar la búsqueda antes de revisar todas las franjas. | 2026-09-11 |
| TypeScript | tipos en parámetros y validación runtime | demostrado | Corrigió `int` por `number`, tipó una función con cuatro parámetros `number` y retorno `boolean`, y explicó que los datos externos de una API deben validarse en runtime porque no se puede asumir con qué tipo llegan. | 2026-09-11 |
| TypeScript | tipos de objetos | demostrado | Definió tipos `Franja` y `Turno`, comprendió que esos parámetros se tipan con el nombre del objeto en lugar de `number`, y escribió una función `cabeTurno(franja: Franja, turno: Turno): boolean` accediendo correctamente a sus propiedades. | 2026-09-11 |

#flashcards

<!-- markdownlint-disable-file MD018 MD031 -->

¿Qué imprime este código y qué pasa en la última línea? ¿Por qué?
```js
const turno = { hora: 540 };
turno.hora = 600;
console.log(turno.hora);
turno = { hora: 700 };
```
?
Imprime `600` y después lanza `TypeError: Assignment to constant variable`.
`const` impide reasignar la variable, pero no impide cambiar el objeto al que apunta.

¿Qué imprimen las dos llamadas a `typeof`? ¿Por qué la variable no «es» de un tipo fijo?
```js
let x = null;
console.log(typeof x);
x = 42;
console.log(typeof x);
```
?
Imprime `object` y después `number`.
El tipo pertenece al valor, no a la variable; `typeof null` da `"object"` por una rareza histórica de JavaScript.

¿Qué imprime cada vuelta? ¿Por qué `"false"` y `"0"` no se comportan como `false` y `0`?
```js
const valores = ["false", [], "", null, 0, "0"];
for (const v of valores) {
  console.log(v ? "sí" : "no");
}
```
?
Imprime `sí`, `sí`, `no`, `no`, `no`, `sí`.
Los valores falsy son una lista corta (`false`, `0`, `""`, `null`, `undefined`, `NaN` y pocos más); cualquier string con texto y cualquier array, aunque esté vacío, son truthy.

¿Qué números imprime este bucle y por qué?
```js
for (const hora of [9, 10, 11, 12, 13]) {
  if (hora === 10) continue;
  if (hora === 12) break;
  console.log(hora);
}
```
?
Imprime `9` y `11`.
`continue` salta solo la vuelta del 10; `break` termina el bucle entero en el 12, así que el 13 nunca se visita.

¿Qué imprime este código y por qué no imprime `10`?
```js
function duplicar(n) {
  n * 2;
}
console.log(duplicar(5));
```
?
Imprime `undefined`.
La función calcula `n * 2` pero no lo devuelve; sin `return`, una función devuelve `undefined`.

¿Qué imprime este código y por qué los largos son distintos?
```js
const a = [1, 2];
const b = a;
const c = [...a];
b.push(3);
console.log(a.length, c.length);
```
?
Imprime `3 2`.
`b = a` comparte la misma referencia, así que el `push` también cambia `a`; `[...a]` creó un array nuevo e independiente.

¿Qué imprime este código y por qué las dos formas de acceso dan resultados distintos?
```js
const turno = { paciente: "Ana", hora: 540 };
const clave = "hora";
console.log(turno.clave, turno[clave]);
```
?
Imprime `undefined 540`.
Con punto se busca literalmente una propiedad llamada `clave`, que no existe; con corchetes se usa el valor de la variable (`"hora"`).

Esta validación de rango, ¿qué imprime para un inicio de 2000 minutos? ¿Por qué no sirve?
```js
const inicio = 2000;
console.log(0 <= inicio <= 1440);
```
?
Imprime `true`, aunque 2000 está fuera de rango.
Se evalúa de izquierda a derecha: `0 <= 2000` da `true`, y `true <= 1440` compara `1 <= 1440`. Hay que escribir `0 <= inicio && inicio <= 1440`.

¿Qué imprime este código si la segunda franja sí tiene lugar para 60 minutos? ¿Por qué?
```js
function hayLugar(franjas, duracion) {
  for (const f of franjas) {
    if (f.fin - f.inicio >= duracion) return true;
    else return false;
  }
}
console.log(hayLugar([{ inicio: 540, fin: 560 }, { inicio: 600, fin: 720 }], 60));
```
?
Imprime `false`.
La primera franja (20 minutos) ejecuta `return false`, que termina toda la función antes de revisar la segunda. El `return false` va después del bucle.

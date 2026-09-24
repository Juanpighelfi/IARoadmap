#flashcards

<!-- markdownlint-disable-file MD018 MD031 -->

¿Qué imprime cada vuelta? ¿Por qué el segundo y el tercer texto fallan de maneras distintas?
```js
const textos = ['{"hora": 540}', "{hora: 540}", '{"hora": "nueve"}'];
for (const t of textos) {
  try {
    const d = JSON.parse(t);
    console.log(typeof d.hora);
  } catch (error) {
    console.log(error.name);
  }
}
```
?
Imprime `number`, `SyntaxError` y `string`.
El segundo es JSON malformado (las claves van entre comillas dobles) y `JSON.parse` lanza; el tercero es JSON válido pero con un dato inválido para `Turno`, y `JSON.parse` no lo detecta: eso es trabajo de tu validación.

Un mensaje de WhatsApp tiene que atenderse «en 0 ms», pero justo después empieza un `while` de 3 segundos. ¿En qué orden se imprime y por qué?
```js
setTimeout(() => console.log("mensaje de WhatsApp"), 0);
const fin = Date.now() + 3000;
while (Date.now() < fin) {}
console.log("terminó el while");
```
?
Primero `terminó el while` (a los 3 s) y después `mensaje de WhatsApp`.
Todo tu JavaScript corre en un solo hilo: el callback no puede ejecutarse hasta que el `while` suelte al cocinero.

Cada mensaje de WhatsApp hace una consulta que tarda 150 ms, y el código la espera de forma bloqueante. ¿Qué le pasa a un segundo mensaje que llega a mitad de la espera? ¿Cuántos mensajes por segundo se pueden atender como máximo?
?
El segundo mensaje espera: el único hilo está frenado hasta recibir la respuesta.
Como máximo unos 6 o 7 por segundo (1000 ÷ 150 ≈ 6,7), aunque el hilo no esté trabajando sino solo esperando.

¿Qué imprime este código y por qué no imprime el contenido del archivo? ¿Qué cambia si el archivo no existe?
```js
import { readFile } from "node:fs/promises";
const datos = readFile("turnos.json", "utf8");
console.log(datos);
```
?
Imprime `Promise { <pending> }`.
`readFile` no puede contestar al instante y el hilo tiene que seguir, así que devuelve un ticket del resultado futuro. Si el archivo no existe, se imprime lo mismo y después la promesa queda rechazada con `ENOENT`; como nadie maneja ese rechazo, Node termina con error.

`turnos.json` existe. ¿En qué orden se imprimen `A` y `B` con `.then(nota())`? ¿Y con `.then(nota)`? ¿Por qué?
```js
import { readFile } from "node:fs/promises";
function nota(texto) {
  console.log("B");
}
readFile("turnos.json", "utf8").then(nota());
console.log("A");
```
?
Con `nota()` sale `B` y después `A`; con `nota` sale `A` y después `B`.
Los paréntesis ejecutan la nota en el acto, sin el texto; sin paréntesis se entrega la función y el hilo la llama cuando la promesa se cumple.

¿En qué orden se imprimen `A`, `B` y `C`? ¿Qué hace el hilo mientras la función espera?
```js
import { readFile } from "node:fs/promises";
async function leer() {
  console.log("A");
  await readFile("turnos.json", "utf8");
  console.log("B");
}
leer();
console.log("C");
```
?
Imprime `A`, `C`, `B`.
El `await` pausa solo `leer` y le devuelve una promesa a quien la llamó: el hilo queda libre para seguir con `C` (o atender mensajes) y retoma `B` cuando el archivo está leído.

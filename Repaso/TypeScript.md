#flashcards

<!-- markdownlint-disable-file MD018 MD031 -->

¿Este código compila? ¿Qué imprime al ejecutarlo y por qué?
```ts
function empiezaAntes(inicio: number, fin: number): boolean {
  return inicio < fin;
}
const datos = JSON.parse('{"inicio": "90", "fin": "600"}');
console.log(empiezaAntes(datos.inicio, datos.fin));
```
?
Compila e imprime `false`, aunque 90 es menor que 600.
`JSON.parse` devuelve `any` y los tipos de TypeScript desaparecen al ejecutar: llegaron strings y se compararon como texto (`"9"` > `"6"`). Los datos externos se validan en runtime.

¿Por qué TypeScript marca error en esta función y cómo se corrige?
```ts
type Turno = { inicio: number; duracion: number };
function calcularFin(turno: number): number {
  return turno.inicio + turno.duracion;
}
```
?
Porque `turno` está tipado como `number`, y un número no tiene `inicio` ni `duracion`.
El parámetro recibe un objeto, así que se tipa con el nombre del tipo: `turno: Turno`.

¿Cuál de estas dos declaraciones da error y por qué?
```ts
type Turno = { paciente: string; observacion?: string };
const a: Turno = { paciente: "Ana" };
const b: Turno = { paciente: "Luis", observacion: 123 };
```
?
Solo `b`.
El `?` permite omitir `observacion`, como en `a`; pero si la propiedad aparece, tiene que ser `string`, y `123` no lo es.

¿Cuáles de estas líneas dan error y por qué?
```ts
type Modalidad = "presencial" | "virtual";
const m1: Modalidad = "virtual";
const m2: Modalidad = "telefonica";
const m3: Modalidad = "Presencial";
```
?
Dan error `m2` y `m3`.
El union de literales acepta solo esos textos exactos: `"telefonica"` no está en la lista y `"Presencial"` difiere por la mayúscula.

¿Por qué TypeScript rechaza este array?
```ts
type Turno = { paciente: string; modalidad: "presencial" | "virtual" };
const turnos: Turno[] = [
  { paciente: "Ana", modalidad: "virtual" },
  { paciente: "Luis" },
];
```
?
Porque el segundo elemento no tiene `modalidad`.
En un `Turno[]` cada elemento tiene que cumplir el tipo `Turno` completo, y `modalidad` es obligatoria.

¿Qué dice TypeScript de esta función y qué devolvería sin él, con cualquier lista?
```ts
type Turno = { paciente: string; modalidad: "presencial" | "virtual" };
function contarPresenciales(turnos: Turno[]): number {
  let total = 0;
  for (const t of turnos) {
    if (t.modalidad === "Presencial") total++;
  }
  return total;
}
```
?
Marca error: la comparación nunca puede ser verdadera, porque `modalidad` solo puede ser `"presencial"` o `"virtual"`.
Sin TypeScript la función devolvería siempre `0` por la mayúscula.

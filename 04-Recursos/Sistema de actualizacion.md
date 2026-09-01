---
tags:
  - recursos
  - metodo
  - actualizacion
---

# Sistema de actualizacion

[[04-Recursos/Anti-roadmap]] dice "no persigas cada modelo nuevo sin aprender patrones
estables". Correcto, pero incompleto: sin un sistema, el resultado no es calma, es
enterarse tarde de cosas que si importaban. Esta nota es el reemplazo concreto.

## La pregunta filtro

Ante cualquier noticia, lanzamiento o paper:

> Esto cambia alguna decision que tengo que tomar este mes?

Si la respuesta es no, va a una lista de "quiza mas adelante" y no ocupa mas tiempo.
La mayoria de lo que se publica no pasa este filtro, y esta bien.

## Cadencia

| Frecuencia | Que | Tiempo |
| --- | --- | --- |
| Diario | Nada obligatorio | 0 |
| Semanal | Un paper con [[05-Plantillas/Plantilla de lectura de paper]] y una pasada por 2 o 3 fuentes | 60-90 min |
| Mensual | Revisar si algo de la lista de "quiza" ya afecta una decision | 30 min |
| Trimestral | Revisar el propio roadmap: precios, herramientas discontinuadas, enlaces rotos, temas nuevos que ya son core | 2 h |

La revision trimestral del vault va junto con la de
[[00-MOC/Estado actual]] y se anota en [[CHANGELOG]].

## Fuentes, pocas y estables

Mejor tres leidas que veinte suscriptas.

**Base:**

- Simon Willison, blog y anotaciones: <https://simonwillison.net/>. La mejor relacion
  senal/ruido para saber que cambio de verdad, con ejemplos ejecutables.
- Sebastian Raschka, Ahead of AI: <https://magazine.sebastianraschka.com/>. Profundidad
  tecnica sin hype, especialmente en entrenamiento y post-training.
- Import AI, Jack Clark: <https://importai.substack.com/>. Panorama semanal con lectura
  de politica y seguridad.

**Segun en que estes:**

- Blogs de ingenieria de los proveedores que uses. Son donde aparecen primero los
  patrones aplicados.
- Hugging Face blog y papers de la semana: <https://huggingface.co/papers>.
- Latent Space, para la parte de producto e ingenieria aplicada:
  <https://www.latent.space/>.
- Papers with Code: <https://paperswithcode.com/>.
- arXiv Sanity: <https://arxiv-sanity-lite.com/>.

**Para no perderse en papers:** que el paper llegue por una de las fuentes de arriba,
no al reves. Suscribirse directo a categorias de arXiv es una forma eficiente de leer
nada.

## Que ignorar con tranquilidad

- Rankings de benchmarks que cambian cada semana.
- Hilos de "esta herramienta lo cambia todo" sin codigo ni numeros.
- Comparativas de modelos hechas con cinco prompts a ojo.
- Frameworks nuevos que envuelven algo que ya sabes hacer en 40 lineas.
- Anuncios de modelos que no podes usar todavia.

## Como se decide adoptar algo

Cuatro preguntas, en orden:

1. Que problema mio resuelve, concretamente.
2. Que estoy usando hoy para eso y por que no alcanza.
3. Cuanto cuesta migrar y cuanto cuesta volver atras.
4. Va a existir en dos anos, y si no, que tan atado quedo.

Si no podes contestar la 1 y la 2, no es una necesidad, es curiosidad. La curiosidad
esta bien pero va a un experimento de una tarde, no al producto.

## Cuota de experimentacion

Una tarde cada dos semanas para probar algo nuevo sin justificacion, con caja cerrada:
si a las tres horas no anda, se abandona y se anota por que. Asi la curiosidad tiene un
lugar y deja de interrumpir el trabajo.

---
tags:
  - nivel
  - carrera
  - comunicacion
  - continuo
duracion: continua
estado: pendiente
inicio:
fin:
---

# 12b - Capa profesional

El roadmap termina en el capstone y ahi se corta. Pero un capstone no consigue trabajo
ni clientes por si solo: lo hace alguien que puede explicar que construyo, por que tomo
cada decision y que salio mal. Este nivel cubre esa traduccion.

No es un nivel con fecha de fin. Corre en paralelo desde el mes 3, no al final.

## 1. Escribir sobre lo que construis

La regla mas rentable del roadmap: por cada proyecto del
[[03-Proyectos/Portfolio minimo]], un texto publico.

- Formato que funciona: problema, que probaste primero, por que no alcanzo, que
  construiste, que medias, que salio mal, que harias distinto.
- Los resultados negativos y los postmortems son mas leidos y mas creibles que los
  tutoriales. Tambien son mas faciles de escribir porque ya los viviste.
- Tu [[06-Bitacora/Como usar la bitacora|bitacora]] es el borrador. Escribir a fin de
  mes desde las cuatro entradas semanales cuesta una hora; escribir de memoria a fin de
  ano es imposible.
- Cadencia realista: una publicacion por mes. Doce al ano es un cuerpo de trabajo.

## 2. Presentar el portfolio

- Cada repo con README que abra con **que problema resuelve y para quien**, no con
  como instalarlo.
- Demo de 60 segundos: video o GIF. Casi nadie va a clonar tu repo.
- Arquitectura en un diagrama y tres decisiones con su tradeoff.
- El dataset de evaluacion y los resultados visibles. Es lo que distingue un proyecto
  de un tutorial seguido.
- Costo y latencia medidos, de [[11b - Inferencia costos y economia unitaria]]. Casi
  ningun portfolio junior los tiene y son lo primero que pregunta alguien con
  experiencia.
- Tres proyectos profundos superan a diez superficiales, siempre.

## 3. Comunicacion tecnica

- Explicar un sistema en tres niveles de profundidad segun quien escucha: usuario,
  colega tecnico, persona que decide el presupuesto.
- Escribir un documento de diseno antes de construir algo grande: problema,
  alternativas, eleccion, riesgos, como se mide el exito.
- Postmortem sin culpables: que fallo, como se detecto, cuanto tardo, que cambia para
  que no se repita.
- Estimar y comunicar incertidumbre en vez de prometer certezas.

## 4. Leer papers sin ahogarte

- Metodo de tres pasadas con [[05-Plantillas/Plantilla de lectura de paper]].
- Cuota: un paper por semana leido de verdad supera a veinte guardados para despues.
- Criterio de seleccion: leelo si cambia una decision que tenes que tomar, si es la
  base de algo que ya usas, o si aparece citado en todos lados hace meses. El resto es
  ruido con formato academico.
- Abandonar en la primera pasada es el comportamiento correcto la mayoria de las veces.

## 5. Entrevistas y clientes

- Si buscas empleo: diseno de sistemas de IA (armar un RAG o un agente en pizarra con
  tradeoffs, costos y evals), fundamentos de ML, y una defensa profunda de un proyecto
  propio. Practica explicar el mismo proyecto en 2, 10 y 30 minutos.
- Si buscas clientes o construis producto propio: el problema del cliente antes que la
  tecnologia, precio en funcion del valor y no del costo de tokens, y un piloto acotado
  con criterio de exito escrito antes de empezar. Ver
  [[02-Rutas/Si estas construyendo un producto]].
- En los dos casos: los numeros de tus propios proyectos son tu credencial mas fuerte.

## 6. Estar al dia sin perseguir el hype

Ver [[04-Recursos/Sistema de actualizacion]]. El resumen: cadencia fija, pocas fuentes,
y la pregunta filtro "esto cambia alguna decision que tengo que tomar este mes".

## Practica

- Publicar el primer texto sobre un proyecto ya terminado, aunque sea viejo.
- Reescribir el README del mejor repo que tengas siguiendo la seccion 2.
- Grabar una explicacion de 5 minutos de tu proyecto y verla. Duele y funciona.
- Un documento de diseno para lo proximo que vayas a construir, antes de escribir codigo.
- Leer y fichar cuatro papers en un mes con la plantilla, abandonando los que no pasen
  la primera pasada.

## Criterio de salida

No hay uno. Hay un ritmo sostenido: un texto por mes, un paper por semana, un README
que alguien externo entiende sin que vos se lo expliques.

## Recursos

- How to Read a Paper, S. Keshav:
  <https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf>
- Simon Willison, blog y anotaciones diarias: <https://simonwillison.net/>
- Sebastian Raschka, Ahead of AI: <https://magazine.sebastianraschka.com/>
- Chip Huyen, escritos sobre carrera y sistemas de ML: <https://huyenchip.com/blog/>
- Papers with Code: <https://paperswithcode.com/>

## Siguiente

- [[03-Proyectos/Capstone]]
- [[02-Rutas/Si estas construyendo un producto]]

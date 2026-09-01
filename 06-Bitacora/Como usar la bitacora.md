---
tags:
  - bitacora
  - metodo
---

# Como usar la bitacora

El roadmap dice a donde ir. La bitacora dice donde estas. Sin ella, un plan de 12 meses
es una lista de deseos: no hay forma de saber si vas atrasado, si un nivel te esta
costando el triple de lo previsto, o si llevas seis semanas leyendo sin construir nada.

## Regla minima

Una entrada por semana. Cinco minutos el domingo. Si una semana no estudiaste, la
entrada igual se escribe y dice que no estudiaste: los ceros son el dato mas util
del registro.

## Como funciona

1. Durante la semana, una nota corta por sesion con
   [[05-Plantillas/Plantilla de sesion de estudio]]. Opcional, pero si la usas la
   entrada semanal se escribe sola.
2. El domingo, una entrada con [[05-Plantillas/Plantilla de bitacora semanal]],
   nombrada `AAAA-Wnn.md` (ejemplo: `2026-W36.md`).
3. Al cerrar un nivel, actualizas su `estado` a `hecho` en el frontmatter y anotas la
   fecha en [[00-MOC/Estado actual]].

## Que registrar

- **Horas reales**, no las planeadas. El plan supone 8-10 h por semana; si tu promedio
  real es 4, el plan de 12 meses es de 24 y mas vale saberlo en el mes 2 que en el 9.
- **Lo construido**, con enlace al commit o al repo. Sin artefacto no cuenta.
- **Lo que no entendiste.** Es la seccion que mas rinde: de ahi salen las tarjetas de
  [[04-Recursos/Repaso espaciado]] y los temas que hay que volver a mirar.
- **Decisiones**, con su motivo. En dos meses no vas a acordarte de por que elegiste
  Qdrant sobre Chroma, y vas a volver a perder la tarde comparandolos.

## Que no registrar

- Resumenes de lo que leiste. Para eso estan las notas de nivel.
- Sentimientos sobre el progreso sin un numero al lado.

## Para que sirve despues

- Es el material para escribir sobre lo que hiciste, que es la mitad de
  [[01-Niveles/12b - Capa profesional]].
- Es la evidencia real de tu portfolio: fechas, decisiones, errores y correcciones.
- Es lo que te deja hacer una retrospectiva honesta cada trimestre en lugar de
  reescribir el plan cada vez que te aburris de un nivel.

## Revision trimestral

Cada 12 semanas, abri las ultimas 12 entradas y responde tres preguntas:

1. Horas reales por semana, promedio. Ajusta el plan a ese numero, no al reves.
2. Ratio construir / leer. Si leer gana, cambia el proximo mes por un proyecto.
3. Que aparece repetido en "que no entendi". Eso es un hueco de fundamentos, no una
   mala semana: volve al nivel que lo cubre.

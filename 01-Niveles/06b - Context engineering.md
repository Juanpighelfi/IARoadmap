---
tags:
  - nivel
  - context-engineering
  - llm
  - memoria
duracion: 3-5 semanas
estado: pendiente
inicio:
fin:
---

# 06b - Context engineering

Prompting es escribir buenas instrucciones. Context engineering es decidir **que
informacion entra en la ventana, en que forma y en que momento**, y que se hace cuando
no entra. En sistemas reales el segundo problema es mas dificil y explica mas fallas
que el primero.

Se separa de [[06 - LLMs aplicados]] porque ahi el contexto se asume dado. Aca el
contexto es la variable de diseno.

## Debes aprender

- Presupuesto de contexto: cuantos tokens gasta cada parte (system, herramientas,
  historial, documentos recuperados, salida esperada) y como se reparte.
- Degradacion por longitud: por que mas contexto no es mejor contexto. Perdida de
  informacion en el medio, dilucion de las instrucciones, aumento de latencia y costo.
- Seleccion: recuperar lo relevante en vez de pegar todo. Conecta con
  [[07 - RAG busqueda embeddings]], pero aplica tambien a historial, esquemas y
  definiciones de herramientas.
- Compactacion: resumir el historial, mantener un estado estructurado aparte, decidir
  que se descarta y como se recupera si vuelve a hacer falta.
- Memoria: working memory de la tarea, memoria episodica de la conversacion, memoria
  persistente del usuario. Que se escribe, cuando se lee, como se corrige y como
  caduca.
- Estado externo frente a estado en contexto: archivos, base de datos o notas como
  memoria del sistema, con el contexto como vista temporal de ese estado.
- Sub-agentes y aislamiento: delegar una subtarea con su propia ventana limpia y
  devolver solo el resultado, para no contaminar el contexto principal.
- Tareas de horizonte largo: como sobrevive un sistema a decenas de pasos sin perder
  el objetivo original.
- Caching de prompts: que se puede cachear, como ordenar el contexto para que el prefijo
  estable quede al principio, y que ahorro real produce.
- Higiene: datos sensibles que no deben entrar al contexto ni a los logs. Conecta con
  [[10 - Evaluacion seguridad gobernanza]].

## Practica

- Instrumentar una app tuya para medir tokens por seccion del contexto en cada llamada.
  Publicar el desglose. Casi siempre aparece una seccion que gasta el triple de lo
  esperado y no aporta nada.
- Tomar un asistente con historial largo y aplicar tres estrategias de compactacion
  (ventana deslizante, resumen incremental, estado estructurado). Comparar calidad,
  costo y latencia sobre el mismo set de conversaciones.
- Diseno de memoria: definir por escrito que se guarda de un usuario, con que politica
  de escritura, lectura, correccion y borrado. Implementarlo y probar que un dato
  corregido no reaparece.
- Reordenar el contexto para maximizar aciertos de cache y medir el ahorro real.
- Romperlo a proposito: llenar la ventana hasta el limite y documentar como falla el
  sistema, si degrada o si se cae.

## Criterio de salida

Podes mostrar el presupuesto de tokens de tu sistema, justificar por que cada bloque
esta ahi, y explicar que pasa cuando el contexto se llena en vez de esperar que no
pase.

## Recursos

- Anthropic, Effective context engineering for AI agents:
  <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
- Lost in the Middle, degradacion por posicion en contextos largos:
  <https://arxiv.org/abs/2307.03172>
- Visualizacion de un LLM ejecutandose, para intuicion de tokens y atencion:
  <https://bbycroft.net/llm>
- Prompt Engineering Guide: <https://www.promptingguide.ai/>

## Siguiente

- [[07 - RAG busqueda embeddings]]
- [[08 - Agentes workflows automatizacion]]
- [[11b - Inferencia costos y economia unitaria]]

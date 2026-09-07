---
id: "06b"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 06b - Context engineering

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

Qué estudiar: Selección de contexto, memoria y compactación; convertir cada patrón en una hipótesis medible con tu modelo.

### Diagnóstico breve

Diferenciá dato permanente, estado de tarea e historial prescindible en una conversación de diez turnos. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Creá diez conversaciones donde se corrige una medida. Compará ventana reciente, resumen y estado estructurado con el mismo presupuesto de entrada.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Poné la corrección al principio, al medio y al final. Comprobá si reaparece la medida antigua después de compactar.

### Cómo comprobar que aprendí

Presupuesto por bloque y prueba de recuperación de correcciones; calidad, costo y latencia comparables. Documentar información perdida por cada estrategia.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si el resumen borra decisiones, mantener estado explícito con fecha y fuente. Si aumenta tokens sin mejorar, reducir contexto por hipótesis.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

Prompting es escribir buenas instrucciones. Context engineering es decidir **que
informacion entra en la ventana, en que forma y en que momento**, y que se hace cuando
no entra. En tareas con mucho contexto, su selección puede explicar fallas que no se resuelven solo cambiando instrucciones.

Se separa de [06 - LLMs aplicados](06%20-%20LLMs%20aplicados.md) porque ahi el contexto se asume dado. Aca el
contexto es la variable de diseno.

## Debes aprender

- Presupuesto de contexto: cuantos tokens gasta cada parte (system, herramientas,
  historial, documentos recuperados, salida esperada) y como se reparte.
- Degradacion por longitud: por que mas contexto no es mejor contexto. Perdida de
  informacion en el medio, dilucion de las instrucciones, aumento de latencia y costo.
- Seleccion: recuperar lo relevante en vez de pegar todo. Conecta con
  [07 - RAG busqueda embeddings](07%20-%20RAG%20busqueda%20embeddings.md), pero aplica tambien a historial, esquemas y
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
  [10 - Evaluacion seguridad gobernanza](10%20-%20Evaluacion%20seguridad%20gobernanza.md).

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Instrumentar una app tuya para medir tokens por seccion del contexto en cada llamada.
  Guardar el desglose y comprobar si alguna sección consume más contexto del que aporta a la tarea.
- Tomar un asistente con historial largo y aplicar tres estrategias de compactacion
  (ventana deslizante, resumen incremental, estado estructurado). Comparar calidad,
  costo y latencia sobre el mismo set de conversaciones.
- Diseno de memoria: definir por escrito que se guarda de un usuario, con que politica
  de escritura, lectura, correccion y borrado. Implementarlo y probar que un dato
  corregido no reaparece.
- Reordenar el contexto para maximizar aciertos de cache y medir el ahorro real.
- Romperlo a proposito: llenar la ventana hasta el limite y documentar como falla el
  sistema, si degrada o si se cae.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Anthropic, Effective context engineering for AI agents:
  <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
- Lost in the Middle, degradacion por posicion en contextos largos:
  <https://arxiv.org/abs/2307.03172>
- Visualizacion de un LLM ejecutandose, para intuicion de tokens y atencion:
  <https://bbycroft.net/llm>
- Prompt Engineering Guide: <https://www.promptingguide.ai/>

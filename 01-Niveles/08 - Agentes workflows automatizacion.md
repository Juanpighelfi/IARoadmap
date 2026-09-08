---
id: "08"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 08 - Agentes, workflows y automatizacion segura

[Abrir la hoja de ejercicios 08, lista para completar](../08-Ejercicios/08.md). Resolvé ahí el diagnóstico, la práctica y las variantes. Si hay código o laboratorio, la hoja indica qué probar y dónde anotar el resultado.

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://www.anthropic.com/engineering/building-effective-agents>

Qué estudiar: Workflows, routing y tool use; implementar primero una máquina de estados y comparar con un loop de agente.

### Diagnóstico breve

Para clasificar una nota y guardarla, indicá qué pasos necesitan decisión probabilística y cuáles son deterministas. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Construí un workflow local con dos herramientas simuladas: consultar ficha y proponer actualización. Guardar el cambio requiere aprobación explícita en la simulación; limitar pasos y reintentos.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). La hoja de este módulo reúne los espacios de respuesta; las referencias amplían el procedimiento.

### Práctica independiente

Simulá timeout, llamada duplicada, argumento inválido e instrucción hostil en el resultado de consulta. Compará agente y workflow con veinte tareas iguales.

### Cómo comprobar que aprendí

Traza reproducible, acciones acotadas, sin escrituras duplicadas y salida segura al agotar pasos. Explicar costo y razones para usar o descartar el agente.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si el loop no termina, poner estado terminal y presupuesto. Si repite escrituras, diseñar idempotencia antes de cambiar modelo.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Diferencia entre workflow determinista, agent loop y multi-agent system.
- Patrones: planner-executor, ReAct, router, evaluator-optimizer.
- Tool use: contratos, permisos, sandboxing, retries, timeouts, audit logs.
- Memoria: episodica, semantica, working memory, retrieval memory.
- Orquestacion: state machines, queues, human-in-the-loop.
- Seguridad: prompt injection, data exfiltration, herramientas destructivas, autorizaciones.
- Observabilidad: traces, spans, decisiones, inputs/outputs de herramientas.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Agente que investiga un tema, cita fuentes, genera reporte y registra cada paso.
- Workflow de documentos con OCR, extraccion estructurada, revision humana y export.
- Agente con herramientas limitadas y politica de permisos explicita.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- ReAct paper: <https://arxiv.org/abs/2210.03629>
- LangGraph docs: <https://langchain-ai.github.io/langgraph/>
- CrewAI docs: <https://docs.crewai.com/>
- Anthropic, Building effective agents (la fuente de los patrones de arriba):
  <https://www.anthropic.com/engineering/building-effective-agents>
- Hugging Face Agents Course: <https://huggingface.co/learn/agents-course>

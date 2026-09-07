---
id: "06"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 06 - LLMs aplicados

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://huggingface.co/learn/llm-course/>

Qué estudiar: Introducción a Transformers, tokenización y uso de modelos preentrenados. Para structured outputs usar la documentación del proveedor o runtime elegido.

### Diagnóstico breve

Diseñá un esquema para extraer material, tamaño y color de una descripción. Indicá qué harías si falta el tamaño. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Prepará 30 descripciones sintéticas con respuesta esperada y extraé JSON. Compará una regla con un modelo disponible; validar campos, capturar error y permitir abstención.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Agregá unidades inconsistentes, una instrucción maliciosa dentro de la descripción y campos faltantes. Medí por separado esquema válido y contenido correcto.

### Rúbrica de salida

Dataset fijo, versión de modelo/prompt, resultados por campo y política de abstención; no inventar valores faltantes ni considerar JSON válido como evidencia de verdad.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si falla el formato, revisar contrato; si falla el significado, inspeccionar casos y mejorar ejemplos antes de añadir un agente.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Tokens, contexto, temperatura, top-p, streaming, latencia, costos.
- Prompting: instrucciones, ejemplos, restricciones, formato, decomposition.
- Structured outputs: JSON schema, validacion, parsers, retries.
- Tool/function calling: contratos, permisos, idempotencia, errores.
- Memoria conversacional: que guardar, que no guardar, privacidad.
- Model selection: proveedor, modelo open source, costo, calidad, latencia, datos.
- Limitaciones: hallucinations, prompt injection, dependencia de contexto.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Asistente CLI que resume, extrae datos y responde con JSON validado.
- API de soporte que decide si responde, pide aclaracion o llama una herramienta.
- Suite de 30 casos de prueba para prompts y outputs.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Prompt Engineering Guide: <https://www.promptingguide.ai/>
- Hugging Face Course: <https://huggingface.co/course>
- DeepLearning.AI short courses: <https://www.deeplearning.ai/courses/>
- Hugging Face LLM Course: <https://huggingface.co/learn/llm-course>
- Chip Huyen, AI Engineering (el libro que mas se solapa con los niveles 06, 10 y 11):
  <https://huyenchip.com/books/>
- Visualizacion de un LLM ejecutandose paso a paso: <https://bbycroft.net/llm>

---
id: "09"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 09 - Multimodalidad

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://huggingface.co/tasks>

Qué estudiar: Image-to-text, ASR y document question answering como panorama. Elegir una modalidad; consultar OpenCV/Tesseract para un baseline de documentos.

### Diagnóstico breve

Elegí una métrica para transcripción y otra para extraer una tabla. Explicá por qué mirar cinco respuestas no basta. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Creá diez documentos sintéticos con campos conocidos y variaciones de orientación. Compará extracción con OCR/reglas y un modelo disponible. Etiquetá cada campo esperado.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Agregá un campo ilegible y una página vacía. El sistema debe marcar incertidumbre o abstenerse en vez de completar por plausibilidad.

### Cómo comprobar que aprendí

Correctitud por campo, tasa de abstención, fallos por calidad de entrada y costo registrados; no extrapolar de documentos sintéticos a reales.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si cambia por rotación, revisar preprocesamiento. Si alucina texto, separar extracción de inferencia y exigir evidencia localizada.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Vision: clasificacion, deteccion, OCR, image embeddings.
- Document AI: PDFs, tablas, formularios, layout, OCR, extraccion robusta.
- Audio: speech-to-text, text-to-speech, voice agents, diarization basica.
- Multimodal prompting: imagen + texto, documento + texto, audio + texto.
- UX de sistemas IA: confirmaciones, controles, revision humana, incertidumbre visible.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Pipeline que extrae campos de facturas o contratos con validacion.
- Buscador multimodal de imagenes o documentos.
- Voice assistant pequeno con logs y fallback a texto.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Hugging Face tasks: <https://huggingface.co/tasks>
- OpenCV docs: <https://docs.opencv.org/>
- Tesseract OCR: <https://github.com/tesseract-ocr/tesseract>

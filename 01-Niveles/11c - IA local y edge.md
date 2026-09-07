---
id: "11c"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 11c - IA local y edge

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://pytorch.org/tutorials/>

Qué estudiar: Saving/loading models, inference y deployment como consulta. Usar inicialmente CPU; exportación y cuantización según el runtime elegido y su compatibilidad.

### Diagnóstico breve

Separá memoria de pesos, activaciones y entradas. Explicá cómo verificar que una optimización conserva calidad. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Tomá el modelo de visión o un MLP pequeño y medí inferencia CPU con batch 1. Registrar latencia extremo a extremo, tamaño del artefacto y calidad del conjunto reservado.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Probá una precisión menor o un modelo más pequeño si el runtime lo permite; compará con el original. Simulá cámara desconectada y entradas fuera de rango.

### Cómo comprobar que aprendí

Tabla de calidad/latencia/memoria en hardware identificado, prueba offline y fallback ante entrada inválida; un resultado negativo también acredita el experimento.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si el entorno no soporta cuantización, comparar un modelo menor y documentar el límite. No instalar varios runtimes a la vez.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

## Debes aprender

- Inferencia offline, CPU/GPU y restricciones de memoria.
- Cuantización, exportación y compatibilidad de operadores.
- Medir captura, preprocesamiento, modelo y salida por separado.
- Modelos pequeños, distilación como extensión, consumo y degradación de calidad.

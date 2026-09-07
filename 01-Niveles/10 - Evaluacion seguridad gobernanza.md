---
id: "10"
tags: [nivel, transversal]
revisado: 2026-09-06
---

# 10 - Evaluacion, seguridad, privacidad y gobernanza

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://scikit-learn.org/stable/common_pitfalls.html>

Qué estudiar: evaluación independiente y errores de medición. Para la ruta personal, empezar con la práctica administrativa siguiente y [OWASP Top 10](https://owasp.org/www-project-top-ten/); no hace falta instalar scikit-learn ni entrenar un modelo. Las secciones de ML y RAG se retoman al elegir esas ramas.

### Aplicación temprana al SaaS

Antes de conectar modelos o proveedores, escribir diez casos sobre un registro administrativo: entrada válida, importe negativo, ID duplicado, cuenta equivocada, falta de sesión, timeout, evento repetido, evento viejo, salida inválida y solicitud ambigua. Definir resultado esperado y cuáles bloquean una entrega. Comparar una regla permisiva y otra que rechaza todo: medir errores y cobertura sin usar un modelo.

Inventariar datos necesarios, quién puede acceder, dónde se guardan y qué no se registra en logs. Usar datos ficticios. Reservar casos distintos para evaluación final; no ajustar el sistema sobre ellos. Aplicar la rúbrica de salida a esta práctica y retomar las amenazas de modelos en 06–08 dentro de esos módulos, sin duplicar horas.

### Diagnóstico breve

Diferenciá pruebas unitarias, validación de modelos y conjunto de test final. Escribí una falla que pase JSON schema. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Antes del primer modelo, escribí diez casos y una rúbrica. Separá desarrollo y test. Para ML usá etiquetas; para LLMs incluí no-answer, cita falsa y entrada hostil.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Construí un sistema deliberadamente malo que siempre abstenga y otro que siempre responda. Tu evaluación debe distinguir cobertura, errores y abstención.

### Rúbrica de salida

Criterios fijados antes de comparar, casos frontera, versión y errores por segmento; no usar un juez LLM sin contrastarlo con etiquetas humanas propias.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si todo pasa, probar controles negativos. Si el juez discrepa, revisar rúbrica y casos ambiguos antes de confiar en el promedio.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Evals deterministas: schema, regex, exact match, unit tests, tool-call shape.
- Evals semanticas: rubricas, LLM-as-judge con cautela, pairwise comparison.
- Evals de RAG: retrieval, groundedness, citation faithfulness.
- Red teaming: prompt injection, jailbreaks, datos sensibles, herramientas peligrosas.
- Privacidad: PII, minimizacion, retention, logs, proveedores.
- Gobernanza: owners, risk register, aprobaciones, incident response.
- Fairness y sesgo: datasets, segmentos, monitoreo, impacto.
- Cumplimiento según jurisdicción: aplicabilidad y clasificación de riesgo cuando corresponda,
  regimenes de datos personales y reglas extra en dominios sensibles. Ver
  [Regulacion y cumplimiento](../04-Recursos/Regulacion%20y%20cumplimiento.md).

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Crear un eval harness con 50 a 100 casos reales o simulados.
- Red-team de tu app: 30 ataques y mitigaciones.
- Documento de riesgos: que puede salir mal, severidad, deteccion, mitigacion.
- Determinar primero jurisdicción y alcance; si corresponde, consultar el marco aplicable y documentar preguntas pendientes sin afirmar cumplimiento.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- NIST AI RMF: <https://airc.nist.gov/airmf-resources/>
- OWASP Top 10 for LLM Applications: <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
- RAGAS: <https://docs.ragas.io/>
- Arize Phoenix: <https://phoenix.arize.com/>
- Hamel Husain, Your AI Product Needs Evals: <https://hamel.dev/blog/posts/evals/>
- Explorador del EU AI Act: <https://artificialintelligence-act.eu/>

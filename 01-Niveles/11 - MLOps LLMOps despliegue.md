---
id: "11"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 11 - MLOps, LLMOps, despliegue y observabilidad

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://madewithml.com/>

Qué estudiar: Serving, testing, versioning y monitoring. Adaptar a una API local antes de estudiar cloud; Docker y MLflow se consultan para lo que efectivamente uses.

### Diagnóstico breve

Explicá cómo volver a la versión anterior del modelo y sus datos si empeora sin cambiar el código. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Serví un modelo ya evaluado mediante un endpoint local, con validación de entrada y health check. Guardá versión de código, modelo, dependencias y métricas.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Simulá un artefacto faltante y una entrada inválida; desplegá una versión peor y hacé rollback. No requiere usuarios externos.

### Rúbrica de salida

Arranque reproducible, errores visibles, regresión antes del cambio y rollback que recupera resultados previos; secretos fuera del repositorio.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si no se reproduce, fijar dependencias y artefactos antes de agregar infraestructura. Si solo falla en servicio, revisar preprocesamiento train/serve.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

## Debes aprender

- Packaging, Docker, CI/CD, config y secrets.
- Serving: FastAPI, batch inference, async jobs, queues, caching.
- Experiment tracking y model registry.
- Versionado de datos, codigo, prompts, embeddings e indices.
- Monitoring: latencia, costo, errores, calidad, drift, feedback.
- Rollbacks, canary releases, feature flags.
- Infra: cloud basico, GPU/CPU tradeoffs, serverless vs containers.
- SLOs: disponibilidad, tiempo de respuesta, costo por request, calidad minima.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Deploy de una API de IA con Docker, CI y health checks.
- Dashboard de latencia, errores, costo y calidad.
- Pipeline que reindexa docs, ejecuta evals y bloquea despliegue si cae la calidad.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Google Cloud MLOps whitepaper: <https://cloud.google.com/resources/mlops-whitepaper>
- MLflow docs: <https://mlflow.org/docs/latest/>
- Docker docs: <https://docs.docker.com/>
- Prometheus docs: <https://prometheus.io/docs/>
- OpenTelemetry: <https://opentelemetry.io/docs/>
- Chip Huyen, Designing Machine Learning Systems: <https://huyenchip.com/books/>
- Made With ML, MLOps aplicado de punta a punta: <https://madewithml.com/>

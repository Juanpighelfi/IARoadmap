# Proyecto conductor: SaaS administrativo con IA

Aprender a comprender, construir y operar un servicio recurrente para profesionales. El primer caso de práctica es administrativo: agenda y registro de cobros; una función de IA se incorpora después si mejora un proceso medible.

## Punto de partida

Se revisó código del [SaaS existente](Estudiar%20con%20el%20SaaS%20real.md), fijando la revisión inspeccionada: TypeScript/Node.js, React/Vite, Fastify, PostgreSQL/Drizzle, Redis/BullMQ, WhatsApp por Twilio e IA mediante un cliente para Vertex/Mistral. Hay implementación de panel, simulador, turnos, cobros e integraciones; no se ejecutaron ni certificaron esos recorridos. Trabajá en una copia de aprendizaje con datos ficticios. El objetivo es comprender y comprobar lo existente, no reconstruir un SaaS imaginario.

## Recuperar el control del código

1. Leer `package.json`, `web/package.json`, las reglas del repositorio y el mapa de código enlazado. Contrastar documentación y código: `docs/stack-explicado` todavía contiene referencias a Evolution API, pero la implementación actual usa Twilio.
2. Registrar comandos de inicio y pruebas, versiones y nombres de variables requeridas, nunca sus valores secretos.
3. Arrancar el entorno de prueba. Si no arranca, elegir un solo fallo reproducible y documentar entrada, salida esperada y resultado observado.
4. Seguir un recorrido: pantalla → endpoint → validación → datos → respuesta. Marcar cada parte que no se comprende.
5. Clasificar funciones como comprobada, rota o no evaluada. Una pantalla visible no demuestra que persista ni que respete permisos.
6. Elegir una corrección pequeña, escribir criterios, revisar el diff y comprobar el resultado. Explicar el cambio sin leer la respuesta de la IA.

Si todavía no tenés fundamentos para estos pasos, hacer primero los ejercicios 01 y 01b. La tarea de inventario es una aplicación de esos módulos y usa su tiempo.

## Primer alcance propuesto

Primero comprender una función pura de horarios y su prueba. Después, cuando estén los fundamentos, seguir una consulta administrativa por el simulador existente, identificar job, worker y cambio de estado. Verificar el alcance por profesional con cuentas ficticias; luego recorrer creación/cancelación de un turno y un cobro de prueba. Reutilizar pantallas y servicios existentes; una funcionalidad se repara después de reproducir su fallo.

La demo de landing, el simulador del panel y un webhook Twilio son recorridos distintos. La guía de código muestra qué prueba cada uno. Una confirmación visible en una demo no acredita persistencia ni una integración externa.

Distinguir desde el modelo de datos:

- Cobro por el servicio profesional: lo que paga su cliente o paciente.
- Suscripción al SaaS: lo que el profesional paga por usar el software.
- Facturación fiscal: integración separada; registrar un cobro no equivale a emitir un comprobante fiscal.

## Entregas acumulativas

| Módulo | Evidencia reutilizable |
| --- | --- |
| 01 y 01b | Script administrativo simple y diff explicado; inventario cuando alcance la base |
| 02 | Consultas sobre turnos y pagos ficticios, importes exactos y datos inválidos |
| 10 y 12d | Datos, permisos, proceso actual, excepciones y criterio de éxito |
| 01c y 02b | Flujo web persistente; pruebas de aislamiento entre cuentas |
| 08c | Evento duplicado o fuera de orden sin estado incorrecto; suscripción separada |
| 11d | Entorno de prueba desplegado, error diagnosticado y respaldo restaurado |
| 06 y 06b | Clasificación o extracción de consultas administrativas con salida validada |
| 08 y 10b | Workflow limitado, casos de error, revisión humana y conjunto reservado |
| 11b y 12b | Costo por tarea, guía de uso y propuesta de piloto actualizada |

## Primer uso de IA

El producto ya tiene Brain y parser de salida. Aislar una decisión administrativa y revisar sus pruebas antes de cambiar prompts: JSON válido no implica decisión válida, y una decisión válida no implica operación completada. Comparar una tarea acotada con reglas, con datos ficticios y revisión antes de cualquier envío. Si no mejora el proceso, conservar reglas es un resultado válido.

Los mensajes de prueba no se envían a personas reales. El modelo no decide sobre cobros, permisos ni estado definitivo de una operación. No incluir diagnóstico, recomendaciones clínicas ni emisión autónoma de recetas en este proyecto de aprendizaje. Las funciones clínicas y los datos reales de salud requieren un alcance separado, validación profesional y revisión de los requisitos aplicables antes de implementarse para uso real.

## De práctica a piloto

La demo académica se verifica con datos ficticios y puede cerrarse con autoevaluación. Un piloto real requiere además un flujo estable, permisos probados, recuperación ensayada, costos entendidos, acuerdo sobre el uso de datos y revisión del contexto aplicable en [regulación y cumplimiento](../04-Recursos/Regulacion%20y%20cumplimiento.md). No se afirma aquí que el producto existente cumpla esos requisitos.

Primero mostrar un único recorrido a un profesional interesado y observar si resuelve su tarea. Registrar interés, uso y pago por separado. No prometer una fecha comercial hasta comprobar el recorrido elegido en ejecución.

## Regla de cierre

Una entrega termina cuando hay código o documento identificable, prueba, explicación propia y siguiente paso. Usá las [prácticas SaaS](../07-Laboratorios/Practicas%20SaaS.md) y los [criterios de cierre del capstone](Capstone.md). Todo ese trabajo cuenta dentro del estudio aplicado, una sola vez.

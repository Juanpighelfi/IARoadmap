# Proyecto conductor: SaaS administrativo con IA

Aprender a comprender, construir y operar un servicio recurrente para profesionales. El primer caso de práctica es administrativo: agenda y registro de cobros; una función de IA se incorpora después si mejora un proceso medible.

## Punto de partida

Existe un SaaS desarrollado con ayuda de IA, pausado y con fallos, pero su repositorio y stack no se revisaron al adaptar esta ruta. No se presupone qué funciones existen ni se prescribe reescribirlo. Trabajá en una copia o rama de desarrollo y un entorno con datos ficticios.

## Recuperar el control del código

1. Leer README, manifiestos y estructura. Anotar lenguaje, interfaz, servidor, base de datos y servicios externos a partir de archivos concretos.
2. Registrar comandos de inicio y pruebas, versiones y nombres de variables requeridas, nunca sus valores secretos.
3. Arrancar el entorno de prueba. Si no arranca, elegir un solo fallo reproducible y documentar entrada, salida esperada y resultado observado.
4. Seguir un recorrido: pantalla → endpoint → validación → datos → respuesta. Marcar cada parte que no se comprende.
5. Clasificar funciones como comprobada, rota o no evaluada. Una pantalla visible no demuestra que persista ni que respete permisos.
6. Elegir una corrección pequeña, escribir criterios, revisar el diff y comprobar el resultado. Explicar el cambio sin leer la respuesta de la IA.

Si todavía no tenés fundamentos para estos pasos, hacer primero los ejercicios 01 y 01b. La tarea de inventario es una aplicación de esos módulos y usa su tiempo.

## Primer alcance propuesto

Dos profesionales ficticios pueden entrar con sus cuentas, crear y cancelar sus propios turnos y registrar un cobro simulado. El alcance se ajusta al inventario y a la necesidad observada: reparar un flujo existente tiene prioridad sobre agregar pantallas.

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

Elegí una sola tarea: clasificar consultas administrativas o preparar un borrador de respuesta usando información ficticia aprobada, con revisión antes de enviarlo. Compará con reglas simples; medí errores y tiempo incluyendo revisión. Si no mejora el proceso, conservar reglas es un resultado válido.

Los mensajes de prueba no se envían a personas reales. El modelo no decide sobre cobros, permisos ni estado definitivo de una operación. No incluir diagnóstico, recomendaciones clínicas ni emisión autónoma de recetas en este proyecto de aprendizaje. Las funciones clínicas y los datos reales de salud requieren un alcance separado, validación profesional y revisión de los requisitos aplicables antes de implementarse para uso real.

## De práctica a piloto

La demo académica se verifica con datos ficticios y puede cerrarse con autoevaluación. Un piloto real requiere además un flujo estable, permisos probados, recuperación ensayada, costos entendidos, acuerdo sobre el uso de datos y revisión del contexto aplicable en [regulación y cumplimiento](../04-Recursos/Regulacion%20y%20cumplimiento.md). No se afirma aquí que el producto existente cumpla esos requisitos.

Primero mostrar un único recorrido a un profesional interesado y observar si resuelve su tarea. Registrar interés, uso y pago por separado. No prometer una fecha comercial hasta inspeccionar el producto y comprobar el alcance.

## Regla de cierre

Una entrega termina cuando hay código o documento identificable, prueba, explicación propia y siguiente paso. Usá las [prácticas SaaS](../07-Laboratorios/Practicas%20SaaS.md) y la [rúbrica de capstone](Capstone.md). Todo ese trabajo cuenta dentro del estudio aplicado, una sola vez.

---
id: "08c"
tags: [nivel, ia-aplicada, saas]
revisado: 2026-09-07
---

# 08c - Integraciones, webhooks y cobros confiables

Consultá horas y prerrequisitos en el [catálogo](../00-MOC/Catalogo%20de%20modulos.md). La carga cubre el ejercicio acotado de este módulo, con lectura, corrección y primer repaso; no un curso entero más el producto completo.

## Resultado

Integrar eventos externos sin duplicar efectos y distinguir el pago del servicio profesional de la suscripción que el profesional abona por usar el SaaS.

## Recurso y lectura seleccionada

La [documentación de webhooks de Stripe](https://docs.stripe.com/webhooks) sirve para estudiar notificaciones, verificación y entregas repetidas. Se usa como referencia conceptual, no como elección de proveedor ni afirmación de disponibilidad en Argentina. Para una integración real, verificar la documentación, condiciones y entorno de pruebas del proveedor elegido.

## Diagnóstico

Un proveedor avisa dos veces que se completó el mismo pago. Explicar por qué crear dos registros es incorrecto y dónde guardarías que el evento ya se procesó, incluso después de reiniciar.

## Aprender

- Credenciales en servidor, permisos mínimos y secretos fuera de repositorios y registros.
- Webhooks frente a consultas periódicas; autenticidad, validación del mensaje y reconciliación con el estado del proveedor.
- Idempotencia: registro durable de eventos y restricción única, con cambios de negocio dentro de una transacción.
- Reintentos limitados, timeout, fallos parciales y revisión manual de operaciones que no se pueden completar.
- Distinguir estado interno, estado informado por el proveedor y estado confirmado; una redirección del navegador no confirma un pago.
- Separar cobro al paciente, suscripción al SaaS y emisión fiscal: son procesos distintos, con identificadores y estados propios.
- Cambios de suscripción, fallos de cobro, cancelación y fecha efectiva de acceso según una política explícita.

## Práctica guiada

Usar el simulador descrito en [prácticas SaaS](../07-Laboratorios/Practicas%20SaaS.md), sin proveedor ni dinero real. Recibir eventos de pago con ID único; validar esquema; escribir el evento y el cambio de estado de forma atómica. Procesar duplicados, reinicio y notificación fuera de orden.

## Práctica independiente

Simular una suscripción al software con estados pendiente, activa y cancelada. Definir cuándo se pierde acceso en el ejercicio y comprobarlo. Si el evento no permite decidir el estado actual, dejarlo pendiente de reconciliación en lugar de adivinar.

## Condiciones de salida

El mismo evento enviado dos veces, incluso en paralelo o tras un reinicio, produce un solo efecto. Una referencia desconocida queda identificada sin alterar otros registros. Un error temporal tiene reintentos acotados y un fallo definitivo queda visible para revisión. Mostrar que la suscripción del profesional no se confunde con los cobros de sus pacientes.

El simulador solo acredita lógica local. La firma real se prueba después en sandbox del proveedor, incluyendo firma inválida y cuerpo alterado; no marcar integración externa verificada antes de esa prueba. Facturación fiscal queda como integración separada a validar antes de operar.

## Si no sale

Reducir a un evento y una tabla de operaciones procesadas. Comprobar primero duplicados y transacciones; luego agregar reintentos. No sumar otro proveedor para eludir el fallo.

## Evaluación y retención

Aplicá la [rúbrica de dominio](../04-Recursos/Autoevaluacion%20y%20dominio.md): implementación, comparación válida, explicación propia y transferencia, de 0 a 2 cada una. Para dominio: 7/8 como mínimo y ninguna dimensión en 0. Guardá evidencia y ayuda usada en `Mi-progreso/`; repetir una variante a los 7 días y reconstruir el razonamiento a los 30. Una demo que funciona con ayuda no acredita todavía independencia.

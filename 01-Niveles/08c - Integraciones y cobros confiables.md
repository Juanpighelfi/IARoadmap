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

El proyecto usa Mercado Pago: empezar por su [documentación de webhooks](https://www.mercadopago.com.ar/developers/es/docs/your-integrations/notifications/webhooks) y contrastarla con `src/webhooks/mercadopago-route.ts`. Para las colas existentes, consultar [workers de BullMQ](https://docs.bullmq.io/guide/workers). El [mapa del SaaS real](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md) enlaza los archivos revisados. No agregar Stripe ni otro proveedor para completar este módulo.

## Diagnóstico

Un proveedor avisa dos veces que se completó el mismo pago. Explicar por qué crear dos registros es incorrecto y dónde guardarías que el evento ya se procesó, incluso después de reiniciar.

## Aprender

- Credenciales en servidor, permisos mínimos y secretos fuera de repositorios y registros.
- Webhooks frente a consultas periódicas; autenticidad, validación del mensaje y reconciliación con el estado del proveedor.
- Idempotencia: registro durable de eventos y restricción única, con cambios de negocio dentro de una transacción.
- Redis/BullMQ: productor, trabajo, consumidor y registro de workers; distinguir HTTP aceptado de tarea completada.
- Reintentos limitados, timeout, fallos parciales y revisión manual de operaciones que no se pueden completar.
- OAuth por profesional en Google Calendar y Mercado Pago; permisos, vencimiento y revocación. No confundir OAuth con verificar la firma de un webhook.
- Distinguir estado interno, estado informado por el proveedor y estado confirmado; una redirección del navegador no confirma un pago.
- Separar cobro al paciente, suscripción al SaaS y emisión fiscal: son procesos distintos, con identificadores y estados propios.
- Cambios de suscripción, fallos de cobro, cancelación y fecha efectiva de acceso según una política explícita.

## Práctica guiada

Usar el ejercicio de eventos sintéticos descrito en [prácticas SaaS](../07-Laboratorios/Practicas%20SaaS.md), sin proveedor ni dinero real. No es el simulador conversacional del panel, que puede invocar servicios según su configuración. Relacionar cada paso con el webhook y las colas existentes, sin duplicar el subsistema. Recibir eventos de pago con ID único; validar esquema; escribir el evento y el cambio de estado de forma atómica. Procesar duplicados, reinicio y notificación fuera de orden.

## Práctica independiente

Como ejercicio acotado, simular una suscripción al software con estados pendiente, activa y cancelada. Su ciclo completo en el producto quedó por verificar en la revisión estática; no asumir que está terminado ni que falta por completo. Definir cuándo se pierde acceso en el ejercicio y comprobarlo. Si el evento no permite decidir el estado actual, dejarlo pendiente de reconciliación en lugar de adivinar.

## Condiciones de salida

El mismo evento enviado dos veces, incluso en paralelo o tras un reinicio, produce un solo efecto. Una referencia desconocida queda identificada sin alterar otros registros. Un error temporal tiene reintentos acotados y un fallo definitivo queda visible para revisión. Mostrar que la suscripción del profesional no se confunde con los cobros de sus pacientes.

El simulador solo acredita lógica local. La firma real se prueba después en sandbox del proveedor, incluyendo firma inválida y cuerpo alterado; no marcar integración externa verificada antes de esa prueba. Facturación fiscal queda como integración separada a validar antes de operar.

## Si no sale

Reducir a un evento y una tabla de operaciones procesadas. Comprobar primero duplicados y transacciones; luego agregar reintentos. No sumar otro proveedor para eludir el fallo.

## Cómo comprobar que aprendí

Usá la [comprobación breve](../04-Recursos/Autoevaluacion%20y%20dominio.md): resolver, explicar y probar una variante sin copiar, cumpliendo las condiciones de salida del módulo. Cerrá con tres líneas en [Mi seguimiento](../00-MOC/Estado%20actual.md). No hacen falta puntajes ni otra ficha; una demo hecha con ayuda no demuestra todavía independencia.

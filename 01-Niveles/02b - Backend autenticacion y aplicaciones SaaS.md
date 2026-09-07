---
id: "02b"
tags: [nivel, ia-aplicada, saas]
revisado: 2026-09-07
---

# 02b - Backend, autenticación y aplicaciones SaaS

Consultá horas y prerrequisitos en el [catálogo](../00-MOC/Catalogo%20de%20modulos.md). La carga cubre el ejercicio acotado de este módulo, con lectura, corrección y primer repaso; no un curso entero más el producto completo.

## Resultado

Construir un recorrido formulario → API → base de datos y separar la información de dos profesionales. Comprender primero un endpoint y su consulta; el proyecto ya tiene colas y workers, pero no es necesario dominarlos para este ejercicio.

## Recurso y lectura seleccionada

Leé [primeros pasos del servidor en MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps) para ubicar sus responsabilidades; retomá tablas, consultas y transacciones del [tutorial de PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html). Consultá [OWASP Top 10](https://owasp.org/www-project-top-ten/) para relacionar riesgos con pruebas concretas de acceso. Consultar [Fastify](https://fastify.dev/docs/latest/Guides/Getting-Started/) para rutas y plugins, y [Drizzle](https://orm.drizzle.team/docs/overview) para reconocer consultas y esquemas. Leer el mecanismo de sesión existente antes de modificarlo.

El [SaaS revisado](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md) usa Fastify, PostgreSQL, Drizzle y Zod. Seguir `src/admin/auth/scoping.ts` y `src/db/schema/appointments.ts` para entender permisos y datos. Su existencia no acredita que todos los endpoints estén protegidos; eso se comprueba con pruebas. No cambiar de framework ni reconstruir la autenticación para cursar.

## Diagnóstico

Dibujar dónde se guarda un turno y cómo sabe el servidor a qué profesional pertenece. Explicar por qué cambiar un identificador en la URL no debe permitir leer registros ajenos.

## Aprender

- Endpoints, contratos y validación del servidor; códigos de error y pruebas de integración.
- Tablas de cuentas, profesionales, turnos y registros de cobro; claves, relaciones, restricciones y migraciones.
- Autenticación frente a autorización; sesiones, cierre de sesión y recuperación de cuenta mediante componentes mantenidos.
- Aislamiento entre cuentas: derivar identidad de la sesión verificada y autorizar cada lectura y escritura, sin confiar en el propietario enviado por el cliente.
- Fechas, zonas horarias y dinero: guardar zona u offset explícitos y montos como enteros en unidad mínima o decimal exacto.
- Transacciones y restricciones para que dos solicitudes concurrentes no reserven el mismo horario exclusivo.

## Práctica guiada

Dos profesionales ficticios, A y B, con sus propias cuentas. Localizar las operaciones existentes para crear, listar y cancelar turnos; escribir pruebas sobre un recorrido acotado antes de cambiarlo. Guardarlos en una base de prueba y comprobar que persisten al reiniciar. Para el ejercicio de duración fija, usar esta regla mínima: mismo profesional y mismo inicio solo admite un turno activo; cancelarlo libera ese horario. Compararla con las reglas actuales antes de editar. No resuelve por sí sola solapamientos de duraciones distintas.

## Práctica independiente

Localizar el registro de cobros y probar una operación administrativa con un cobro ficticio asociado a un turno propio; si falta, diseñar una variante pequeña en la rama de aprendizaje. Es un registro administrativo, no mueve dinero ni emite una factura fiscal. Probar importes inválidos y acceso con otra cuenta.

## Condiciones de salida

- Sin sesión, la API rechaza acceder a los turnos.
- A no puede leer, cambiar ni cobrar un turno de B aunque adivine su ID; la API tampoco revela su contenido en errores.
- Dos altas simultáneas en el mismo horario no generan dos reservas activas.
- Un reinicio conserva los datos y una cancelación tiene el efecto previsto.
- La entrada inválida se rechaza también al llamar la API sin pasar por el formulario.

Son pruebas obligatorias para cerrar el módulo, además de la rúbrica. Un fallo de autorización bloquea el cierre aunque el puntaje restante sea alto.

## Si no sale

Separar persistencia de interfaz. Resolver primero una consulta del 02 y una prueba de permiso; después conectar la pantalla. Pedir a la IA una explicación o un cambio delimitado, no que reconstruya toda la aplicación.

## Evaluación y retención

Aplicá la [rúbrica de dominio](../04-Recursos/Autoevaluacion%20y%20dominio.md): implementación, comparación válida, explicación propia y transferencia, de 0 a 2 cada una. Para dominio: 7/8 como mínimo y ninguna dimensión en 0. Guardá evidencia y ayuda usada en `Mi-progreso/`; repetir una variante a los 7 días y reconstruir el razonamiento a los 30. Una demo que funciona con ayuda no acredita todavía independencia.

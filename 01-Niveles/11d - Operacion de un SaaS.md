---
id: "11d"
tags: [nivel, ia-aplicada, saas]
revisado: 2026-09-07
---

# 11d - Operación y mantenimiento de un SaaS

Consultá horas y prerrequisitos en el [catálogo](../00-MOC/Catalogo%20de%20modulos.md). La carga cubre el ejercicio acotado de este módulo, con lectura, corrección y primer repaso; no un curso entero más el producto completo.

## Resultado

Poner una versión de prueba en funcionamiento, detectar fallos y recuperarla. El despliegue de software no requiere completar entrenamiento de modelos; este módulo es independiente de la rama MLOps.

## Recurso y lectura seleccionada

Usá [The Twelve-Factor App](https://12factor.net/) como guía conceptual de configuración, dependencias, procesos y registros. Para comandos concretos, consultá la documentación oficial del alojamiento y la base de datos que efectivamente usa el SaaS. No se elige una plataforma nueva por completar el módulo.

Antes del despliegue, usar el [mapa del SaaS real](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md): `src/server.ts`, `src/worker-app.ts`, `WORKER_MODE`, scripts y CI. Explicar cuándo el servidor ejecuta consumidores y cuándo necesita un worker separado. Revisar por separado el typecheck del servidor y el de `web`; un chequeo del catálogo conversacional no sustituye una prueba de ejecución.

## Diagnóstico

Explicar cómo reproducir una versión, dónde viven sus secretos y qué harías si una actualización deja de guardar turnos. Distinguir volver al código anterior de recuperar datos dañados.

## Aprender

- Dependencias y versiones reproducibles; entornos local, prueba y producción separados.
- Configuración externa, HTTPS y credenciales; no copiar datos reales al entorno didáctico.
- Pruebas antes de desplegar y comprobación del flujo crítico después.
- Migraciones compatibles, reversión de aplicación y recuperación de base de datos.
- Logs con ID de correlación, sin datos sensibles; alertas accionables y diagnóstico de incidentes.
- Copia de seguridad y ensayo de restauración; registrar qué se pierde y cuánto tarda.
- Costo fijo, costo por operación, soporte, altas, cancelaciones y mantenimiento.

## Práctica guiada

Desplegar un entorno de prueba del flujo administrativo con datos ficticios. Registrar versión y configuración requerida. Provocar un fallo controlado, localizarlo desde los registros y recuperar el servicio siguiendo una guía escrita.

## Práctica independiente

Restaurar un respaldo en una base de prueba separada y ejecutar el flujo crítico. Medir tiempo de recuperación y registros recuperados. Escribir cómo revertir una versión sin aplicar una migración incompatible a ciegas.

## Condiciones de salida

Otra sesión puede reconstruir el entorno siguiendo una guía propia con comandos, versiones y configuración de prueba. Hay evidencia del flujo después del despliegue, un error diagnosticado y una restauración ensayada. El presupuesto incluye alojamiento, base de datos, integraciones y tiempo de soporte, aunque algunos importes sigan como hipótesis identificadas. Nunca presentar cifras hipotéticas como gasto medido.

Cerrar el módulo no equivale a certificar que el servicio está listo para datos de salud o uso comercial; esa decisión usa los controles y el alcance del [proyecto conductor](../03-Proyectos/SaaS%20administrativo%20con%20IA.md).

## Si no sale

Volver a ejecutar localmente desde instrucciones limpias. Resolver una sola dependencia o configuración faltante y repetir. No introducir contenedores u orquestadores adicionales si el problema es un comando sin documentar.

## Evaluación y retención

Aplicá la [rúbrica de dominio](../04-Recursos/Autoevaluacion%20y%20dominio.md): implementación, comparación válida, explicación propia y transferencia, de 0 a 2 cada una. Para dominio: 7/8 como mínimo y ninguna dimensión en 0. Guardá evidencia y ayuda usada en `Mi-progreso/`; repetir una variante a los 7 días y reconstruir el razonamiento a los 30. Una demo que funciona con ayuda no acredita todavía independencia.

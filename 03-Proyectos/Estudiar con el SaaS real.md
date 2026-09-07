# Estudiar con el SaaS real

Revisión de código del 7 de septiembre de 2026 sobre [asitente-administrativo-psiquiatria, revisión da1d6d1](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/tree/da1d6d116889c9f34d5b5c2eae278d1654a490ec). Los enlaces fijan esa revisión para que el material siga siendo verificable aunque cambie `main`.

**Alcance:** lectura del árbol, manifiestos, arranque, entrada de mensajes, colas, orquestación de IA, simulador, esquemas y pruebas seleccionadas. No se ejecutó el SaaS, no se accedió a bases de datos ni a servicios desplegados, y no se modificó su código. «Implementado en código» no significa «funcionando en producción». Las pruebas de este roadmap tampoco prueban el SaaS.

## Qué estudiar y dónde reconocerlo

| Capa | Tecnología y responsabilidad observadas | Evidencia del proyecto |
| --- | --- | --- |
| Lenguaje y ejecución | TypeScript, ESM y Node.js; manifiesto requiere Node 22 o posterior | [package.json](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/package.json) |
| Interfaz | React, Vite y React Router; landing y panel administrativo | [web/package.json](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/web/package.json) |
| Servidor | Fastify: plugins, webhooks, panel, métricas y arranque | [server.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/server.ts) |
| Validación | Zod para entradas y configuración; tipado no sustituye validación | [env.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/config/env.ts) |
| Persistencia | PostgreSQL y Drizzle, tablas y migraciones | [schema de turnos](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/db/schema/appointments.ts) |
| Trabajo asíncrono | Redis y BullMQ, contratos y registro de workers | [queue.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/services/queue.ts), [registro](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/services/queue-registry.ts) |
| WhatsApp | Twilio: recepción, firma, parser y cliente de salida | [webhook actual](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/whatsapp/webhook.route.ts) |
| IA | Cliente común con rutas para Vertex y Mistral; selección por configuración | [llm-client.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/services/llm-client.ts) |
| Integraciones | Google Calendar, Mercado Pago y servicio de facturación ARCA | [integraciones](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/tree/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/integrations), [facturación](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/billing/arca-service.ts) |
| Pruebas | Vitest, integración separada, Playwright y evaluación conversacional | [Vitest](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/vitest.config.ts), [CI](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/.github/workflows/ci.yml) |

Las dependencias del manifiesto son rangos declarados, no una recomendación de actualizar paquetes. Conservá el lockfile. `AI_PROVIDER` admite Vertex y Mistral, con Vertex como valor predeterminado del código leído; no se verificó el proveedor seleccionado en el entorno desplegado.

## Dos correcciones respecto de la documentación antigua

La carpeta [stack-explicado](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/tree/da1d6d116889c9f34d5b5c2eae278d1654a490ec/docs/stack-explicado) es útil como orientación, pero su README todavía describe Evolution API. El webhook actual importa Twilio y registra `/api/webhooks/whatsapp/twilio`; el contrato de configuración limita WhatsApp a Twilio. Usar el código para esa parte, no reinstalar Evolution API siguiendo la explicación histórica.

Asimismo, no reducir IA a «Gemini solamente»: el cliente común contiene las dos rutas citadas. Y el panel ya existe en React; aprender sobre él tiene más sentido que construir otra interfaz desde cero. Esta revisión no corrige esos documentos dentro del SaaS: solo identifica la diferencia para estudiar sin confundirse.

## Orden de aproximación

1. **Una función pura:** horarios semanales. Comprender entradas, condiciones y resultado sin levantar PostgreSQL, Redis ni un modelo.
2. **Un contrato:** salida de IA válida e inválida, leyendo parser y pruebas.
3. **Una pantalla y su petición:** cliente React → API Fastify, sin agregar otra interfaz.
4. **Un mensaje de prueba:** simulador → cola → dispatcher → Brain → respuesta.
5. **Una operación administrativa:** elegir y confirmar un turno, siguiendo estado y persistencia.
6. **Una integración:** evento de Mercado Pago y su firma; estudiar OAuth y errores antes de habilitar operaciones reales.

Cada paso entra cuando estén acreditados sus prerrequisitos en la ruta. No recorrer todo el sistema en una sesión ni modificar archivos clínicos para practicar sintaxis.

## Primera pieza real: horarios

Leé [weekly-schedule.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/appointments/weekly-schedule.ts) y sus [tests](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/appointments/__tests__/weekly-schedule.test.ts). Empezá con `slotFitsSchedule` y una sola franja: lunes de 540 a 720 minutos, modalidad presencial.

| Entrada de práctica | Resultado esperado |
| --- | --- |
| Lunes 540, duración 45, presencial | Cabe |
| Lunes 675, duración 45, presencial | Cabe; termina al cierre |
| Lunes 690, duración 45, presencial | No cabe |
| Martes sin rangos | No cabe |
| Lunes 600, duración 45, virtual | No cabe en esa franja presencial |

Predecí los resultados antes de leer las expectativas. En una copia de aprendizaje, implementá una versión mínima con parámetros explícitos; luego compará con la función real. La versión mínima no reemplaza el código del producto. La condición de cierre es explicar límites y modalidades y resolver una variante sin la IA.

Después de preparar las dependencias de una copia local del SaaS, este comando ejecuta su prueba existente:

```bash
npm test -- src/modules/appointments/__tests__/weekly-schedule.test.ts
```

No se ejecutó ese comando durante esta revisión. Un test aislado que pasa tampoco valida reservas concurrentes, calendario externo ni todo el SaaS.

## Distinguir tres recorridos conversacionales

| Recorrido | Entrada y ejecución observadas | Qué no demuestra por sí solo |
| --- | --- | --- |
| WhatsApp | Webhook Twilio → `dispatch` → cola → worker | Que el sandbox del panel pruebe la firma de Twilio |
| Simulador del panel | `/admin/api/simulator/send` → `system.inbound` → procesamiento interno, con identificadores de sesión y turno | Que no use proveedores o recursos reales; revisar configuración antes de ejecutarlo |
| Demo de landing | Motor `demo-engine.ts`: llama al Brain y usa simulaciones de operaciones de dominio | Que una reserva o cobro real se haya completado |

Evidencia: [simulator-api.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/admin/api/simulator-api.ts), [demo-engine.ts](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/demo/demo-engine.ts), [dispatcher](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/src/modules/router/main-dispatcher.ts).

En modo `WORKER_MODE=inline`, el servidor inicia el consumidor; en `none`, produce trabajos y necesita el proceso worker separado. Una petición aceptada no prueba que el trabajo se consumió ni que se entregó respuesta. Seguí un ID de turno y de job antes de cambiar el prompt.

## Módulo → ejercicio real

| Módulo | Trabajo acotado sobre el proyecto |
| --- | --- |
| 01 | Entender la función de horarios; funciones, objetos, arrays y tipos |
| 01b | Predecir una variante de horario, proponer un test y explicar un diff pequeño en una rama de práctica |
| 02 | Explicar tablas de profesionales y turnos, consultar datos ficticios con SQL antes de escribir la consulta Drizzle |
| 01c | Leer `web/src/admin/api/client.ts`, un componente y sus estados de carga/error |
| 02b | Seguir un endpoint hasta sus permisos; comprobar el alcance de `professionalId` con dos cuentas de prueba |
| 08c | Leer productor, cola y worker; firma de webhook y OAuth; distinguir reintento de duplicado |
| 11d | Entender procesos HTTP/worker, salud y recuperación; no desplegar durante una sesión introductoria |
| 06 y 06b | Leer `brain-client.ts` y `output-parser.ts`; comparar contrato válido, ausencia de decisión y JSON malformado |
| 08 y 10b | Reconstruir una traza del simulador y distinguir error de modelo, estado, cola o integración |
| 11b y 12d | Medir costo por tarea y tiempo de revisión; distinguir cobros profesionales de ingresos por suscripción al software |

No se verificó un ciclo completo de suscripciones recurrentes al SaaS. Encontrar cobros de pacientes, OAuth de Mercado Pago o un precio en la landing no acredita ese ciclo. Registrarlo como «por verificar», no como función ausente ni terminada.

## Comandos y precauciones

Los comandos siguientes pertenecen al repositorio del SaaS, no a IARoadmap. Los comandos Python del README de IARoadmap validan material curricular; no compilan TypeScript ni prueban esta aplicación.

Preparar una copia de aprendizaje con Node compatible, leer los scripts y usar dependencias fijadas:

```bash
npm ci
npm --prefix web ci
npm run typecheck
npm --prefix web run typecheck
npm test -- src/modules/appointments/__tests__/weekly-schedule.test.ts
npm test -- src/modules/brain/__tests__/output-parser.test.ts
```

`typecheck` raíz cubre el servidor; el de `web` comprueba el frontend. La prueba del parser usa mocks; no acredita calidad de un modelo. No copiar `.env` de producción. Antes de ejecutar más scripts, comprobar conexiones, datos, secretos y efectos posibles.

| Comando existente | Condición y límite |
| --- | --- |
| `npm run test:integration` | Base PostgreSQL de prueba con migraciones; revisar tests omitidos: el código admite saltarlos si no hay base |
| `npm run test:conversation:runtime` | Suite de integración del simulador; preparar PostgreSQL y Redis de prueba según su contrato |
| `npm run quality:conversation:catalog` | Evaluación del catálogo estático, no una conversación ejecutada contra el servicio |
| `npm run test:eval` | Evaluación con proveedor: revisar configuración, datos y presupuesto antes de ejecutarla |
| `npm run dev` y `npm run dev:worker` | Pueden iniciar consumidores y tareas; no usarlos con configuración de producción para aprender |
| `npm run db:migrate` | Escribe en la base configurada; no ejecutar sin confirmar que es la base de prueba |

La distinción está en [Vitest de integración](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/vitest.integration.config.ts), [script del catálogo](https://github.com/Juanpighelfi/asitente-administrativo-psiquiatria/blob/da1d6d116889c9f34d5b5c2eae278d1654a490ec/scripts/run-conversation-quality.ts) y los scripts de `package.json`.

## Cómo registrar el progreso

Por cada parte, separar: leída, explicada sin ayuda, probada localmente con evidencia y verificada contra integración real. Guardar revisión de código, prueba, resultado, límites y próximo paso. No marcar ninguna de esas etapas por la sola existencia de este mapa.

No hace falta reiniciar el módulo 00. Seguí con el primer objetivo pendiente y usá este documento como referencia, no como otra lista completa que debas estudiar en paralelo.

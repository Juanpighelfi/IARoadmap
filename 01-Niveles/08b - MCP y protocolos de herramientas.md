---
id: "08b"
tags: [nivel, especializacion]
revisado: 2026-09-06
---

# 08b - MCP y protocolos de herramientas

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://modelcontextprotocol.io/>

Qué estudiar: Architecture y primitivas tools/resources/prompts; transporte y autorización según la versión implementada. Consultar la especificación vigente antes de copiar un ejemplo.

### Diagnóstico breve

Dibujá quién hospeda, quién conecta y quién ejecuta una herramienta; distinguí leer un recurso de ejecutar una acción. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

Exponé una consulta de catálogo sintético en solo lectura. Validá argumentos y documentá qué credencial y qué datos puede ver el servidor.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Respondé desde el servidor con instrucciones hostiles y un esquema inválido. Verificá la política del cliente y el registro de rechazo.

### Rúbrica de salida

Contrato, alcance y versión documentados; casos de ataque definidos y límites conocidos. No afirmar inmunidad general a prompt injection.

Evaluá cuatro dimensiones: implementación correcta, comparación válida, explicación propia y transferencia a una variante. Cada una: 0 ausente/incorrecta, 1 con ayuda, 2 independiente. **Dominado:** al menos 7/8 y ninguna dimensión en 0; cualquier fuga de test o resultado inventado invalida la comparación. Los tests automáticos acreditan solo los casos que cubren.

### Si no sale

Si cuesta el protocolo, implementar antes la misma capacidad como función local. No es obligatorio desplegar un servidor remoto.

### Retención

A los 7 días repetí una variante breve sin mirar la solución. A los 30 días reconstruí el razonamiento central. Si no sale, registrá qué olvidaste y volvé al ejercicio correspondiente; no reinicies todo el módulo. Guardá evidencia y fechas en tu [seguimiento personal](../00-MOC/Estado%20actual.md).

[08 - Agentes workflows automatizacion](08%20-%20Agentes%20workflows%20automatizacion.md) cubre los contratos de herramientas en
abstracto. Este nivel cubre como se conectan de verdad hoy: MCP (Model Context
Protocol) es el estandar abierto que se volvio la forma comun de exponer datos y
acciones a un modelo, sin escribir una integracion a medida por cada par
modelo-herramienta.

Vale la pena aunque no vayas a usar MCP: el protocolo obliga a pensar en permisos,
descubrimiento y limites de una herramienta, que es exactamente lo que hay que
disenar bien.

## Debes aprender

- El problema que resuelve: integraciones N x M entre modelos y sistemas, y por que
  cada framework de agentes reinventaba lo mismo.
- Arquitectura: host, cliente y servidor. Quien inicia, quien autoriza, quien ejecuta.
- Primitivas: **tools** (acciones que el modelo puede invocar), **resources** (datos
  que puede leer) y **prompts** (plantillas que el usuario puede elegir). Cuando algo
  es un recurso y no una herramienta, y por que confundirlos ensucia el contexto.
- Transporte: stdio local frente a HTTP remoto, y que implica cada uno para seguridad.
- Diseno de servidores: granularidad de las herramientas, descripciones que el modelo
  pueda entender, esquemas de entrada estrictos, errores utiles, idempotencia.
- Costo en contexto: las definiciones de herramientas incluidas en el contexto consumen tokens; el efecto depende del cliente, carga selectiva y caché. Evaluá el costo de cargar muchas herramientas y si su selección compensa la complejidad. Conecta con
  [06b - Context engineering](06b%20-%20Context%20engineering.md).
- Seguridad: consentimiento del usuario, alcance de credenciales, servidores de
  terceros como superficie de ataque, herramientas destructivas, inyeccion de prompt a
  traves del contenido que devuelve un servidor. Conecta con
  [10 - Evaluacion seguridad gobernanza](10%20-%20Evaluacion%20seguridad%20gobernanza.md).
- Alternativas y complementos: tool calling directo del proveedor, OpenAPI como fuente
  de herramientas, y cuando un simple cliente HTTP alcanza.

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Escribir un servidor MCP propio que exponga una capacidad real tuya: tu base de
  datos en solo lectura, tus notas, o una API interna. Con esquemas estrictos y
  errores descriptivos.
- Conectarlo a un cliente y registrar cada llamada: argumentos, resultado, latencia,
  tokens consumidos.
- Escribir el modelo de permisos por escrito: que herramienta puede escribir, cual
  requiere confirmacion humana, cual no deberia existir.
- Red team de tu propio servidor: que pasa si el contenido devuelto trae instrucciones
  para el modelo. Documentar la mitigacion.
- Medir el costo en tokens de exponer 5 herramientas frente a 20, y disenar una
  estrategia de carga selectiva.

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Especificacion de MCP: <https://modelcontextprotocol.io/>
- SDKs y ejemplos: <https://github.com/modelcontextprotocol>
- Anthropic, Building effective agents:
  <https://www.anthropic.com/engineering/building-effective-agents>
- OWASP Top 10 for LLM Applications:
  <https://owasp.org/www-project-top-10-for-large-language-model-applications/>

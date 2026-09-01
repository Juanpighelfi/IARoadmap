---
tags:
  - nivel
  - mcp
  - herramientas
  - integraciones
duracion: 2-4 semanas
estado: pendiente
inicio:
fin:
---

# 08b - MCP y protocolos de herramientas

[[08 - Agentes workflows automatizacion]] cubre los contratos de herramientas en
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
- Costo en contexto: cada herramienta expuesta ocupa tokens en cada llamada. Veinte
  herramientas cargadas siempre es un problema de diseno, no una feature. Conecta con
  [[06b - Context engineering]].
- Seguridad: consentimiento del usuario, alcance de credenciales, servidores de
  terceros como superficie de ataque, herramientas destructivas, inyeccion de prompt a
  traves del contenido que devuelve un servidor. Conecta con
  [[10 - Evaluacion seguridad gobernanza]].
- Alternativas y complementos: tool calling directo del proveedor, OpenAPI como fuente
  de herramientas, y cuando un simple cliente HTTP alcanza.

## Practica

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

## Criterio de salida

Podes exponer una capacidad real como servidor, explicar por que cada herramienta
tiene el alcance que tiene, y mostrar que un servidor hostil no puede tomar el control
de tu agente.

## Recursos

- Especificacion de MCP: <https://modelcontextprotocol.io/>
- SDKs y ejemplos: <https://github.com/modelcontextprotocol>
- Anthropic, Building effective agents:
  <https://www.anthropic.com/engineering/building-effective-agents>
- OWASP Top 10 for LLM Applications:
  <https://owasp.org/www-project-top-10-for-large-language-model-applications/>

## Siguiente

- [[09 - Multimodalidad]]
- [[10 - Evaluacion seguridad gobernanza]]

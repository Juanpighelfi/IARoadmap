---
tags:
  - nivel
  - herramientas
  - productividad
  - agentic-coding
duracion: 2-4 semanas
estado: pendiente
inicio:
fin:
---

# 01b - Ingenieria asistida por IA

Transversal. Se aprende una vez, temprano, y multiplica todos los niveles siguientes.
No es "usar ChatGPT para programar": es aprender a dirigir, revisar y acotar a un
agente que escribe codigo en tu repo.

Va despues de [[01 - Computacion Python Git y entorno]] a proposito. Antes de saber
Git, tests y estructura de proyecto, un asistente de codigo acelera la produccion de
codigo que no podes evaluar, que es la peor combinacion posible.

## Debes aprender

- Herramientas de codigo agentico: que hacen, que ven de tu repo, que pueden ejecutar.
- Contexto del repo: por que un `AGENTS.md` o `CLAUDE.md` con convenciones, comandos de
  build y estilo cambia por completo la calidad de la salida.
- Desarrollo dirigido por especificacion: escribir el criterio de aceptacion y los tests
  antes de pedir la implementacion.
- Tamano de tarea: por que "refactoriza este modulo" funciona y "construi la app"
  no; como cortar trabajo en unidades revisables.
- Revision de codigo generado: leerlo como si viniera de un desconocido apurado.
  Buscar dependencias inventadas, manejo de errores ausente, casos borde ignorados.
- Cuando no usarlo: codigo que no entendes y no vas a poder mantener, y ejercicios de
  aprendizaje donde la friccion es el punto.
- Higiene: secretos fuera del contexto, permisos de herramientas, revisar diffs antes
  de commitear, no dejar que un agente toque `main`.

## Practica

- Configurar el archivo de contexto de tu repo con comandos, convenciones y limites.
  Medir la diferencia en calidad antes y despues sobre la misma tarea.
- Tomar una tarea real de tu proyecto y hacerla dos veces: a mano y dirigida. Comparar
  tiempo, cantidad de defectos encontrados en revision y cuanto entendes del resultado
  una semana despues.
- Escribir el criterio de aceptacion y los tests de una feature, y recien despues pedir
  la implementacion. Que los tests sean los que digan si esta terminada.
- Revisar un diff generado de 200+ lineas y anotar cada cosa que corregiste. Esa lista
  es tu mapa de en que no confiar.

## Criterio de salida

Podes delegar una tarea acotada, revisar el diff con criterio y explicar cada linea
del resultado. Y sabes nombrar tres tipos de tarea donde delegar te sale mas caro
que hacerlo a mano.

## Advertencia

Este nivel tiene un modo de fallo propio: sentir que aprendiste porque el codigo
funciona. El criterio de salida de todos los demas niveles sigue siendo tuyo, no del
asistente. Si no podes reimplementar a mano lo esencial de lo que entregaste, no
cumpliste el nivel. Ver [[04-Recursos/Anti-roadmap]].

## Recursos

- Claude Code docs: <https://docs.claude.com/en/docs/claude-code/overview>
- Cursor docs: <https://docs.cursor.com/>
- GitHub Copilot docs: <https://docs.github.com/en/copilot>
- Anthropic, Claude Code best practices:
  <https://www.anthropic.com/engineering/claude-code-best-practices>
- Simon Willison sobre programar con LLMs:
  <https://simonwillison.net/2025/Mar/11/using-llms-for-code/>

## Siguiente

- [[02 - Datos SQL visualizacion y estadistica]]
- [[06 - LLMs aplicados]]

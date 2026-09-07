---
id: "01b"
tags: [nivel, transversal]
revisado: 2026-09-06
---

# 01b - Ingenieria asistida por IA

## Cómo cursarlo

Consultá el [catálogo de módulos](../00-MOC/Catalogo%20de%20modulos.md) para los prerrequisitos y el rango de horas de este módulo. Las horas incluyen lectura seleccionada, práctica, corrección y primer repaso; no son una promesa de dominio ni se suman a cursos completos. El ID conserva enlaces históricos y no impone orden.

**Recurso principal:** <https://docs.github.com/en/copilot>

Qué estudiar: Conceptos de asistencia de código, revisión y uso responsable. Elegir el asistente disponible; no contratar otro para cursar.

### Diagnóstico breve

Explicá un diff de 30 líneas: identificá entrada, salida, efectos secundarios y cómo probarías un error. Si lo resolvés sin ayuda y lo justificás, intentá directamente la tarea independiente; omitir lectura exige evidencia, no autopercepción.

### Práctica guiada

En tu ruta personal, pedí una variante acotada de la función de horarios del 01, vinculada al [SaaS real](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md). En el camino Python, usá la CLI del laboratorio. Escribí antes tres criterios de aceptación, revisá el diff y ejecutá los tests.

Los laboratorios numerados están en el [índice ejecutable](../07-Laboratorios/README.md). Para los demás ejercicios, la consigna de esta página es la práctica; las referencias amplían el procedimiento.

### Práctica independiente

Una semana después, implementá sin IA una variante de la función modificada y compará tus decisiones.

### Cómo comprobar que aprendí

Conservar especificación, diff revisado, pruebas y lista de correcciones. Separar lo que hizo el asistente de lo que podés explicar y reconstruir.

Comprobá que podés resolver el ejercicio, explicar el resultado y hacer una variante sin copiar. No hace falta puntuarte ni completar otra plantilla. Se mantienen los criterios técnicos anteriores: no inventar resultados ni usar datos de evaluación para ajustar la solución. Los tests solo comprueban los casos que cubren.

### Si no sale

Si el código funciona pero no podés modificarlo, volver al 01 y usar al asistente solo para pistas y preguntas.

### Retención

Cada tanto, retomá una variante sin mirar la solución. Si no sale, anotá ese punto como próximo ejercicio en [Mi seguimiento](../00-MOC/Estado%20actual.md), sin otra planilla ni fechas obligatorias. No hace falta reiniciar el módulo.

Transversal. Se aprende una vez, temprano, y multiplica todos los niveles siguientes.
No es "usar ChatGPT para programar": es aprender a dirigir, revisar y acotar a un
agente que escribe codigo en tu repo.

Va despues de [01 - Programación, Git y entorno](01%20-%20Computacion%20Python%20Git%20y%20entorno.md) a proposito. Antes de saber
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

## Práctica adicional opcional

La práctica guiada y la variante de arriba constituyen el ciclo principal. Elegí una de estas extensiones solo si aporta; no se suman todas al rango de horas.

- Configurar el archivo de contexto de tu repo con comandos, convenciones y limites.
  Medir la diferencia en calidad antes y despues sobre la misma tarea.
- Tomar una tarea real de tu proyecto y hacerla dos veces: a mano y dirigida. Comparar
  tiempo, cantidad de defectos encontrados en revision y cuanto entendes del resultado
  una semana despues.
- Escribir el criterio de aceptacion y los tests de una feature, y recien despues pedir
  la implementacion. Que los tests sean los que digan si esta terminada.
- Revisar un diff generado de 200+ lineas y anotar cada cosa que corregiste. Esa lista
  es tu mapa de en que no confiar.

## Advertencia

Este nivel tiene un modo de fallo propio: sentir que aprendiste porque el codigo
funciona. El criterio de salida de todos los demas niveles sigue siendo tuyo, no del
asistente. Si no podes reimplementar a mano lo esencial de lo que entregaste, no
cumpliste el nivel. Ver [Anti-roadmap](../04-Recursos/Anti-roadmap.md).

## Referencias adicionales

Consulta estas fuentes solo si el recurso principal no alcanza; no son una lista de cursos obligatorios.

- Claude Code docs: <https://docs.claude.com/en/docs/claude-code/overview>
- Cursor docs: <https://docs.cursor.com/>
- GitHub Copilot docs: <https://docs.github.com/en/copilot>
- Anthropic, Claude Code best practices:
  <https://www.anthropic.com/engineering/claude-code-best-practices>
- Simon Willison sobre programar con LLMs:
  <https://simonwillison.net/2025/Mar/11/using-llms-for-code/>

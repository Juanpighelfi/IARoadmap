---
tags:
  - ruta
  - producto
  - fundador
---

# Si estas construyendo un producto

Para quien ya tiene un producto en marcha, o una idea concreta, y quiere aprender IA
sin frenar el producto. Es la ruta con mas riesgo de fracaso silencioso: estudiar por un
lado y construir por otro, pagando dos veces por el mismo aprendizaje.

## Regla de la ruta

**Cada nivel se cierra contra tu producto, no contra un ejercicio.** El criterio de
salida se cumple cuando lo aplicaste a algo que un usuario real va a tocar. Y el
[[03-Proyectos/Capstone]] no es un proyecto aparte: es tu producto, documentado con el
rigor que pide el capstone.

Esto acorta el plan a la mitad. Tambien lo hace mas dificil, porque un producto real
tiene usuarios, datos sucios y consecuencias.

## Orden recomendado

1. [[01-Niveles/00 - Orientacion y alfabetizacion en IA]], rapido.
2. [[01-Niveles/01 - Computacion Python Git y entorno]], si te falta base de software.
3. [[01-Niveles/01b - Ingenieria asistida por IA]]. Temprano: es lo que te devuelve
   horas para todo lo demas.
4. [[01-Niveles/06 - LLMs aplicados]] y [[01-Niveles/06b - Context engineering]].
5. [[01-Niveles/10 - Evaluacion seguridad gobernanza]], **antes** de escalar el uso.
   Fuera de orden a proposito: sin evals no vas a saber si tus cambios mejoran algo, y
   con usuarios reales ese no saber cuesta caro.
6. [[01-Niveles/07 - RAG busqueda embeddings]], si tu producto responde sobre
   documentos o datos propios.
7. [[01-Niveles/08 - Agentes workflows automatizacion]] y
   [[01-Niveles/08b - MCP y protocolos de herramientas]], si el producto ejecuta
   acciones y no solo responde.
8. [[01-Niveles/10b - Error analysis y evals desde trazas]], en cuanto tengas trafico
   real. Este es el nivel que mas rinde con producto en marcha y no se puede hacer sin el.
9. [[01-Niveles/11 - MLOps LLMOps despliegue]] y
   [[01-Niveles/11b - Inferencia costos y economia unitaria]].
10. [[01-Niveles/02 - Datos SQL visualizacion y estadistica]] y
    [[01-Niveles/04 - Machine learning clasico]], cuando aparezca un problema que los
    pida de verdad: prediccion, segmentacion, deteccion.
11. [[01-Niveles/12b - Capa profesional]], en paralelo desde el principio.

Fundamentos pesados ([[01-Niveles/03 - Matematicas para ML]],
[[01-Niveles/05 - Deep learning y PyTorch]], [[01-Niveles/05b - Post-training aplicado]])
quedan para cuando el producto los necesite o cuando quieras cambiar de perfil. No los
tachas: los aplazas con motivo escrito en [[00-MOC/Estado actual]].

## Que aplicar de cada nivel a tu producto

| Nivel | Que sale de aca para tu producto |
| --- | --- |
| 01b Ingenieria asistida por IA | Contexto del repo configurado, revision de diffs, y tiempo recuperado |
| 06 LLMs aplicados | Salidas estructuradas y validadas donde hoy hay texto libre; eleccion de modelo con criterio |
| 06b Context engineering | Presupuesto de tokens por llamada; politica de memoria del usuario escrita |
| 07 RAG | Respuestas con cita a tu documentacion; y saber no responder |
| 08 y 08b Agentes y MCP | Acciones con permisos explicitos, confirmacion humana y log de auditoria |
| 09 Multimodalidad | Extraccion de documentos y audio con validacion, si tu flujo los tiene |
| 10 Evals y gobernanza | Suite de regresion que corre antes de cada deploy; registro de riesgos |
| 10b Error analysis | Taxonomia de fallas reales de tus usuarios, con frecuencia y prioridad |
| 11 MLOps | Deploy con health checks, rollback y tablero |
| 11b Inferencia y costos | Costo por tarea y p95 medidos; margen que cierra |
| 12b Capa profesional | Un texto publico por mes; el producto como carta de presentacion |

## Si tu dominio es sensible

Salud, finanzas, legal, educacion o empleo cambian el orden de prioridades. Lee
[[04-Recursos/Regulacion y cumplimiento]] **antes** de conectar datos reales, no
despues del primer usuario.

Lo minimo, en este orden:

1. Que dato personal entra al prompt y si hace falta que entre. Casi siempre se puede
   trabajar con menos del que uno supone.
2. Que retiene el proveedor del modelo y donde se procesa.
3. Que queda en logs y trazas, quien accede, cuando se borra.
4. Como borras a una persona del sistema entero, indices vectoriales incluidos.
5. Que decision **nunca** toma el sistema solo, escrito y visible para el usuario.
6. Supervision humana con tiempo y poder real de rechazar, no un boton de confirmar.
7. Evals segmentados: el promedio esconde el desempeno en el grupo de mas riesgo.

Y una regla de producto que no es tecnica: en un dominio de alto riesgo, la version
util no es la que decide, es la que prepara la decision y la deja revisada en dos
minutos en lugar de veinte.

## Advertencia

El modo de fallo de esta ruta es al reves que el de las otras. En las demas se estudia
de mas y se construye de menos; aca se construye de mas y no se consolida nada.
Antidoto: la [[06-Bitacora/Como usar la bitacora|bitacora]] y los criterios de salida.
Si en tres meses no cerraste ningun nivel, no estas estudiando, estas trabajando y
diciendote que estudias.

## Primer proyecto sugerido

El que ya tenes. Elegi el flujo mas repetido y de menor riesgo de tu producto, y
llevalo al estandar completo: salida estructurada validada, 50 casos de eval, trazas,
costo por tarea medido, y un limite escrito de lo que no hace. Documentado con
[[05-Plantillas/Plantilla de proyecto]], ese flujo ya es tu capstone.

# Capstone personal

Consolidá el proyecto que ya trabajaste. Para la ruta principal, usá el [SaaS administrativo con IA](SaaS%20administrativo%20con%20IA.md): un flujo pequeño comprendido, probado y recuperable, con una comparación que justifique incorporar IA o conservar reglas. Para visión opcional, usá [inspección de piezas](Inspeccion%20visual%20de%20piezas.md); para investigación, una reproducción acotada. El cierre académico no requiere clientes; la validación comercial se documenta aparte.

## Entrega

| Criterio | Evidencia requerida |
| --- | --- |
| Problema | Entrada, salida, usuario previsto y límites |
| Datos | Procedencia, permisos y tamaño; casos sintéticos identificados y conjunto reservado para la evaluación de IA |
| Método | Baseline y alternativa con justificación |
| Evaluación | Conjunto reservado, métricas por segmento y limitaciones |
| Reproducibilidad | Código, versiones, configuración, datos de prueba y comandos; semilla si corresponde |
| Operación | Tiempo/memoria/costo medidos si se ejecuta; rollback o recuperación local |
| Aprendizaje | Error investigado, cambio medido y una variante resuelta sin ayuda |

Puntuá cada criterio 0 (ausente/incorrecto), 1 (parcial) o 2 (completo y comprobable). Cierre: al menos 12/14, sin cero en datos, evaluación o reproducibilidad. Un sistema que no supera el baseline puede aprobar si el experimento y la conclusión son válidos. Una demo sin evidencia queda como prototipo.

Las trazas pueden venir de tu uso personal o de pruebas diseñadas; identificá su origen. No afirmar que un sistema tiene usuarios, cumple una norma o funciona en hardware que no se probó.

## Requisitos adicionales del SaaS

Para cerrar el capstone de esta ruta, demostrar aislamiento entre dos cuentas, persistencia, evento duplicado sin efecto repetido, fallo diagnosticado y restauración ensayada. Un error de acceso a datos ajenos o acción no autorizada bloquea el cierre aunque el puntaje global alcance. El piloto comercial requiere además las condiciones del proyecto conductor; una buena autoevaluación no demuestra uso real ni pago.

## Defensa individual

Sin abrir el código: explicar tres decisiones y una limitación. Después, modificar una condición del problema y predecir el efecto antes de ejecutar. Repetir al mes usando solo el README. Si no podés reproducir, corregir documentación o comprensión y registrar el resultado.

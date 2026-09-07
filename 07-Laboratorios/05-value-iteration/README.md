# Laboratorio 05: Decisión secuencial con value iteration

## Consigna

Implementa iteración de valores para un MDP tabular estocástico. `terminals` es un conjunto: todo terminal conserva `V=0` y no tiene acciones. La recompensa de éxito o fallo está en la transición que entra al terminal. Cada resultado es `(probabilidad, siguiente_estado, recompensa)`. Valida el modelo y los parámetros; si no alcanza `tol` en `max_iterations`, falla explícitamente.

Copia `starter.py` a `Mi-progreso/labs/` (excluida por Git) y trabaja allí. No mires `solucion.py` hasta completar un intento comprobable.

## Datos sintéticos

Los datos están explícitos en el archivo CSV del laboratorio o en los ejemplos literales de las pruebas. Son pequeños y artificiales: sirven para comprobar lógica, no rendimiento real.

## Pistas

Copia valores para cada barrido (actualización síncrona). Calcula `Σp(r+γV(s’))` por acción y elige el máximo.

## Evaluación

Desde la raíz, reemplaza la ruta por tu archivo:

```bash
LAB05_PATH=/ruta/privada/mi_solucion.py python -m unittest discover -s 07-Laboratorios -p 'test_lab05.py'
```

## Transferencia manual

Cambia la probabilidad de éxito de `intentar` en el estado `riesgo`, manteniendo la suma en 1. Observa la política en `riesgo` e `inicio` para varios valores y explica cualquier cambio; no presupongas que existe un umbral en el intervalo probado. Explica también el efecto de `gamma`.

**Criterio:** solución correcta en un caso nuevo y explicación escrita de cada decisión sin copiar la referencia.

## Recuperación y repaso

Si terminales cambian o no converge, repasa Bellman y suma de probabilidades; realiza dos barridos manuales y reintenta en 72 h.

La referencia está en `solucion.py`; `EXPLICACION.md` explica sus decisiones.

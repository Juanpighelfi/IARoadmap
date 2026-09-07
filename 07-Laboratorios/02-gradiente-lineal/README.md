# Laboratorio 02: Gradiente de regresión lineal

## Consigna

Implementa MSE, los gradientes analíticos de `ŷ=w*x+b` y descenso por gradiente. `fit` devuelve `(w, b, historial)` con pérdida inicial y una entrada por paso. Verifica a mano el gradiente para `x=[1,2]`, `y=[3,5]`, `w=b=0`.

Copia `starter.py` a `Mi-progreso/labs/` (excluida por Git) y trabaja allí. No mires `solucion.py` hasta completar un intento comprobable.

## Datos sintéticos

Los datos están explícitos en el archivo CSV del laboratorio o en los ejemplos literales de las pruebas. Son pequeños y artificiales: sirven para comprobar lógica, no rendimiento real.

## Pistas

Derivadas: `dw=2/n Σ(ŷ-y)x`, `db=2/n Σ(ŷ-y)`. Actualiza ambos con los gradientes del mismo estado.

## Evaluación

Desde la raíz, reemplaza la ruta por tu archivo:

```bash
LAB02_PATH=/ruta/privada/mi_solucion.py python -m unittest discover -s 07-Laboratorios -p 'test_lab02.py'
```

## Transferencia manual

Prueba `y=-3x+2` con valores negativos; elige una tasa que converja y justifícala con el historial.

**Criterio:** solución correcta en un caso nuevo y explicación escrita de cada decisión sin copiar la referencia.

## Recuperación y repaso

Si el gradiente manual o la pérdida no coinciden, repasa derivadas y promedio; recalcula tres iteraciones en papel y reintenta en 48 h.

La referencia está en `solucion.py`; `EXPLICACION.md` explica sus decisiones.

# Laboratorio 01: Python, CSV y validación de piezas 3D

## Consigna

Implementa `validate_rows(rows)` y `read_and_validate(path)`. Normaliza espacios y material, convierte cuatro medidas a `float`, acepta PLA/PETG/ABS y separa filas válidas de reportes `{fila, errores}`. Rechaza ID vacío/duplicado y números no positivos o no finitos. Usa `piezas.csv`.

Copia `starter.py` a `Mi-progreso/labs/` (excluida por Git) y trabaja allí. No mires `solucion.py` hasta completar un intento comprobable.

## Datos sintéticos

Los datos están explícitos en el archivo CSV del laboratorio o en los ejemplos literales de las pruebas. Son pequeños y artificiales: sirven para comprobar lógica, no rendimiento real.

## Pistas

Recorre con `enumerate(rows, 2)`; conserva un `set` de IDs aceptados; `math.isfinite` cubre NaN e infinito.

## Evaluación

Desde la raíz, reemplaza la ruta por tu archivo:

```bash
LAB01_PATH=/ruta/privada/mi_solucion.py python -m unittest discover -s 07-Laboratorios -p 'test_lab01.py'
```

## Transferencia manual

Crea otro CSV con columnas en distinto orden y una medida `inf`; explica qué filas admitirías antes de ejecutar.

**Criterio:** solución correcta en un caso nuevo y explicación escrita de cada decisión sin copiar la referencia.

## Recuperación y repaso

Si fallan 2 o más casos, repasa `csv.DictReader`, excepciones y conjuntos; corrige y repite al día siguiente.

La referencia está en `solucion.py`; `EXPLICACION.md` explica sus decisiones.

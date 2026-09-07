# Laboratorio 04: Partición por pieza y por tiempo

## Consigna

Implementa una división reproducible que mantenga todas las fotos de una pieza juntas, una división temporal por fecha ISO y un detector de piezas compartidas. Usa `fotos.csv`. Esto evalúa partición, no entrena ni afirma métricas de ML.

Copia `starter.py` a `Mi-progreso/labs/` (excluida por Git) y trabaja allí. No mires `solucion.py` hasta completar un intento comprobable.

## Datos sintéticos

Los datos están explícitos en el archivo CSV del laboratorio o en los ejemplos literales de las pruebas. Son pequeños y artificiales: sirven para comprobar lógica, no rendimiento real.

## Pistas

Baraja IDs únicos con `random.Random(seed)`, no filas. Las fechas ISO `AAAA-MM-DD` ordenan, pero `date.fromisoformat` valida.

## Evaluación

Desde la raíz, reemplaza la ruta por tu archivo:

```bash
LAB04_PATH=/ruta/privada/mi_solucion.py python -m unittest discover -s 07-Laboratorios -p 'test_lab04.py'
```

## Transferencia manual

Añade diez fotos desbalanceadas de una sola pieza; compara porcentaje de filas y de piezas, y argumenta cuál informa el riesgo real.

**Criterio:** solución correcta en un caso nuevo y explicación escrita de cada decisión sin copiar la referencia.

## Recuperación y repaso

Si aparece una pieza en ambos conjuntos, repasa unidad de independencia y agrupa antes de dividir; reconstruye la partición con tarjetas y repite.

La referencia está en `solucion.py`; `EXPLICACION.md` explica sus decisiones.

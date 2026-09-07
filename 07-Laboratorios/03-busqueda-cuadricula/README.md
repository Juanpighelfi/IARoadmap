# Laboratorio 03: BFS y A* en una cuadrícula

## Consigna

Implementa caminos mínimos con movimientos ortogonales. La cuadrícula usa `(fila, columna)`, límites `rows × cols`, y `blocked` es un conjunto. Devuelve la lista completa de inicio a meta o `None`; valida extremos.

Copia `starter.py` a `Mi-progreso/labs/` (excluida por Git) y trabaja allí. No mires `solucion.py` hasta completar un intento comprobable.

## Datos sintéticos

Los datos están explícitos en el archivo CSV del laboratorio o en los ejemplos literales de las pruebas. Son pequeños y artificiales: sirven para comprobar lógica, no rendimiento real.

## Pistas

BFS usa cola y marca al descubrir. A* usa prioridad `g + Manhattan`; guarda padre y mejora costos.

## Evaluación

Desde la raíz, reemplaza la ruta por tu archivo:

```bash
LAB03_PATH=/ruta/privada/mi_solucion.py python -m unittest discover -s 07-Laboratorios -p 'test_lab03.py'
```

## Transferencia manual

Dibuja una cuadrícula 6×6 con dos rutas posibles; predice longitud y compara BFS/A*. Explica cuándo A* exploraría menos.

**Criterio:** solución correcta en un caso nuevo y explicación escrita de cada decisión sin copiar la referencia.

## Recuperación y repaso

Si el camino no es continuo o mínimo, repasa reconstrucción y momento de marcar visitados; resuelve una cuadrícula 3×3 a mano y repite.

La referencia está en `solucion.py`; `EXPLICACION.md` explica sus decisiones.

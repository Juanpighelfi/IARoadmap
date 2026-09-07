# Hardware y presupuesto

La ruta no presupone una GPU dedicada ni un modelo concreto de computadora. No compres hardware para empezar: los laboratorios incluidos usan Python estándar y CPU.

| Etapa | Entorno inicial | Cuándo ampliar |
| --- | --- | --- |
| Python, matemáticas, búsqueda y MDP | Python 3.11+ y biblioteca estándar | No requiere GPU |
| ML tabular | CPU, entorno con NumPy/scikit-learn | Si una medición demuestra que el tamaño lo necesita |
| DL y visión | Dataset pequeño, modelo reducido o cabeza congelando el backbone | Cuando el experimento ya funciona y el tiempo es el límite |
| Modelos de lenguaje locales | Modelo que quepa en la RAM/VRAM disponible | Después de medir calidad, contexto y memoria |
| Robótica | Simulación 2D | Hardware físico solo tras validar el bucle y elegir proyecto |

## Ficha previa a cada experimento

Anotá CPU/GPU, RAM/VRAM, sistema operativo, versión del runtime, modelo y licencia, almacenamiento necesario, límite de tiempo y presupuesto máximo autorizado por vos. Si no hay presupuesto definido, elegí una versión sin gasto.

Memoria mínima de pesos ≈ parámetros × bits por parámetro / 8. A eso se agregan activaciones, caché, buffers y overhead; para entrenamiento también gradientes y estado del optimizador. El cálculo no garantiza que el proceso quepa.

Compará calidad, latencia y memoria con el mismo conjunto de tareas. Los precios de API/nube cambian: consultá al proveedor antes de ejecutar y fijá límites; el repo no fija precios ni contrata servicios. Guardá el costo observado, distinguiendo descarga, preparación, entrenamiento e inferencia.

Si dependés de un entorno temporal, respaldá código, configuración y checkpoints fuera de ese entorno. Los datos locales de `Mi-progreso/` no quedan respaldados por este repositorio automáticamente.

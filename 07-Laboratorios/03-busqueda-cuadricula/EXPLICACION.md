# Explicación de referencia

## API y contrato

`bfs` y `astar` reciben dimensiones, obstáculos, inicio y meta. Devuelven una lista continua que incluye ambos extremos, con movimientos ortogonales, o `None` si no existe ruta. Con costos unitarios, ambos deben devolver una ruta mínima.

## Ejemplo paso a paso

En una cuadrícula 2×2 sin obstáculos, desde `(0,0)` hasta `(1,1)`, BFS descubre los vecinos a distancia 1 y luego la meta a distancia 2. El diccionario `parents` permite reconstruir `[(0,0),(0,1),(1,1)]` o la alternativa igualmente óptima. A* prioriza `g + h`; Manhattan vale 2 al inicio y nunca sobreestima pasos ortogonales.

## Decisiones y bordes

BFS marca una celda al descubrirla para no encolarla varias veces. A* conserva el mejor costo conocido y actualiza padre si lo mejora. `inicio == meta` produce una lista de un elemento. Extremos fuera de límites o bloqueados son errores de entrada; una meta aislada es un resultado válido `None`.

## Errores y complejidad

Sea V el número de celdas libres y E sus adyacencias. BFS cuesta O(V+E). A* cuesta O((V+E) log V) con heap; puede explorar menos celdas gracias a la heurística. Padres y costos usan O(V).

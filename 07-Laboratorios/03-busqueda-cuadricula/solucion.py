"""Búsqueda de caminos con BFS y A* en una cuadrícula rectangular."""
from collections import deque
from heapq import heappop, heappush


def _validate_grid(rows, cols, blocked, start, goal):
    if rows <= 0 or cols <= 0:
        raise ValueError("las dimensiones deben ser positivas")
    for point in (start, goal):
        row, col = point
        if not (0 <= row < rows and 0 <= col < cols) or point in blocked:
            raise ValueError("inicio y meta deben ser celdas libres dentro de la cuadrícula")


def _neighbors(point, rows, cols, blocked):
    row, col = point
    for candidate in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
        if 0 <= candidate[0] < rows and 0 <= candidate[1] < cols and candidate not in blocked:
            yield candidate


def _reconstruct(parents, goal):
    if goal not in parents:
        return None
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    return list(reversed(path))


def bfs(rows, cols, blocked, start, goal):
    """Devuelve un camino mínimo ortogonal, o None si la meta es inalcanzable."""
    _validate_grid(rows, cols, blocked, start, goal)
    frontier = deque([start])
    parents = {start: None}
    while frontier:
        current = frontier.popleft()
        if current == goal:
            break
        for neighbor in _neighbors(current, rows, cols, blocked):
            if neighbor not in parents:
                parents[neighbor] = current
                frontier.append(neighbor)
    return _reconstruct(parents, goal)


def astar(rows, cols, blocked, start, goal):
    """Devuelve un camino mínimo usando costo unitario y distancia Manhattan."""
    _validate_grid(rows, cols, blocked, start, goal)
    frontier = [(0, start)]
    parents = {start: None}
    costs = {start: 0}
    while frontier:
        _, current = heappop(frontier)
        if current == goal:
            break
        for neighbor in _neighbors(current, rows, cols, blocked):
            new_cost = costs[current] + 1
            if new_cost < costs.get(neighbor, float("inf")):
                costs[neighbor] = new_cost
                parents[neighbor] = current
                heuristic = abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                heappush(frontier, (new_cost + heuristic, neighbor))
    return _reconstruct(parents, goal)

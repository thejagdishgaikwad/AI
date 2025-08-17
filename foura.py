import heapq

def a_star(start, goal, neighbors_fn, h_fn):
    """
    A* pathfinding algorithm.

    Args:
        start: starting node (tuple, int, etc.)
        goal: target node
        neighbors_fn: function(node) -> list of (neighbor, cost)
        h_fn: heuristic function(node) -> estimated cost to goal

    Returns:
        path (list), cost (int/float)
    """
    # Priority queue (f, g, node, path)
    open_set = [(h_fn(start), 0, start, [start])]
    visited = {}

    while open_set:
        f, g, node, path = heapq.heappop(open_set)

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        if node == goal:
            return path, g

        for neighbor, cost in neighbors_fn(node):
            g2 = g + cost
            f2 = g2 + h_fn(neighbor)
            heapq.heappush(open_set, (f2, g2, neighbor, path + [neighbor]))

    return None, float("inf")


# Grid definition (0 = free, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

rows, cols = len(grid), len(grid[0])

def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0

def neighbors_fn(node):
    r, c = node
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    result = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            result.append(((nr, nc), 1))  # cost = 1
    return result

def h_fn(node):
    # Manhattan distance
    r, c = node
    gr, gc = goal
    return abs(r - gr) + abs(c - gc)

start = (0, 0)
goal = (4, 4)

path, cost = a_star(start, goal, neighbors_fn, h_fn)

print("Path:", path)
print("Cost:", cost)


from collections import deque

def water_jug(x, y, d):
    """
    Solve the water jug problem using BFS.
    x: capacity of jug X
    y: capacity of jug Y
    d: target amount to measure
    """
    visited = set()
    q = deque([ (0, 0, []) ])  # (jugX, jugY, path)

    while q:
        jugX, jugY, path = q.popleft()

        # If target found
        if jugX == d or jugY == d:
            return path + [(jugX, jugY)]

        if (jugX, jugY) in visited:
            continue
        visited.add((jugX, jugY))

        # All possible moves
        moves = [
            (x, jugY),             # fill jug X
            (jugX, y),             # fill jug Y
            (0, jugY),             # empty jug X
            (jugX, 0),             # empty jug Y
            # pour X → Y
            (jugX - min(jugX, y - jugY), jugY + min(jugX, y - jugY)),
            # pour Y → X
            (jugX + min(jugY, x - jugX), jugY - min(jugY, x - jugX))
        ]

        for newX, newY in moves:
            q.append((newX, newY, path + [(jugX, jugY)]))

    return None
# Example: Jug X = 4L, Jug Y = 3L, target = 2L
solution = water_jug(4, 3, 2)

if solution:
    print("Steps to reach the solution:")
    for state in solution:
        print(state)
else:
    print("No solution found.")


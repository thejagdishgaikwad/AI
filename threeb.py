import random

def hill_climb(objective_fn, neighbor_fn, max_iterations=1000):
    """
    Hill climbing algorithm.

    Args:
        objective_fn: function(x) -> value (higher is better)
        neighbor_fn: function(x) -> list of neighbors
        max_iterations: max steps before stopping

    Returns:
        Best solution found and its score.
    """
    # Start from a random initial solution
    current = random.randint(-10, 10)
    current_score = objective_fn(current)

    for _ in range(max_iterations):
        neighbors = neighbor_fn(current)
        if not neighbors:
            break
        # pick best neighbor
        next_candidate = max(neighbors, key=objective_fn)
        next_score = objective_fn(next_candidate)

        if next_score <= current_score:
            # No improvement → stop
            break

        current, current_score = next_candidate, next_score

    return current, current_score


# Example: maximize f(x) = -(x-3)^2 + 9 (peak at x=3)
def objective_fn(x):
    return -(x - 3) ** 2 + 9

def neighbor_fn(x):
    return [x - 1, x + 1]  # simple neighbors

# Run
best_solution, best_value = hill_climb(objective_fn, neighbor_fn, max_iterations=100)
print(f"Best solution: x={best_solution}, f(x)={best_value}")


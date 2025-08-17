import math

def alpha_beta(node, depth, alpha, beta, maximizing_player, evaluate, children_fn):
    """
    Alpha-Beta search algorithm.

    Args:
        node: current game state (can be anything)
        depth: remaining depth to search
        alpha: best value that the maximizer currently can guarantee
        beta: best value that the minimizer currently can guarantee
        maximizing_player: True if it's maximizer's turn
        evaluate: function(node) -> int (heuristic evaluation)
        children_fn: function(node) -> list of next states

    Returns:
        Best score achievable from this node.
    """
    # base case: leaf node or depth reached
    if depth == 0 or not children_fn(node):
        return evaluate(node)

    if maximizing_player:
        max_eval = -math.inf
        for child in children_fn(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, False, evaluate, children_fn)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  # prune
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in children_fn(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, True, evaluate, children_fn)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:  # prune
                break
        return min_eval


# Example game tree
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Leaf values
leaf_values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

def children_fn(node):
    return game_tree.get(node, [])

def evaluate(node):
    return leaf_values.get(node, 0)  # default 0 if not leaf

best_value = alpha_beta('A', depth=3, alpha=-math.inf, beta=math.inf,
                        maximizing_player=True,
                        evaluate=evaluate,
                        children_fn=children_fn)

print("Best value from root (A):", best_value)


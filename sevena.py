# Re-run after kernel reset: implement & execute quickly (shorter print), then save file.

from collections import deque
from typing import Dict, List, Tuple, Callable, Iterable, Optional, Any
import copy

class CSP:
    def __init__(self, variables, domains, neighbors, constraint):
        self.variables = variables
        self.domains = {v: list(domains[v]) for v in variables}
        self.neighbors = {v: list(neighbors.get(v, [])) for v in variables}
        self.constraint = constraint

    def ac3(self, arcs=None):
        if arcs is None:
            queue = deque((Xi, Xj) for Xi in self.variables for Xj in self.neighbors[Xi])
        else:
            queue = deque(arcs)
        while queue:
            Xi, Xj = queue.popleft()
            if self.revise(Xi, Xj):
                if not self.domains[Xi]:
                    return False
                for Xk in self.neighbors[Xi]:
                    if Xk != Xj:
                        queue.append((Xk, Xi))
        return True

    def revise(self, Xi, Xj):
        revised = False
        to_remove = []
        for x in self.domains[Xi]:
            if not any(self.constraint(Xi, x, Xj, y) for y in self.domains[Xj]):
                to_remove.append(x)
        if to_remove:
            for x in to_remove:
                self.domains[Xi].remove(x)
            revised = True
        return revised

def backtracking_search(csp: CSP, use_ac3=True, use_forward_check=True):
    if use_ac3 and not csp.ac3():
        return None

    assignment: Dict[Any, Any] = {}

    def forward_check(var, value, removals):
        if not use_forward_check:
            return True
        for nb in csp.neighbors[var]:
            if nb not in assignment:
                for val in list(csp.domains[nb]):
                    if not csp.constraint(var, value, nb, val):
                        csp.domains[nb].remove(val)
                        removals.append((nb, val))
                if not csp.domains[nb]:
                    return False
        return True

    def restore(removals):
        for v, val in removals:
            if val not in csp.domains[v]:
                csp.domains[v].append(val)

    def select_unassigned_variable():
        unassigned = [v for v in csp.variables if v not in assignment]
        mrv = min(unassigned, key=lambda v: len(csp.domains[v]))
        min_size = len(csp.domains[mrv])
        ties = [v for v in unassigned if len(csp.domains[v]) == min_size]
        if len(ties) == 1:
            return ties[0]
        return max(ties, key=lambda v: len([n for n in csp.neighbors[v] if n not in assignment]))

    def order_domain_values(var):
        def constraint_count(val):
            cnt = 0
            for nb in csp.neighbors[var]:
                if nb not in assignment:
                    for y in csp.domains[nb]:
                        if not csp.constraint(var, val, nb, y):
                            cnt += 1
            return cnt
        return sorted(csp.domains[var], key=constraint_count)

    def consistent(var, val):
        for v2, val2 in assignment.items():
            if v2 in csp.neighbors[var] and not csp.constraint(var, val, v2, val2):
                return False
        return True

    def backtrack():
        if len(assignment) == len(csp.variables):
            return dict(assignment)
        var = select_unassigned_variable()
        for val in order_domain_values(var):
            if consistent(var, val):
                assignment[var] = val
                removals = []
                if forward_check(var, val, removals):
                    if use_ac3:
                        inferences = deque((nb, var) for nb in csp.neighbors[var] if nb not in assignment)
                        snapshot = copy.deepcopy({v: list(csp.domains[v]) for v in csp.variables})
                        if csp.ac3(inferences):
                            result = backtrack()
                            if result is not None:
                                return result
                        for v in csp.variables:
                            csp.domains[v] = snapshot[v]
                    else:
                        result = backtrack()
                        if result is not None:
                            return result
                restore(removals)
                del assignment[var]
        return None

    return backtrack()

# Example 1: Australia Map Coloring
def australia_map_coloring():
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colors = ["Red", "Green", "Blue"]
    neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q":  ["NT", "SA", "NSW"],
        "NSW":["SA", "Q", "V"],
        "V":  ["SA", "NSW"],
        "T":  []
    }
    domains = {r: list(colors) for r in regions}

    def constraint(Xi, xi, Xj, xj):
        return xi != xj if Xj in neighbors[Xi] else True

    csp = CSP(regions, domains, neighbors, constraint)
    return backtracking_search(csp, use_ac3=True, use_forward_check=True)

# Example 2: Sudoku
def sudoku_csp(grid: str):
    squares = [f"{r}{c}" for r in "ABCDEFGHI" for c in "123456789"]
    rows = "ABCDEFGHI"
    cols = "123456789"
    def cross(A, B):
        return [a+b for a in A for b in B]
    unitlist = ([cross(r, cols) for r in rows] +
                [cross(rows, c) for c in cols] +
                [cross(rs, cs) for rs in ("ABC","DEF","GHI") for cs in ("123","456","789")])
    units = {s: [u for u in unitlist if s in u] for s in squares}
    peers = {s: sorted(set(sum(units[s], [])) - {s}) for s in squares}
    variables = squares
    digits = list("123456789")
    domains = {s: (digits if ch in ".0" else [ch]) for s, ch in zip(squares, grid)}
    neighbors = {s: peers[s] for s in squares}
    def constraint(Xi, xi, Xj, xj):
        return xi != xj if Xj in neighbors[Xi] else True
    return CSP(variables, domains, neighbors, constraint)

def solve_sudoku(grid: str):
    csp = sudoku_csp(grid)
    sol = backtracking_search(csp, use_ac3=True, use_forward_check=True)
    if not sol:
        return None
    board = [["" for _ in range(9)] for _ in range(9)]
    for r_i, r in enumerate("ABCDEFGHI"):
        for c_i, c in enumerate("123456789"):
            board[r_i][c_i] = sol[f"{r}{c}"]
    return board

# Run quick demos
print("=== Australia Map Coloring ===")
print(australia_map_coloring())

print("\n=== Sudoku Demo (first 3 rows) ===")
puzzle = (
    "53..7...."
    "6..195..."
    ".98....6."
    "8...6...3"
    "4..8.3..1"
    "7...2...6"
    ".6....28."
    "...419..5"
    "....8..79"
)
board = solve_sudoku(puzzle)
if board:
    for row in board[:3]:
        print(" ".join(row))
else:
    print("No solution found.")

# Save file
code_text = open(__file__, "r").read() if "__file__" in globals() else ""
with open("csp_solver.py", "w", encoding="utf-8") as f:
    if code_text:
        f.write(code_text)
    else:
        # Minimal self-contained file if source not available
        f.write("# CSP solver saved from session.\n")
print("\ncsp_solver.py")

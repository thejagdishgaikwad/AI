#Practical 2A
#!/usr/bin/env python3
from typing import List

def solve_n_queens_backtracking(n: int) -> List[List[int]]:
    sols: List[List[int]] = []
    cols = [-1] * n
    used_cols = set()
    used_diag1 = set()  # r - c
    used_diag2 = set()  # r + c

    def place(row: int):
        if row == n:
            sols.append(cols.copy())
            return
        for c in range(n):
            if c in used_cols or (row - c) in used_diag1 or (row + c) in used_diag2:
                continue
            cols[row] = c
            used_cols.add(c)
            used_diag1.add(row - c)
            used_diag2.add(row + c)
            place(row + 1)
            used_cols.remove(c)
            used_diag1.remove(row - c)
            used_diag2.remove(row + c)
            cols[row] = -1

    place(0)
    return sols

def solve_n_queens_bitmask(n: int) -> List[List[int]]:
    sols: List[List[int]] = []
    cols = [-1] * n

    def dfs(row: int, colMask: int, d1Mask: int, d2Mask: int):
        if row == n:
            sols.append(cols.copy())
            return
        available = (~(colMask | d1Mask | d2Mask)) & ((1 << n) - 1)
        while available:
            bit = available & -available
            available -= bit
            c = (bit.bit_length() - 1)
            cols[row] = c
            dfs(row + 1,
                colMask | bit,
                (d1Mask | bit) << 1,
                (d2Mask | bit) >> 1)
            cols[row] = -1

    dfs(0, 0, 0, 0)
    return sols

def boards_from_solutions(n: int, solutions: List[List[int]]) -> List[List[str]]:
    boards = []
    for sol in solutions:
        board = []
        for r, c in enumerate(sol):
            row = ['.'] * n
            row[c] = 'Q'
            board.append(' '.join(row))
        boards.append(board)
    return boards

def pretty_print_solutions(n: int, solutions: List[List[int]]):
    boards = boards_from_solutions(n, solutions)
    print(f"N={n} — {len(boards)} solution(s)\\n")
    for i, b in enumerate(boards, 1):
        print(f"Solution {i}:")
        for row in b:
            print(row)
        print()

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Solve the N-Queens problem and print all solutions.")
    ap.add_argument("N", type=int, help="Board size (number of queens)")
    ap.add_argument("--method", choices=["backtracking", "bitmask"], default="bitmask",
                    help="Solver to use (bitmask is faster for larger N)")
    args = ap.parse_args()

    if args.N <= 0:
        raise SystemExit("N must be a positive integer.")

    if args.method == "backtracking":
        sols = solve_n_queens_backtracking(args.N)
    else:
        sols = solve_n_queens_bitmask(args.N)

    pretty_print_solutions(args.N, sols)

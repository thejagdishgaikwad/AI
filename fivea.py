import math

# Print the board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("|".join(row))
    print()

# Check for winner
def check_winner(board):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),  # rows
        (0,3,6),(1,4,7),(2,5,8),  # cols
        (0,4,8),(2,4,6)           # diagonals
    ]
    for a,b,c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif winner == "Draw":
        return 0

    if is_maximizing:  # O's turn (AI)
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  # X's turn (human)
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Best move for AI (O)
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
def play_game():
    board = [" "] * 9
    print("Tic-Tac-Toe (You are X, AI is O)")
    print_board(board)

    while True:
        # Human turn
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"
        print_board(board)

        if check_winner(board):
            print("Result:", check_winner(board))
            break

        # AI turn
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI played:")
        print_board(board)

        if check_winner(board):
            print("Result:", check_winner(board))
            break


# Run game
if __name__ == "__main__":
    play_game()


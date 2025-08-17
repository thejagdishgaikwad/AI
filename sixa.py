import os
import sys
import tty
import termios
import random

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)
        if ch1 == '\x1b':  # escape sequence
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            return ch1 + ch2 + ch3
        else:
            return ch1
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def print_board(board):
    os.system("clear")
    for row in board:
        print(" ".join(f"{x:2}" if x != 0 else "  " for x in row))

def find_blank(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

def move(board, direction):
    i, j = find_blank(board)
    if direction == '\x1b[A' and i < len(board) - 1:  # Up arrow
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    elif direction == '\x1b[B' and i > 0:  # Down arrow
        board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
    elif direction == '\x1b[C' and j > 0:  # Right arrow
        board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
    elif direction == '\x1b[D' and j < len(board[0]) - 1:  # Left arrow
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

# --- Main game ---
size = 3
nums = list(range(size*size))
random.shuffle(nums)
board = [nums[i*size:(i+1)*size] for i in range(size)]

while True:
    print_board(board)
    print("Use arrow keys to move, q to quit")
    key = get_key()
    if key == "q":
        break
    move(board, key)

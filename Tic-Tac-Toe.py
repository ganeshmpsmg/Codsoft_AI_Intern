"""
CODSOFT AI Internship - Task 2
Tic-Tac-Toe AI using Minimax Algorithm
Run: python tictactoe.py
"""

import math

board = [" "] * 9


def print_board():
    print("\n")
    for i in range(3):
        row = []
        for j in range(3):
            index = i * 3 + j

            # Show position number if empty
            if board[index] == " ":
                row.append(str(index + 1))
            else:
                row.append(board[index])

        print(f"  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print(" ---+---+---")
    print()


def winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if winner("Y"):
        return 1
    if winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "Y"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best


def ai_move():
    best_score = -math.inf
    best_pos = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "Y"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_pos = i

    board[best_pos] = "Y"


print("=" * 40)
print("  Tic-Tac-Toe — CODSOFT AI Task 2")
print("=" * 40)
print("  You = X  |  AI = Y")
print("  Enter position numbers to play\n")


while True:
    board = [" "] * 9

    for turn in range(9):
        print_board()

        if turn % 2 == 0:
            while True:
                try:
                    pos = int(input("Your move (1-9): ")) - 1
                    if 0 <= pos <= 8 and board[pos] == " ":
                        board[pos] = "X"
                        break
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a number between 1 and 9.")

        else:
            print("ONLINE AI is Thinking,wait...")
            ai_move()

        if winner("X"):
            print_board()
            print(" You win! Congrates!")
            break

        if winner("Y"):
            print_board()
            print(" AI wins! next time try and if not,again try to win...")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

    again = input("Play again? Type 'replay' to continue: ").strip().lower()

    if again != "replay":
        print("Thanks for playing! Goodbye!")
        break
README.md
# Tic-Tac-Toe AI using Minimax Algorithm - CODSOFT AI Internship Task 2

This project implements a **Tic-Tac-Toe game** with an AI opponent using the **Minimax algorithm**. The AI plays optimally, ensuring a challenging game for the player.  

---

## Features

- Play Tic-Tac-Toe against an AI.  
- AI uses **Minimax Algorithm** to make optimal moves.  
- Command-line interface with interactive prompts.  
- Replay option to start a new game without restarting the program.  

---

## How It Works

1. **Board Representation:** The 3x3 Tic-Tac-Toe board is represented as a list of 9 elements.  
2. **Minimax Algorithm:** AI evaluates all possible moves and chooses the move that maximizes its chance to win while minimizing the player's chance.  
3. **Win/Draw Detection:** The game checks for winning conditions after each move and detects draw situations.  
4. **User Interaction:** The player enters positions (1-9) to place their marker ("X"). The AI moves as "Y".  

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/ganesmpsmg/Tic-Tac-Toe.git
cd Tic-Tac-Toe

Install dependencies:

pip install -r requirements.txt

Run the program:

python tictactoe.py

Follow the prompts to play:

Enter numbers 1-9 to make your move.

The AI will respond automatically.

Type replay after a game ends to play again.

Example Gameplay
  1 | 2 | 3
 ---+---+---
  4 | 5 | 6
 ---+---+---
  7 | 8 | 9

Your move (1-9): 5
ONLINE AI is Thinking, wait...

  X |   |  
 ---+---+---
    | Y |  
 ---+---+---
    |   |  

...
You win! Congrates!
Requirements

Python 3.7+

Libraries:

math (built-in)

No external packages are required.

Author

Ganesh MP
CODSOFT AI Internship – Task 2


Github repository link:https://github.com/ganesmpsmg/Codsoft_AI_Intern/tree/Tic-Tac-Toe

import tkinter as tk
from tkinter import messagebox
import random

# Make the Game Board
# take Player input
# Check for Win or Tie
# Switch the player 
# Check for win or tie again
# Add Ai Elements

def next_turn():
    pass

def check_winner():
    def check_winner(board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False


def empty_spaces():
    pass

def new_game():
    pass
# Function to start or restart the game in the selected mode
def start_game(mode):
    global single_player, board, buttons
    single_player = mode == "Single Player"

    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

# Initialize the board and buttons
    board = [[' ' for _ in range(3)] for _ in range(3)]
    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            btn = tk.Button(window, text=' ', font=('Arial', 24), width=5, height=2,)
            btn.grid(row=i, column=j)
            row_buttons.append(btn)
        buttons.append(row_buttons)

# Function to check if the board is full (draw condition)
def is_full(board):
    return all(cell in ('X', 'O') for row in board for cell in row)

# Function to reset the board for a new game
def reset_board():
    global board, turn
    turn = 0
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state=tk.NORMAL)

#Main Window setup
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x500")  # Window Size

#Main Component for the Game
players = ['X', 'O']
player = random.choice(players)
single_player = False
buttons = []
board = []

#label = (text= player + " turn", font=('consolas',40))
#label.pack(side="Bottom")

reset_button = tk.Button(window, text="Restart", font=('consolas',20), command=start_game)
reset_button.grid(row=3, column=0, columnspan=3)

start_game("Two Player")
window.mainloop()

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
    pass

def empty_spaces():
    pass

def new_game():
    pass


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

reset_button = tk.Button(window, text="Restart", font=('consolas',20), command=new_game)
reset_button.grid(row=3, column=0, columnspan=3)


window.mainloop()

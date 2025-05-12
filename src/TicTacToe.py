import tkinter as tk
from tkinter import messagebox
import random

# Check if a player has won
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check for draw condition
def is_full(board):
    return all(cell in ('X', 'O') for row in board for cell in row)

# Reset the board for a new game
def reset_board():
    global board, turn
    turn = 0
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state=tk.NORMAL)

# Ai Function to find winning move or block opponent
def find_best_move(board, player):
    opponent = 'X' if player == 'O' else 'O'

    # Try to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if check_winner(board, player):
                    board[i][j] = ' '
                    return (i, j)
                board[i][j] = ' '

    # Block opponent from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = opponent
                if check_winner(board, opponent):
                    board[i][j] = ' '
                    return (i, j)
                board[i][j] = ' '

    return None

# Function to handle the AI's move
def ai_move():
    best_move = find_best_move(board, 'O')
    if best_move:
        row, col = best_move
    else:
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        row, col = random.choice(empty_cells)

    board[row][col] = 'O'
    buttons[row][col].config(text='O')

    if check_winner(board, 'O'):
        messagebox.showinfo("Game Over", "AI wins!", parent=window)
        reset_board()
    elif is_full(board):
        messagebox.showinfo("Game Over", "It's a draw!", parent=window)
        reset_board()

# When button is clicked it handle a player's move
def on_click(row, col):
    global turn
    if board[row][col] == ' ':
        board[row][col] = players[turn % 2]
        buttons[row][col].config(text=players[turn % 2])

        if check_winner(board, players[turn % 2]):
            messagebox.showinfo("Game Over", f"Player {players[turn % 2]} wins!", parent=window)
            reset_board()
            return
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a draw!", parent=window)
            reset_board()
            return

        turn += 1
        # Let AI play after human in single player mode
        if single_player and turn % 2 == 1:
            ai_move()
            turn += 1

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
            btn = tk.Button(window, text=' ', font=('Arial', 24), width=5, height=2,
                            command=lambda i=i, j=j: on_click(i, j))
            btn.grid(row=i, column=j)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    # Reset/play again button
    reset_button = tk.Button(window, text="Play Again", font=('Arial', 14), command=reset_board)
    reset_button.grid(row=3, column=0, columnspan=3)

    # Mode selection buttons
    mode_frame = tk.Frame(window)
    mode_frame.grid(row=4, column=0, columnspan=3)

    pvp_button = tk.Button(mode_frame, text="Two Player", font=('Arial', 12), command=lambda: start_game("Two Player"))
    pvp_button.pack(side=tk.LEFT, padx=5)

    ai_button = tk.Button(mode_frame, text="Single Player", font=('Arial', 12), command=lambda: start_game("Single Player"))
    ai_button.pack(side=tk.LEFT, padx=5)

    reset_board()

#Main Winodw
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x500")  # Window Size

#Main Component for the Game
players = ['X', 'O']
player = random.choice(players)
single_player = False
buttons = []
board = []

#Start Game
start_game("Two Player")
window.mainloop()

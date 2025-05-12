board = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]
currrentPlayer = "X"
winner = None
gameRunning= True


#Make the Game Board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("________")
    print(board[6] + " | " + board[7] + " | " + board[8])
    printBoard(board)
    print("________")

# take Player input


# Check for Win or Tie

# Switch the player 

# Check for win or tie again
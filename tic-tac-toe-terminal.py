import random
# import tkinter as tk

# root = tk.Tk()
# root.title("Tic Tac Toe")


board =["-","-","-",
        "-","-","-",
        "-","-","-"]

currentPlayer = "X"
winner = None
gameRunning  = True




#printing the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take player input
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter position (1-9): "))

            if inp < 1 or inp > 9:
                print("Enter a number between 1 and 9.")
                continue

            if board[inp-1] != "-":
                print("That position is already occupied.")
                continue

            board[inp-1] = currentPlayer
            return True

        except ValueError:
            print("Please enter a number.")
    


#check for win or tie

def checkTie(board):
    global gameRunning

    if "-" not in board:
        printBoard(board)
        print("It's a Tie!")
        gameRunning = False
        return True

    return False
    
def checkWin():
    
        global winner, gameRunning

        winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if board[a] == board[b] == board[c] != "-":
                winner = board[a]
                printBoard(board)
                print(f"The winner is {winner} 🎉")
                gameRunning = False
                return True

        return False

#switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
        print(f"Current chance is of {currentPlayer}")
    else:
        currentPlayer = "X"
        print(f"Current chance is of {currentPlayer}")

#computer 

def computer(board):
    if difficulty == "easy":
            easyBot(board)
    else:
            mediumBot(board)
    
    

def easyBot(board):
    while True:
        position = random.randint(0,8)

        if board[position] == "-":
            board[position] = "O"
            return
    
def mediumBot(board):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        values = [board[i] for i in combo]
        if values.count("O") == 2 and values.count("-") == 1:
            move = combo[values.index("-")]
            board[move] = "O"
            return
        
    for combo in wins:
        values = [board[i] for i in combo]
        if values.count("X") == 2 and values.count("-") == 1:
            move = combo[values.index("-")]
            board[move] = "O"
            return
    
    chance = random.randint(1, 100)

    if chance <= 80:

        # Take center
        if board[4] == "-":
            board[4] = "O"
            return

        # Random corner
        corners = [0,2,6,8]
        random.shuffle(corners)

        for corner in corners:
            if board[corner] == "-":
                board[corner] = "O"
                return

        # Random side
        sides = [1,3,5,7]
        random.shuffle(sides)

        for side in sides:
            if board[side] == "-":
                board[side] = "O"
                return

    else:
        # Random move
        empty = []

        for i in range(9):
            if board[i] == "-":
                empty.append(i)

        move = random.choice(empty)
        board[move] = "O"

#--------------Main Menu-----------------#
print("Welcome to Tic Tac Toe")
print("1. Player vs Player")
print("2. Player vs Computer")
print("3. Exit")

choice = int(input("Select Game Mode: "))

difficulty = ""

if choice == 2:
    difficulty = input("Easy or Medium: ").lower()
print("-------------------------------------------------------------------------------")
print("Game is started by X")



#-------------game-loop--------------#


while gameRunning:
    printBoard(board)
    playerInput(board)
    
    if checkWin():
        break

    if checkTie(board):
        break
    

    switchPlayer()

    if choice == 1:
        playerInput(board)
    else:
        computer(board)

    if checkWin():
        break

    if checkTie(board):
        break

    switchPlayer()

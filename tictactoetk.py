import random
import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("420x500")
windowWidth = 420
windowHeight = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = (screenWidth // 2) - (windowWidth // 2)
y = (screenHeight // 2) - (windowHeight // 2)

root.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")
root.resizable(False, False)

# ---------------- GAME VARIABLES ---------------- #

board = ["-"] * 9
buttons = []

currentPlayer = "X"
winner = None
winningLine = []
gameRunning = True

gameMode = ""
difficulty = ""



# ---------------- FRAMES ---------------- #

menuFrame = tk.Frame(root)
difficultyFrame = tk.Frame(root)
gameFrame = tk.Frame(root)

# Show only menu first
menuFrame.pack(fill="both", expand=True)

# ---------------- MENU ---------------- #

title = tk.Label(
    menuFrame,
    text="TIC TAC TOE",
    font=("Arial", 24, "bold")
)

title.pack(pady=30)


def startPVP():
    global gameMode

    gameMode = "pvp"

    menuFrame.pack_forget()
    gameFrame.pack(fill="both", expand=True)


def showDifficulty():

    menuFrame.pack_forget()
    difficultyFrame.pack(fill="both", expand=True)


pvpButton = tk.Button(
    menuFrame,
    text="Player vs Player",
    font=("Arial", 15),
    width=20,
    command=startPVP
)

pvpButton.pack(pady=10)


computerButton = tk.Button(
    menuFrame,
    text="Player vs Computer",
    font=("Arial", 15),
    width=20,
    command=showDifficulty
)

computerButton.pack(pady=10)

# ---------------- DIFFICULTY SCREEN ---------------- #

difficultyTitle = tk.Label(
    difficultyFrame,
    text="Select Difficulty",
    font=("Arial", 22, "bold")
)

difficultyTitle.pack(pady=30)


def startEasy():
    global gameMode, difficulty

    gameMode = "computer"
    difficulty = "easy"

    difficultyFrame.pack_forget()
    gameFrame.pack(fill="both", expand=True)


def startMedium():
    global gameMode, difficulty

    gameMode = "computer"
    difficulty = "medium"

    difficultyFrame.pack_forget()
    gameFrame.pack(fill="both", expand=True)


easyButton = tk.Button(
    difficultyFrame,
    text="Easy",
    font=("Arial", 15),
    width=20,
    command=startEasy
)

easyButton.pack(pady=10)


mediumButton = tk.Button(
    difficultyFrame,
    text="Medium",
    font=("Arial", 15),
    width=20,
    command=startMedium
)

mediumButton.pack(pady=10)

backButton = tk.Button(
    difficultyFrame,
    text="Back",
    font=("Arial", 15),
    width=20,
    command=lambda: (
        difficultyFrame.pack_forget(),
        menuFrame.pack(fill="both", expand=True)
    )
)

backButton.pack(pady=30)

# ---------------- GAME SCREEN ---------------- #

statusLabel = tk.Label(
    gameFrame,
    text="Current Turn : X",
    font=("Arial",16,"bold")
)

statusLabel.grid(row=0, column=0, columnspan=3, pady=10)


def updateStatus():
    statusLabel.config(text=f"Current Turn : {currentPlayer}")

def restartGame():

    global board
    global currentPlayer
    global winner
    global gameRunning

    board = ["-"] * 9

    currentPlayer = "X"
    winner = None
    gameRunning = True

    updateStatus()

    for button in buttons:
        button.config(
        text="",
        state="normal",
        bg="white",
        fg="black"
        )   
        winningLine.clear()



for row in range(3):
    for col in range(3):

        position = row * 3 + col

        button = tk.Button(
            gameFrame,
            text="",
            font=("Arial",30,"bold"),
            width=5,
            height=2,
            bg="white",
            activebackground="#e8f4ff",
            command=lambda pos=position: buttonClick(pos)
        )

        button.grid(
            row=row+1,
            column=col,
            padx=2,
            pady=2
        )

        buttons.append(button)


restartButton = tk.Button(
    gameFrame,
    text="Restart",
    font=("Arial",15),
    command=restartGame
)

restartButton.grid(
    row=4,
    column=0,
    columnspan=3,
    sticky="we",
    pady=10
)
exitButton = tk.Button(
    gameFrame,
    text="Exit",
    font=("Arial",14),
    command=root.destroy
)

exitButton.grid(
    row=4,
    column=2,
    sticky="we"
)
# ---------------- GAME LOGIC ---------------- #

board = ["-"] * 9



currentPlayer = "X"
winner = None
gameRunning = True


def updateStatus():
    statusLabel.config(text=f"Current Turn : {currentPlayer}")


def switchPlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

    updateStatus()


def disableBoard():
    for button in buttons:
        button.config(state="disabled")

def updateBoard():

    for i in range(9):

        buttons[i]["text"] = board[i]

        if board[i] == "X":
            buttons[i].config(fg="#0066ff")

        elif board[i] == "O":
            buttons[i].config(fg="#ff3333")

        else:
            buttons[i].config(fg="black")

def checkTie():
    global gameRunning

    if "-" not in board:
        gameRunning = False
        return True

    return False


def checkWin():
    global winner
    global gameRunning

    winningCombinations = [

        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]

    ]

    for combo in winningCombinations:

        a,b,c = combo

        if board[a] == board[b] == board[c] != "-":

            winner = board[a]
            winningLine[:] = combo
            gameRunning = False

            return True

    return False

def highlightWinner():

    for i in winningLine:

        buttons[i].config(
            bg="lightgreen"
        )
# ---------------- COMPUTER AI ---------------- #

def computer():

    if difficulty == "easy":
        easyBot()
    else:
        mediumBot()


def easyBot():

    while True:

        position = random.randint(0,8)

        if board[position] == "-":
            board[position] = "O"
            return


def mediumBot():

    wins = [

        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]

    ]

    # Win

    for combo in wins:

        values = [board[i] for i in combo]

        if values.count("O") == 2 and values.count("-") == 1:

            move = combo[values.index("-")]

            board[move] = "O"

            return

    # Block

    for combo in wins:

        values = [board[i] for i in combo]

        if values.count("X") == 2 and values.count("-") == 1:

            move = combo[values.index("-")]

            board[move] = "O"

            return


    chance = random.randint(1,100)

    if chance <= 80:

        if board[4] == "-":

            board[4] = "O"

            return


        corners = [0,2,6,8]

        random.shuffle(corners)

        for corner in corners:

            if board[corner] == "-":

                board[corner] = "O"

                return


        sides = [1,3,5,7]

        random.shuffle(sides)

        for side in sides:

            if board[side] == "-":

                board[side] = "O"

                return

    else:

        empty = []

        for i in range(9):

            if board[i] == "-":

                empty.append(i)

        move = random.choice(empty)

        board[move] = "O"

# ---------------- BUTTON CLICK ---------------- #

def buttonClick(position):

    global currentPlayer

    if not gameRunning:
        return

    if board[position] != "-":
        return

    board[position] = currentPlayer
    buttons[position]["text"] = currentPlayer

    # ---------- Player Win ----------

    if checkWin():
        messagebox.showinfo(
            "Game Over",
            f"{winner} Wins!"
        )
        highlightWinner()
        disableBoard()
        return

    if checkTie():
        messagebox.showinfo(
            "Game Over",
            "It's a Tie!"
        )
        highlightWinner()
        disableBoard()
        return

    switchPlayer()

    # ---------- Computer ----------

    if gameMode == "computer":

        computer()

        updateBoard()

        if checkWin():
            messagebox.showinfo(
                "Game Over",
                f"{winner} Wins!"
            )
            highlightWinner()
            disableBoard()
            return

        if checkTie():
            messagebox.showinfo(
                "Game Over",
                "It's a Tie!"
            )
            highlightWinner()
            disableBoard()
            return

        switchPlayer()


root.mainloop()

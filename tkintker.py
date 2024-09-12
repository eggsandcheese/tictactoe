from tkinter import *
import copy
from random import choice

AI = False
X = "X"
O = "O"
EMPTY = ""
players = [X , O]
player = X
number_of_turns = 0

# Checks for next turn of player
def next_turn(row, column):
    if click(row, column) == "ok":
        runai()

def click(row, column):
    global number_of_turns
    global player
    if terminal() == True:
        return 
    if (board[row][column]['text'] != ""):
        return
    board[row][column]['text'] = player
    if player == O:
        player = X
        number_of_turns +=1
        numberofturnsButton.config(text=number_of_turns)
    else:
        player = O
        number_of_turns +=1
        numberofturnsButton.config(text=number_of_turns)
    turn.config(text= (player + "'s turn"))
    terminal()
    if AI == True:
        return "ok"

def aitrue():
    global AI
    if AI == False:
        AI = True
        
    else:
        AI = False

def actions():
    if terminal():
        return
    allactions = [(row, column) for row in range(len(board)) for column in range((len(board[row]))) if board[row][column]['text'] == EMPTY]
    return allactions

def runai():
    if terminal():
        return
    row , column = choice(actions())
    click(row, column)
    """
    egg = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column]['text'] == "":
                egg.append((row, column))
                click(random.choice(egg))
    """


# Checks for Winner
def check_winner():
    #Check for Function Call 
    global player
    print('check')
    for row in range(len(board)):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] and board[row][0]['text']  != "":
            print("egg2")
            board[row][0].config(bg="green")
            board[row][1].config(bg="green")
            board[row][2].config(bg="green")
            return board[row][0]['text']
    print ("win")
    for column in range(len(board)):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] and board[1][column]['text']  != "":
            print("egg2")
            board[0][column].config(bg="green")
            board[1][column].config(bg="green")
            board[2][column].config(bg="green")
            return board[0][column]['text']
    
    if board[1][1]['text'] == '':
        return False
    elif board[0][0]['text'] == board[2][2]['text'] == board[1][1]['text']:
        board[0][0].config(bg="green")
        board[1][1].config(bg="green")
        board[2][2].config(bg="green")
        return board[0][0]['text']
    elif board[0][2]['text'] == board[2][0]['text'] == board[1][1]['text']:
        board[0][2].config(bg="green")
        board[2][0].config(bg="green")
        board[1][1].config(bg="green")
        return board[0][2]['text']
    space = 9
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]['text'] != "":
                space -= 1
        
    if space == 0:
        for row in range(len(board)):
            for column in range(len(board)):
                board[row][column].config(bg="yellow")   
        return "Tie"
    
def new_game(board):
    global player
    global number_of_turns
    number_of_turns = 0
    numberofturnsButton.config(text=number_of_turns)
    player = X
    turn.config(text=player+"'s turn")
    for row in range(len(board)):
        for column in range((len(board))):
            board[row][column].config(text="",bg="#F0F0F0")
    return False

def result():
    pass
    boards = []
    for row in range(len(board)):
        for column in range(len(board)):
            board.append(board[row][column]['text'])
    
    return boards

    
def terminal():  
    if check_winner() == O:
        turn.config(text= 'O wins')
        return True
    
    elif check_winner() == X:
        turn.config(text= 'X wins')
        return True
    
    elif check_winner() == "Tie":
        turn.config(text="Tie") 
        return True
    return False

def utility():
    if check_winner() == X:
        return 1

    elif check_winner() == O:
        return -1
    
    else:
        return 0

def maxvalue():
    v = float('-inf')
    if terminal():
        return utility()
    for action in actions():
        v = max(v, minvalue(actions()))
        return v

def minvalue():
    v = float('inf')
    if terminal():
        return utility()
    for action in actions:
        v = min(v, maxvalue(actions()))
        return v




root = Tk()
root.title("Tic-Tac-Toe")

numberofturnsButton = Label(text=number_of_turns)
numberofturnsButton.pack(side="top")

aicheckBox = Checkbutton(root, text='AI' , command=aitrue)
aicheckBox.pack()

turn = Label(text= "")
turn.pack(side="top")

board = [[EMPTY, EMPTY, EMPTY],  
         [EMPTY, EMPTY, EMPTY],  
         [EMPTY, EMPTY, EMPTY]]

resetButton = Button(text="Restart", command=lambda board=board: new_game(board))
resetButton.pack(side="top")

frame=Frame(root)
frame.pack()



for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text=EMPTY, width=20, height=8, command= lambda row=row , column=column: next_turn(row, column))
        board[row][column].grid(row=row, column=column ,sticky=W+E) 
        
           

        
    
root.mainloop()

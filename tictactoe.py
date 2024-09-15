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
    boards = [] 
    for row in range(len(board)):
        for column in range(len(board)):
            boards.append(board[row][column]['text'])
    print (boards)
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
    


# Checks for Winner
def check_winner():
    #Check for Function Call 
    global player
    print('check')
    for row in range(len(board)):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] and board[row][0]['text']  != "":
            print("egg2")
            colour(row, 0, row, 1, row, 2)
            return board[row][0]['text']
    print ("win")
    for column in range(len(board)):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] and board[1][column]['text']  != "":
            print("egg2")
            colour(0, column, 1,column, 2, column)
            return board[0][column]['text']
    
    if board[1][1]['text'] == '':
        return False
    elif board[0][0]['text'] == board[2][2]['text'] == board[1][1]['text']:
        colour( 0, 0, 1, 1, 2, 2)
        return board[0][0]['text']
    elif board[0][2]['text'] == board[2][0]['text'] == board[1][1]['text']:
        colour(0,2 , 2, 0 ,1, 1)
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

def colour(r1,c1,r2,c2,r3,c3):
    board[r1][c1].config(bg="green")
    board[r2][c2].config(bg="green")
    board[r3][c3].config(bg="green")

def new_game(board):
    global player
    global number_of_turns
    number_of_turns = 0
    numberofturnsButton.config(text=number_of_turns)
    player = X
    turn.config(text=player+"'s turn. TicTacToe. Click boxes to play, or click checkbox to play with AI.")
    for row in range(len(board)):
        for column in range((len(board))):
            board[row][column].config(text="",bg="#F0F0F0")
    return False

def result(boards, actions):
    row, column = action
    boards[row][column] = player
    print (boards)
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
def minimax(boards):
    row, column = minvalue(boards)
    return 
def maxvalue(boards):
    v = float('-inf')
    if terminal():
        return utility()
    for action in actions():
        v = max(v, minvalue(result(boards, action)))
        return v

def minvalue(boards):
    v = float('inf')
    if terminal():
        return utility()
    for action in actions:
        v = min(v, maxvalue(result(boards, action)))
        return v




root = Tk()
root.title("Tic-Tac-Toe")

numberofturnsButton = Label(text=number_of_turns)
numberofturnsButton.pack(side="top")

aicheckBox = Checkbutton(root, text='AI' , command=aitrue)
aicheckBox.pack()

turn = Label(text= "TicTacToe. Click boxes to play, or click checkbox to play with AI.")
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

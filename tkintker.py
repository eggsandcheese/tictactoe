from tkinter import *
import copy
import random

X = "X"
O = "O"
EMPTY = None
players = [X , O]
player = random.choice(players)
win = False

# Checks for next turn of player
def next_turn(row, column):
    global player
    global win
    #Debug
    if check_winner() == "Tie":
        return
    print(player)
    if check_winner() == True:
        return
    print ("error1")
    if (board[row][column]['text'] != ""):
        return
    print ("error2")

    print ("error3")
    board[row][column]['text'] = player
    if player == "O":
        player = "X"
    else:
        player = "O"
    turn.config(text= (player + " 's turn"))


# Checks for Winner
def check_winner():
    #Check for Function Call
    global win  
    print('check')
    for row in range(len(board)):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text']:
            if board[row][0]['text'] == 'X':
                print("egg2")
                board[row][0].config(bg="green")
                board[row][1].config(bg="green")
                board[row][2].config(bg="green")
                turn.config(text= 'X wins')
                return True
            elif board[row][0]['text'] == O:
                board[row][0].config(bg="green")
                board[row][1].config(bg="green")
                board[row][2].config(bg="green")
                turn.config(text= 'O wins')
                return True
    print ("win")
    for column in range(len(board)):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text']:
            if board[0][column]['text'] == X:
                board[0][column].config(bg="green")
                board[1][column].config(bg="green")
                board[2][column].config(bg="green")

                turn.config(text= 'X wins')
                return True
            if board[0][column]['text'] == O:
                board[0][column].config(bg="green")
                board[1][column].config(bg="green")
                board[2][column].config(bg="green")
                turn.config(text= 'O win')
                return True
    
    if board[1][1]['text'] == '':
        return False
    elif board[0][0]['text'] == board[2][2]['text'] == board[1][1]['text']:
        board[0][0].config(bg="green")
        board[1][1].config(bg="green")
        board[2][2].config(bg="green")
        turn.config(text= board[1][1]['text'] + ' wins')
        return True
    elif board[0][2]['text'] == board[2][0]['text'] == board[1][1]['text']:
        board[0][2].config(bg="green")
        board[2][0].config(bg="green")
        board[1][1].config(bg="green")
        turn.config(text= board[1][1]['text'] + ' wins')
        return True
    print ("checiking..")
    space = 9
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]['text'] != "":
                space -= 1
        
    if space == 0:
        for row in range(len(board)):
            for column in range(len(board)):
                board[row][column].config(bg="yellow")
                turn.config(text="Tie")    
        return "Tie"
    print ("egg3")
    


def new_game(board):
    global win
    print("eggghjgvhj")
    player = random.choice(players)
    turn.config(text=player+" turn")
    for row in range(len(board)):
        for column in range((len(board))):
            board[row][column].config(text="",bg="#F0F0F0")
    return False




root = Tk()
root.title("Tic-Tac-Toe")



turn = Label(text= player + "'s turn")
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

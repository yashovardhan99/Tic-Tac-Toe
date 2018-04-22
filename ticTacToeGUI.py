from tkinter import *
import tkinter.messagebox
from ticTacToe import getAIMove,isWinner,isSpaceFree,makeMove

b = ['']*10
var = ['']*10
gameBoard = ['']*10
playerLetter='X' #Change later
AILetter = 'O'
playerColor='red'#Will be able to change later
AIColor='blue'
playerMove=False
startGameCheck = False
moves = 0

master=Tk()
f = Frame(master, height=300, width=300)


def makeGUIMove(pos,board,letter):
    #To make the relevant move and also update the GUI accordingly
    makeMove(letter,board,pos)
    if letter is playerLetter:
        b[pos].config(text=letter,disabledforeground=playerColor)
    else:
        b[pos].config(text=letter,disabledforeground=AIColor)
    b[pos].config(state=DISABLED)
    #Check if winner as well!
    pass

def checkDraw():
    global moves
    if moves>=9:
        tkinter.messagebox.showinfo(title='Tic Tac Toe',message="It's a draw!")

def makeAIMove():
    global moves,playerMove
    move = getAIMove(gameBoard,AILetter)
    makeGUIMove(move,gameBoard,AILetter)
    playerMove=True
    moves = moves+1
    if isWinner(gameBoard,AILetter):
        tkinter.messagebox.showinfo(title='Tic Tac Toe',message="Oops! The AI wins!")
    else:
        checkDraw()

def onClick(id):
    global moves
    if not startGameCheck:
        startGame()
        return
    global playerMove
    if playerMove and isSpaceFree(id,gameBoard):
        playerMove=False
        makeGUIMove(id,gameBoard,playerLetter)
        moves = moves+1

        if isWinner(gameBoard,playerLetter):
            tkinter.messagebox.showinfo(title='Tic Tac Toe',message="You Win!")
        else:
            checkDraw()
            makeAIMove()
            #check for winner
    else:
        #Do Something maybe
        pass

def __init__():
    global gameBoard
    #Initial setup of game board
    f.grid()
    for i in range(1,10):
        gameBoard[i]=str(i)
        var[i]=Variable(value=0)
        b[i] = Button(f,text=str(i),command= lambda id=i:onClick(id), width=8, height=4)
        #b[i].pack(fill=BOTH,expand=1)
        if i in range(1,4):
            b[i].grid(row=2,column=i-1,)
        elif i in range(4,7):
            b[i].grid(row=1,column=i-4)
        else:
            b[i].grid(row=0,column=i-7)
#Starting here
def startGame():
    global moves
    global playerMove
    global startGameCheck
    startGameCheck=True
    #starts the logical part of the game
    #We assume right now that the player starts first and is X (RED)
    moves=0
    current = 0 #0 for player, 1 for AI

    '''while True:
        if moves>=9:
            t=Message(master,text="Its a DRAW!")
            t.pack()
            break'''

    if current==0:
        playerMove=TRUE
    else:
        playerMove=False
            

 #Calls mainloop for GUI setup. Should only be called once
__init__() #Inirial setup
mainloop()

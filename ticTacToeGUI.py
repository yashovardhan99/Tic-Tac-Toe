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

def restartGame():
    global gameBoard,moves,b,var,playerMove,startGameCheck
    for i in range(1,10):
        gameBoard[i]=str(i)
        var[i]=Variable(value=0)
        b[i].config(text=str(i),state=NORMAL)
    playerMove=False
    startGameCheck=False
    moves=0
    startGame()


def __init__():
    global gameBoard,master
    #Initial setup of game board
    for i in range(1,10):
        gameBoard[i]=str(i)
        var[i]=Variable(value=0)
        b[i] = Button(master,text=str(i),font={"arial",10,"bold"},padx=2,pady=2,overrelief=RIDGE,command= lambda id=i:onClick(id))
        #b[i].pack(fill=BOTH,expand=1)
        if i in range(1,4):
            b[i].grid(row=2,column=i-1,sticky=NSEW)
        elif i in range(4,7):
            b[i].grid(row=1,column=i-4,sticky=NSEW)
        else:
            b[i].grid(row=0,column=i-7,sticky=NSEW)
    for i in range(3):
        Grid.columnconfigure(master,i,weight=1,minsize=80)
        Grid.rowconfigure(master,i,weight=1,minsize=80)
    menubar = Menu(master)
    menubar.add_command(label='Restart Game',command=restartGame)
    master.config(menu=menubar)
    master.title("Tic Tac Toe")
    startGame()

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

    if current==0:
        playerMove=TRUE
    else:
        makeAIMove()
        playerMove=False
            

 #Calls mainloop for GUI setup. Should only be called once
__init__() #Inirial setup
master.mainloop()
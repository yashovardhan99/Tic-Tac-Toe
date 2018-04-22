from tkinter import *
from ticTacToe import getAIMove,isWinner,isSpaceFree,makeMove

b = ['']*10
var = ['']*10
gameBoard = ['']*10
playerLetter='X' #Change later
playerColor='red'#Will be able to change later
AIColor='blue'

def makeGUIMove(pos,board,letter):
    #To make the relevant move and also update the GUI accordingly
    makeMove(letter,board,pos)
    if letter is playerLetter:
        b[pos].config(text=letter,disabledforeground=playerColor)
    else:
        b[pos].config(Text=letter,fg=AIColor)
    b[pos].config(state=DISABLED)
    #Check if winner as well!
    pass

def onClick(id):
    if isSpaceFree(id,gameBoard):
        makeGUIMove(id,gameBoard,playerLetter)
        #Do something more?
        pass
    else:
        #Do Something maybe
        pass

def __init__():
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
master=Tk()
f = Frame(master, height=300, width=300)
__init__() #Inirial setup
mainloop() #Calls mainloop for GUI setup. Should only be called once
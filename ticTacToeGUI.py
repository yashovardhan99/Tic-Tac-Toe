from tkinter import *
from ticTacToe import makeAIMove,isWinner
def onClick(id):
    pass

def __init__():
    #Initial setup of game board
    f = Frame(master, height=300, width=300)
    f.pack()
    b = ['']*10
    var = ['']*10
    for i in range(1,10):
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
__init__()
mainloop()
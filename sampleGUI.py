'''This is testing the GUI implementation. It will soon be added to the appropriate methods'''
from tkinter import *
master = Tk()

def onClick(i):
    #Check if space is free
    #Check if user's turn
    print("TEST"+str(i))
    b[i].config(background='blue',state=DISABLED)
    b[i].destroy()


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
    
menubar = Menu(master)
menubar.add(itemType=COMMAND,foreground='green',label='New Game',command=onClick)
menubar.config(bg='blue',fg='red')
master.config(bg='darkblue',menu=menubar)
master.mainloop()

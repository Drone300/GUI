import tkinter as tk
from tkinter import *
from BLackJack import table

def button(win):
    frame = Frame(win)
    frame.pack()
    bottomframe = Frame(win)
    bottomframe.pack( side = BOTTOM )
    blackbutton = Button(bottomframe, text = 'BlackJack', fg ='Black', font="Arial", command=table)
    blackbutton.pack( side = LEFT)
    greenbutton = Button(bottomframe, text = 'Solitaire', fg='olive', font="Arial")
    greenbutton.pack( side = LEFT )
    redbutton = Button(bottomframe, text ='BattleShip', fg ='DarkRed',font="Arial")
    redbutton.pack( side = LEFT )
def main():
    win = tk.Tk()
    bg = PhotoImage(file="Blavck Hole 1.png")
    label1 = Label(win, image=bg)
    label1.place(x=0, y=0)
    win.title('Retro Arcade')
    win.geometry("500x600")
    win.resizable(0,0)
    menu = Menu(win)
    win.config(menu=menu)
    button(win)
    win.mainloop()

main()

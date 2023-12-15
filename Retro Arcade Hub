import tkinter as tk
from tkinter import *

def gui(win):
    menu = Menu(win)
    win.config(menu=menu,background="green")
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command=main)
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=win.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')

def button(win):
    frame = Frame(win)
    frame.pack()
    bottomframe = Frame(win)
    bottomframe.pack( side = BOTTOM )
    redbutton = Button(bottomframe, text = 'BJ', fg ='Black', font="Arial")
    redbutton.pack( side = LEFT)
    greenbutton = Button(bottomframe, text = 'Solitaire', fg='olive', font="Arial")
    greenbutton.pack( side = LEFT )
    bluebutton = Button(bottomframe, text ='BattleShip', fg ='DarkRed',font="Arial")
    bluebutton.pack( side = LEFT )

def main():
    win = tk.Tk()
    win.title('Retro Arcade')
    win.geometry("350x350")
    menu = Menu(win)
    win.config(menu=menu)
    gui(win)
    button(win)
    win.mainloop()

main()

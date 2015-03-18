import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk
import kingkong

class Menu(Frame):

    def __init__(mine,master = None):
        Frame.__init__(mine,master)

        mine.master = master

        mine.window()
        mine.show_button()    

    def window(mine):
        mine.master.title("King Kong")

        #load images
        background = PhotoImage(file ="bg.gif")
        king = PhotoImage(file = "king1.gif")
        mine.nextbackg = PhotoImage(file = "bg5.gif")
        mine.new_game_btn = PhotoImage(file ="play.gif")
        mine.new_gameh_btn = PhotoImage(file ="play1.gif")
        mine.help_btn = PhotoImage(file = "help.gif")
        mine.helph_btn = PhotoImage(file = "help1.gif")
        mine.exit_btn = PhotoImage(file = "quit.gif")
        mine.exith_btn = PhotoImage(file = "quit1.gif")
        mine.back_btn =PhotoImage (file = "back.gif")
        mine.backh_btn =PhotoImage (file = "back1.gif")
        mine.instruct_btn = PhotoImage(file = "helpp.gif")

        mine.pack(fill = BOTH, expand = 1)

        #display background
        mine.bg_img = Label(mine, image = background)
        mine.bg_img.image = background
        mine.bg_img.place(x=-2, y=-2)

        mine.bg2_img = Label(mine, image = king)
        mine.bg2_img.image = king
        mine.bg2_img.place(x=580, y=420)

    def show_button(mine):
        #displaying of buttons
        mine.btn_ng = Button(mine, bd=0, bg="black", image = mine.new_game_btn, command = mine.new_game)
        mine.btn_ng.configure(image = mine.new_game_btn)
        mine.btn_ng.place(x=0, y = 450)
        mine.btn_ng.bind('<Enter>', mine.btn_ngEnter)
        mine.btn_ng.bind('<Leave>', mine.btn_ngLeave)

        mine.btn_help = Button(mine, bd=0, bg="black", image = mine.help_btn, command = mine.helps)
        mine.btn_help.configure(image = mine.help_btn)
        mine.btn_help.place(x=190, y =450)
        mine.btn_help.bind('<Enter>', mine.btn_helpEnter)
        mine.btn_help.bind('<Leave>', mine.btn_helpLeave)

        mine.btn_exit = Button(mine, bd=0, bg="black", image = mine.exit_btn, command = win.destroy)
        mine.btn_exit.configure(image = mine.exit_btn)
        mine.btn_exit.place(x=380, y = 450)
        mine.btn_exit.bind('<Enter>', mine.btn_exitEnter)
        mine.btn_exit.bind('<Leave>', mine.btn_exitLeave)

    def btn_ngEnter(mine, event):
        mine.btn_ng.configure(image = mine.new_gameh_btn)
    def btn_ngLeave(mine, event):
        mine.btn_ng.configure(image =mine.new_game_btn )

    def btn_helpEnter(mine, event):
        mine.btn_help.configure(image = mine.helph_btn)
    def btn_helpLeave(mine, event):
        mine.btn_help.configure(image =mine.help_btn )

    def btn_exitEnter(mine, event):
        mine.btn_exit.configure(image = mine.exith_btn)
    def btn_exitLeave(mine, event):
        mine.btn_exit.configure(image =mine.exit_btn )

    def btn_backEnter(mine, event):
        mine.back.configure(image = mine.backh_btn)
    def btn_backLeave(mine, event):
        mine.back.configure(image = mine.back_btn )
  

    def new_game(mine):
        kingkong.main()
        mine.master.withdraw()
        
    def nextback(mine, lbl):
        mine.window()
        mine.bg_img.configure(image = mine.nextbackg)
        
        mine.back= Button(mine, bd =0, bg = "blue", image = mine.back_btn, command = mine.back)
        mine.back.configure(image = mine.back_btn)
        mine.back.place(x =230, y = 445)
        mine.back.bind('<Enter>', mine.btn_backEnter)
        mine.back.bind('<Leave>', mine.btn_backLeave)

    def helps(mine):
        mine.nextback("help")

        img =PhotoImage(file = "helpp.gif")
        lbl = Label(mine, bd = 0, image = img)
        lbl.image = img
        lbl.place(x = 150, y = 50)

    def back(mine):
        mine.window()
        mine.show_button()

win = Tk()
win.geometry ("740x500")
win.resizable(0,0)

app = Menu(win)

win.mainloop ()


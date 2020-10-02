from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import os

Inp_score = 0
pc_score = 0
games = 0
mode = ['black', 'white', 'gray']
currentdir = os.path.dirname(os.path.realpath(__file__))   

class Root():
    def __init__(self):
        '''initialize a root widget'''
        self.root = Tk()
        self.root.title("Rock Paper Scissor")
        self.root.geometry("800x500")
        self.box = LabelFrame(self.root, bd=15, bg=mode[2], padx=5, pady=10)
        self.header = LabelFrame(self.box, bd=10, bg=mode[0], padx=40, width=100)
        self.guess = LabelFrame(self.box, bg=mode[0], fg=mode[1], bd=10, padx=5, pady=10)
        self.head = Label(self.header,text="ROCK PAPER SCISSOR", padx=40, pady=2, fg=mode[1], bg=mode[0], font=("Arial black", 25), justify=CENTER)
        self.score = Label(self.header, text="self.scoreBOARD:: Computer [{0}] vs YOU [{1}] of [{2}]".format(pc_score, Inp_score, games), padx=2, pady=2, font=("cambria", 14), justify="right", fg=mode[1], bg=mode[0])
        self.rock_icon = ImageTk.PhotoImage(image = Image.open(os.path.join(currentdir, "rock.png")))
        self.paper_icon = ImageTk.PhotoImage(image = Image.open(os.path.join(currentdir, "paper.png")))
        self.scissor_icon = ImageTk.PhotoImage(image = Image.open(os.path.join(currentdir, "scissor.png")))
        self.rock_lbl = Label(self.guess, padx=1, pady=2)
        self.paper_lbl = Label(self.guess, padx=1, pady=2)
        self.scissor_lbl = Label(self.guess, padx=1, pady=2)
        self.rock_btn = Button(self.rock_lbl, image=self.rock_icon, command= lambda: self.getInp("rock"))
        self.paper_btn =  Button(self.paper_lbl, image=self.paper_icon, command= lambda: self.getInp("paper"))
        self.scissor_btn =  Button(self.scissor_lbl, image=self.scissor_icon, command= lambda: self.getInp("scissor"))
        self.menu()
        self.rock_btn.pack()
        self.paper_btn.pack()
        self.scissor_btn.pack()
        self.rock_lbl.grid(row=0, column=1)
        self.paper_lbl.grid(row=0, column=0)
        self.scissor_lbl.grid(row=0, column=2)
        self.box.pack(padx=10, pady=5, side="top")
        self.header.pack(padx=5, pady=20)
        self.head.pack(side="top", padx=5)
        self.score.pack(side="bottom", padx=15, pady=4)
        self.guess.pack(padx=1, pady=1)
        self.root.config(menu=self.menubar)
        self.root.mainloop()

    def menu(self):
        '''
        menubar on game widget
        '''
        self.menubar = Menu(self.box, font=15, bd=5)
        self.settings = Menu(self.menubar, tearoff=0)

        self.settings.add_command(label="Dark Mode", command=lambda:self.setmode(0))
        self.settings.add_command(label="Bright Mode", command=lambda:self.setmode(1))

        self.menubar.add_command(label="New Game", command=lambda:self.newgame())
        self.menubar.add_cascade(label="self.settings", menu=self.settings)
        self.menubar.add_command(label="Help", command=lambda:self.helpwindow())
        self.menubar.add_command(label="Exit", command=self.root.destroy)

    def newgame(self):
        '''
        Initialize a New Game
        '''
        global mode, games, pc_score, Inp_score
        self.root.destroy()
        Inp_score = 0
        pc_score = 0
        games = 0
        self.createWindow()

    def helpwindow(self):
        howto = '''
    ROCK-PAPER-SCISSOR  is a simple luck based game where 

    you have three  choices -    ROCK, PAPER and SCISSOR. 

            Rock + Paper -> Paper
            Rock + Scissor -> Rock
            Paper + Scissor -> Scissor

    You can play unlimited  times  against  the  computer, 

    as  it is  a single player game. You can restart a new 

    game  by  selecting 'NEW GAME'  option in the menu bar  

    any time.

    ENJOY THE GAME. HAVE A GREAT TIME!!
    '''
        messagebox.showinfo("HOW TO PLAY", howto, parent=self.root)
        return self

    def setmode(self, choice):
        global mode, games, pc_score, Inp_score
        if choice:
            mode = ['white', 'black', 'white']
        else:
            mode=['black', 'white', 'gray']
        self.refresh()
        return self

    def createWindow(self):    
        '''Create New Game Window'''
        self.__init__()


    def getInp(self, Inp):
        '''take input from user'''
        global mode, games, pc_score, Inp_score
        pc = random.choice(['rock', 'paper', 'scissor'])
        games += 1
        if(pc == Inp):
            res = "GAME DRAWN!!"
        elif(pc == "rock"):
            if(Inp == "paper"):
                res = "YOU WON"
                Inp_score += 1
            else:
                res = "YOU LOST"
                pc_score += 1
        elif(pc == "paper"):
            if(Inp == "scissor"):
                res = "YOU WON"
                Inp_score += 1
            else:
                res = "YOU LOST"
                pc_score += 1
        elif(pc == "scissor"):
            if(Inp == "rock"):
                res = "YOU WON"
                Inp_score += 1
            else:
                res = "YOU LOST"
                pc_score += 1
        info = '''
    YOU       :   {0}
    COMPUTER  :   {1}
    '''.format(Inp.upper(), pc.upper())
        messagebox.showinfo(res, info, parent=self.root)
        self.refresh()

    def refresh(self):
        '''
        resets the game window
        '''
        self.root.destroy()
        self.createWindow()

Newgame = Root()
Newgame.createWindow()

from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import os

Inp_score = 0
pc_score = 0
games = 0
mode = ['black', 'white', 'gray']

def newgame(root):
    root.destroy()
    global Inp_score, pc_score, games
    Inp_score = 0
    pc_score = 0
    games = 0
    createWindow()

def helpwindow(root):
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
    msg = messagebox.showinfo("HOW TO PLAY", howto, parent=root)
    return

def setmode(choice, root):
    global mode
    if choice:
        mode = ['white', 'black', 'white']
    else:
        mode=['black', 'white', 'gray']
    refresh(root)
    return


def createWindow():    
    currentdir = os.path.dirname(os.path.realpath(__file__))   
    root = Tk()
    root.title("Rock Paper Scissor")
    root.geometry("800x500")
    global pc_score, Inp_score, games, newgame, helpwindow, mode

    box = LabelFrame(root, bd=15, bg=mode[2], padx=5, pady=10)
    header = LabelFrame(box, bd=10, bg=mode[0], padx=40, width=100)
    guess = LabelFrame(box, bg=mode[0], fg=mode[1], bd=10, padx=5, pady=10)

    head = Label(header,text="ROCK PAPER SCISSOR", padx=40, pady=2, fg=mode[1], bg=mode[0], font=("Arial black", 25), justify=CENTER)
    score = Label(header, text="SCOREBOARD:: Computer [{0}] vs YOU [{1}] of [{2}]".format(pc_score, Inp_score, games), padx=2, pady=2, font=("cambria", 14), justify="right", fg=mode[1], bg=mode[0])
    
    menubar = Menu(box, font=15, bd=5)
    settings = Menu(menubar, tearoff=0)

    settings.add_command(label="Dark Mode", command=lambda:setmode(0, root))
    settings.add_command(label="Bright Mode", command=lambda:setmode(1, root))

    menubar.add_command(label="New Game", command=lambda:newgame(root))
    menubar.add_cascade(label="Settings", menu=settings)
    menubar.add_command(label="Help", command=lambda:helpwindow(root))
    menubar.add_command(label="Exit", command=root.destroy)

    rock_icon = ImageTk.PhotoImage(image = Image.open(os.path.join(currentdir, "rock.png")))
    paper_icon = ImageTk.PhotoImage(image = Image.open(os.path.join(currentdir, "paper.png")))
    scissor_icon = ImageTk.PhotoImage(image = Image.open(os.path.join(currentdir, "scissor.png")))

    rock_lbl = Label(guess, padx=1, pady=2)
    paper_lbl = Label(guess, padx=1, pady=2)
    scissor_lbl = Label(guess, padx=1, pady=2)

    rock_btn = Button(rock_lbl, image=rock_icon, command= lambda: getInp("rock", root))
    paper_btn =  Button(paper_lbl, image=paper_icon, command= lambda: getInp("paper", root))
    scissor_btn =  Button(scissor_lbl, image=scissor_icon, command= lambda: getInp("scissor", root))

    rock_btn.pack()
    paper_btn.pack()
    scissor_btn.pack()

    rock_lbl.grid(row=0, column=1)
    paper_lbl.grid(row=0, column=0)
    scissor_lbl.grid(row=0, column=2)

    box.pack(padx=10, pady=5, side="top")
    header.pack(padx=5, pady=20)
    head.pack(side="top", padx=5)
    score.pack(side="bottom", padx=15, pady=4)
    guess.pack(padx=1, pady=1)
    root.config(menu=menubar)
    root.mainloop()


def getInp(Inp, root):
    global pc_score, Inp_score, score, games
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
    msg = messagebox.showinfo(res, info, parent=root)
    refresh(root)


def refresh(root):
    '''
    resets the root
    '''
    root.destroy()
    createWindow()


createWindow()



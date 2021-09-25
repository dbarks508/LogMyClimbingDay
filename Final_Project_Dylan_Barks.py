from tkinter import *
root = Tk()

def logAscent():
    running = eFive.get()
    eFive.delete(0, END)
    r = int(running)
    grade = eTwo.get()
    eFive.insert(0, r + int(grade) )

    attRunning = eSix.get()
    eSix.delete(0, END)
    aR = int(attRunning)
    tries = eThree.get()
    eSix.insert(0, aR + int(tries) )

    movesRunning = eSeven.get()
    eSeven.delete(0, END)
    mR = int(movesRunning)
    moves = eFour.get()
    eSeven.insert(0, mR + int(moves) )

    eOne.delete(0,END)
    eTwo.delete(0,END)
    eThree.delete(0,END)
    eFour.delete(0,END)
    



myLabel = Label(root, text="Welcome to log-my-climbing-day!")
lOne = Label(root, text="Boulder Name: ")
eOne = Entry(root)
lTwo = Label(root, text="v-grade: ")
eTwo = Entry(root)
lThree = Label(root, text="Number of attempts: ")
eThree = Entry(root)
lFour = Label(root, text="Number of moves: ")
eFour = Entry(root)
bOne = Button(root,text="Log ascent", command=logAscent)
bTwo = Button(root,text="show my day!")
my_Label = Label(root, text="RuNnInG ToTaLs")
lFive = Label(root, text="v-points:")
eFive = Entry(root)
eFive.insert(0, "0")
lSix = Label (root, text="Total attempts")
eSix = Entry(root)
eSix.insert(0, "0")
lSeven = Label(root, text="Total moves")
eSeven = Entry(root)
eSeven.insert(0,"0")




myLabel.pack()
lOne.pack()
eOne.pack()
lTwo.pack()
eTwo.pack()
lThree.pack()
eThree.pack()
lFour.pack()
eFour.pack()
bOne.pack()
my_Label.pack()
lFive.pack()
eFive.pack()
lSix.pack()
eSix.pack()
lSeven.pack()
eSeven.pack()
bTwo.pack()









root.mainloop()

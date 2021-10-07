"""
This module logs 'boulder problems' from a day of
climbing and returns statistics about the day
"""

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("300x700")
root.title("Log-my-climbing-day")
root.configure(bg="#EDF1FF")

#images
my_img = ImageTk.PhotoImage(Image.open("DylanDyno.jpg"))
other_img = ImageTk.PhotoImage(Image.open("whatsthescoop.jpg"))

#variable for tracking hardest climb
hardest = 0

def logAscent():
    """main function for logging ascents"""
    global hardest
    
    #v-grade running total
    running = eFive.get()
    eFive.delete(0, END)
    r = int(running)
    grade = eTwo.get()
    eFive.insert(0, r + int(grade) )

    #hardest boulder tracker
    latest = eTwo.get()
    if int(latest) >= int(hardest):
        hardest = latest
        
    #attempts running total
    attRunning = eSix.get()
    eSix.delete(0, END)
    aR = int(attRunning)
    tries = eThree.get()
    eSix.insert(0, aR + int(tries) )
    
    #moves running total
    movesRunning = eSeven.get()
    eSeven.delete(0, END)
    mR = int(movesRunning)
    moves = eFour.get()
    eSeven.insert(0, mR + int(moves) )

    #logs the names of all boulders
    name = eOne.get()
    eEight.insert(0, str(name) + " || ")
    
def count():
    """counts the number of boulders"""
    c = eNine.get()
    eNine.delete(0, END)
    count = int(c)
    count += 1
    eNine.insert(0, count)

def clear():
    """clears the entry fields"""
    eOne.delete(0,END)
    eTwo.delete(0,END)
    eThree.delete(0,END)
    eFour.delete(0,END)

def goTo():
    """second window function"""
    top = Toplevel()
    top.title("Statistics")
    top.configure(bg="#97A192")

    #computes average v points
    clmbs = eNine.get()
    vtotal = eFive.get()
    avg = int(vtotal) / int(clmbs)

    #gets total attempts
    atts = eSix.get()

    #gets total number of climbs
    boulders = eNine.get()

    #gets names of climbs
    names = eEight.get()

    #gets total number of moves
    mvs = eSeven.get()

    #window two widgets
    lbl = Label(top, text="Check your stats!!")
    lblOne = Label(top, text= "Your average v-grade was v-" + str(avg))
    lblTwo = Label(top, text= "Your hardest boulder was v-" + str(hardest))
    lblThree = Label(top, text= "You took " + str(atts) +
                     " attempts over "+ str(boulders)+ " boulders!")
    lblFour = Label(top,text = "You climbed a total of " + str(mvs) +
                    " moves over " + str(boulders) + " boulders!")
    lblFive = Label(top,text = "These are the names of the boulders you climbed: "
                    + str(names))
    picture = Label(top, image=other_img)
    btn = Button(top, text="close window", command=top.destroy)

    #configures window two widgets
    lbl.pack()
    lblOne.pack()
    lblTwo.pack()
    lblThree.pack()
    lblFour.pack()
    lblFive.pack()
    picture.pack()
    btn.pack()

def reset():
    """resets the first window for a new set of entries"""
    global hardest
    eFive.delete(0,END)
    eSix.delete(0,END)
    eSeven.delete(0,END)
    eEight.delete(0,END)
    eNine.delete(0, END)
    eFive.insert(0, "0")
    eSix.insert(0, "0")
    eSeven.insert(0,"0")
    eNine.insert(0, "0")
    hardest = 0

#widgets in main window
myLabel = Label(root, text="Welcome to log-my-climbing-day!")
pic = Label(root, image=my_img)
lOne = Label(root, text="Boulder Name: ")
eOne = Entry(root)
lTwo = Label(root, text="v-grade: ")
eTwo = Entry(root)
lThree = Label(root, text="Number of attempts: ")
eThree = Entry(root)
lFour = Label(root, text="Number of moves: ")
eFour = Entry(root)
bOne = Button(root,text="Log ascent",
              command=lambda: [logAscent(), clear(), count()])
my_Label = Label(root, text="RuNnInG ToTaLs")
lFive = Label(root, text="v-points:")
eFive = Entry(root)
eFive.insert(0, "0")
lSix = Label (root, text="Total attempts:")
eSix = Entry(root)
eSix.insert(0, "0")
lSeven = Label(root, text="Total moves:")
eSeven = Entry(root)
eSeven.insert(0,"0")
lEight = Label(root, text="Boulders:")
eEight = Entry(root)
lNine = Label(root, text="Total climbs")
eNine = Entry(root)
eNine.insert(0, "0")
bTwo = Button(root,text="show my day!", command= lambda:[goTo(), reset()])

#configures widgets in main window
myLabel.pack()
pic.pack()
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
lEight.pack()
eEight.pack()
lNine.pack()
eNine.pack()
bTwo.pack()

root.mainloop()

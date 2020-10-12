# File that creates a usable GUI for the program
from tkinter import *

def mainFrame():
    # This is just to separate this frame from the second one,
    #which has the equation and the answer box

    # Initialize the tkinter object along with its size
    root = Tk()
    root.geometry("1000x600")
    mainFrame = Frame(root)
    mainFrame.pack()

    # Frame label
    nameLabel = Label(mainFrame, text = "Board")
    nameLabel.grid(row=0,columnspan=10)

    # Placeholder text for the buttons, they can change according to the
    # other code, if we want to make it fancy

    # Board buttons for choosing the question
    button1 = Button(mainFrame, text="A1")
    button1.grid(row=1, column=0)

    button2 = Button(mainFrame, text="A2")
    button2.grid(row=1, column=1)

    button3 = Button(mainFrame, text="A3")
    button3.grid(row=1, column=2)

    button4 = Button(mainFrame, text="A4")
    button4.grid(row=1, column=3)

    button5 = Button(mainFrame, text="A5")
    button5.grid(row=1, column=4)

    button6 = Button(mainFrame, text="B1")
    button6.grid(row=2, column=0)

    button7 = Button(mainFrame, text="B2")
    button7.grid(row=2, column=1)

    button8 = Button(mainFrame, text="B3")
    button8.grid(row=2, column=2)

    button9 = Button(mainFrame, text="B4")
    button9.grid(row=2, column=3)

    button10 = Button(mainFrame, text="B5")
    button10.grid(row=2, column=4)

    button11 = Button(mainFrame, text="C1")
    button11.grid(row=3, column=0)

    button12 = Button(mainFrame, text="C2")
    button12.grid(row=3, column=1)

    button13 = Button(mainFrame, text="C3")
    button13.grid(row=3, column=2)

    button14 = Button(mainFrame, text="C4")
    button14.grid(row=3, column=3)

    button15 = Button(mainFrame, text="C5")
    button15.grid(row=3, column=4)

    button16 = Button(mainFrame, text="D1")
    button16.grid(row=4, column=0)

    button17 = Button(mainFrame, text="D2")
    button17.grid(row=4, column=1)

    button18 = Button(mainFrame, text="D3")
    button18.grid(row=4, column=2)

    button19 = Button(mainFrame, text="D4")
    button19.grid(row=4, column=3)

    button20 = Button(mainFrame, text="D5")
    button20.grid(row=4, column=4)

    button21 = Button(mainFrame, text="E1")
    button21.grid(row=5, column=0)

    button22 = Button(mainFrame, text="E2")
    button22.grid(row=5, column=1)

    button23 = Button(mainFrame, text="E3")
    button23.grid(row=5, column=2)

    button24 = Button(mainFrame, text="E4")
    button24.grid(row=5, column=3)

    button25 = Button(mainFrame, text="E5")
    button25.grid(row=5, column=4)

    # Running the GUI
    root.title("Equation Jeopardy")
    root.mainloop()

    return 0


def answerFrame():
    # Second Frame where the answer box is located, does not need to be inside a function
    #Only to separate it from the first Frame
    
    #initialize the frame
    answerRoot = Tk()
    answerRoot.geometry("500x300")
    answerFrame = Frame(answerRoot)
    answerFrame.pack()
    
    #label
    answerLabel = Label(answerFrame, text="Answer")
    answerLabel.grid(row=0, columnspan=10)
    
    #Answer box and confirm button.
    #Still need to add the function the button will do once pressed
    answerButton = Button(answerFrame, text="Submit answer")
    answerButton.grid(row=3, column=7,columnspan=3)
    
    dataEntry = Entry(answerFrame ''', command=function we want it to do''')
    dataEntry.grid(row=3, column=0, columnspan=4)
    
    return 0

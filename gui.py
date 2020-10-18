import tkinter as tk
import game

global root, frame, leftFrame, rightFrame

# this outside section creates the skeleton of the window,
# the main Frame and the two side Frames that are located within it
root = tk.Tk()
root.geometry('500x500')

frame = tk.Frame(root)
frame.pack()

leftFrame = tk.Frame(frame,bd=10)
leftFrame.pack(fill='y',side='left',pady=10,padx=10)

rightFrame = tk.Frame(frame,bd=10)
rightFrame.pack(fill='y',side='right',pady=10,padx=10)

# affects the left side Frame, as it is a grid of buttons that 
# equates to the display board
class Board:
    
    global root, frame, leftFrame, rightFrame

    def __init__(self):
        self.text = ''

    #####

    # changes coordinate of a button to 'x' once pressed
    def coord_remove(self, button):
        button.set('x')

    #####
    
    # creates the buttons for the board
    # no need to re-run it every time to update coordinates to 'x'
    # supposedly the StringVar() type updates the tk objects automatically
    def genBoard(self):
        b1 = tk.StringVar()
        b1.set('A1')
        button1 = tk.Button(leftFrame, textvariable=b1)
        button1.grid(row=1, column=0)
        
        b2 = tk.StringVar()
        b2.set('A2')
        button2 = tk.Button(leftFrame, textvariable=b2)
        button2.grid(row=1, column=1)

        b3 = tk.StringVar()
        b3.set('A3')
        button3 = tk.Button(leftFrame, textvariable=b3)
        button3.grid(row=1, column=2)

        b4 = tk.StringVar()
        b4.set('A4')
        button4 = tk.Button(leftFrame, textvariable=b4)
        button4.grid(row=1, column=3)
        
        b5 = tk.StringVar()
        b5.set('A5')
        button5 = tk.Button(leftFrame, textvariable=b5)
        button5.grid(row=1, column=4)

        b6 = tk.StringVar()
        b6.set('B1')
        button6 = tk.Button(leftFrame, textvariable=b6)
        button6.grid(row=2, column=0)

        b7 = tk.StringVar()
        b7.set('B2')
        button7 = tk.Button(leftFrame, textvariable=b7)
        button7.grid(row=2, column=1)
        
        b8 = tk.StringVar()
        b8.set('B3')
        button8 = tk.Button(leftFrame, textvariable=b8)
        button8.grid(row=2, column=2)

        b9 = tk.StringVar()
        b9.set('B4')
        button9 = tk.Button(leftFrame, textvariable=b9)
        button9.grid(row=2, column=3)

        b10 = tk.StringVar()
        b10.set('B5')
        button10 = tk.Button(leftFrame, textvariable=b10)
        button10.grid(row=2, column=4)
        
        b11 = tk.StringVar()
        b11.set('C1')
        button11 = tk.Button(leftFrame, textvariable=b11)
        button11.grid(row=3, column=0)

        b12 = tk.StringVar()
        b12.set('C2')
        button12 = tk.Button(leftFrame, textvariable=b12)
        button12.grid(row=3, column=1)

        b13 = tk.StringVar()
        b13.set('C3')
        button13 = tk.Button(leftFrame, textvariable=b13)
        button13.grid(row=3, column=2)
        
        b14 = tk.StringVar()
        b14.set('C4')
        button14 = tk.Button(leftFrame, textvariable=b14)
        button14.grid(row=3, column=3)

        b15 = tk.StringVar()
        b15.set('C5')
        button15 = tk.Button(leftFrame, textvariable=b15)
        button15.grid(row=3, column=4)

        b16 = tk.StringVar()
        b16.set('D1')
        button16 = tk.Button(leftFrame, textvariable=b16)
        button16.grid(row=4, column=0)
        
        b17 = tk.StringVar()
        b17.set('D2')
        button17 = tk.Button(leftFrame, textvariable=b17)
        button17.grid(row=4, column=1)

        b18 = tk.StringVar()
        b18.set('D3')
        button18 = tk.Button(leftFrame, textvariable=b18)
        button18.grid(row=4, column=2)

        b19 = tk.StringVar()
        b19.set('D4')
        button19 = tk.Button(leftFrame, textvariable=b19)
        button19.grid(row=4, column=3)
        
        b20 = tk.StringVar()
        b20.set('D5')
        button20 = tk.Button(leftFrame, textvariable=b20)
        button20.grid(row=4, column=4)

        b21 = tk.StringVar()
        b21.set('E1')
        button21 = tk.Button(leftFrame, textvariable=b21)
        button21.grid(row=5, column=0)

        b22 = tk.StringVar()
        b22.set('E2')
        button22 = tk.Button(leftFrame, textvariable=b22)
        button22.grid(row=5, column=1)
        
        b23 = tk.StringVar()
        b23.set('E3')
        button23 = tk.Button(leftFrame, textvariable=b23)
        button23.grid(row=5, column=2)

        b24 = tk.StringVar()
        b24.set('E4')
        button24 = tk.Button(leftFrame, textvariable=b24)
        button24.grid(row=5, column=3)

        b25 = tk.StringVar()
        b25.set('E5')
        button25 = tk.Button(leftFrame, textvariable=b25)
        button25.grid(row=5, column=4)

        # this runs the gui, but I've no idea whether to put it here or in game.py
        # root.title("Equation Jeopardy")
        # root.mainloop()

    #####

#######

# this manages the right side Frame, that displays the equation and 
# takes in the answer via an Entry box widget
class Answer:

    global root, frame, leftFrame, rightFrame

    def __init__(self):
        self.question = ''
        self.answer = ''

    #####

    # this is supposed to run every time a button on the board is pressed,
    # essentially generating new content inside the Frame each time
    def genAnswerFrame(self):
        global eqText

        questionLabel = tk.Label(rightFrame,text='Pregunta')
        questionLabel.pack()

        eqText = tk.StringVar()
        equationLabel = tk.Label(rightFrame,textvariable=eqText)
        equationLabel.pack()

        answerLabel = tk.Label(rightFrame,text='Respuesta')
        answerLabel.pack(pady=10)

        entry=tk.Entry(rightFrame)
        entry.pack()

        confirmButton = tk.Button(rightFrame,text='Submit answer',command=self.confirmAnswer(entry))
        confirmButton.pack()

    #####

    # this deletes the previous text from the Entry box, just for asthetics
    def resetLabels(self):
        global eqText

        eqText.set('')

    #####
    
    # this is supposed to get the correspoding equation from game.py
    # and display it
    ## still have to connect the game to the gui

    def setEquation(self):
        global eqText

        eqText.set(self.question)

    #####
    
    # this runs when the confirm button is pressed, all it does is update the value 
    # of answer to what is written in the Entry box
    ## still have to connect the game to the gui
    def confirmAnswer(self, entry):
        self.answer = entry.get()
    
    #####

    # this is here to send the entered answer to game.py so that that can 
    # send it to boards.py and check if it's correct or not
    # it runs after confirmAnswer() has put the value into the variable
    ## still have to connect the game to the gui
    def sendAnswer(self):
        return self.answer
    
    #####

#######

#########
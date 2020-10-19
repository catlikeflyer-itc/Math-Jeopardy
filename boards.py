from random import choice
import csv
import re

# display_board is the one the user can see,
# the secret_board are the problems hidden behind
# the options in the visible board.

# class tha encapsulates the formation of the visible and problem boards 
class GameBoard:
    def __init__(self):
        self.display_board = []
        self.secret_board = []

    # creates the visible board
    def generate_display_board(self):
        j = 0

        # creates a series of 25 string which are deposited into display_board 
        for x in range(1,6):
            self.display_board.append([])

            for i in 'ABCDE':
                self.display_board[j].append(str(x)+i)

            j += 1
        
        return self.display_board

    # creates the secret board, the problems
    def generate_secret_board(self, file):
        c = 0

        # gets a list of equations form a .csv file
        with open(file, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        # places those equations in a board, similar to the 
        # display_board creation process
        for i in range(0,5):
            self.secret_board.append([])

            for j in range(0,5):
                self.secret_board[c].append(choice(data)[0])
            c += 1
        
        return self.secret_board

    # removes already selected coordenates by replacing the text with an 'x'
    def remove_coord(self, row, column):
        self.display_board[row][column] = 'x'

# class that encapsulates the problem-solution revision
class Problem:
    answer = None

    def __init__(self, choice, dboard, sboard):
        for row in dboard:
            for i in row:
                if i == choice:
                    self.row = dboard.index(row)
                    self.column = row.index(i)
        
        self.problem = sboard[self.row][self.column]

    # function that calculates the answer
    def get_answer(self):
        lis = re.split(r'(\D)', self.problem)

        for i in range(len(lis)):
            if lis[i] == "+":
                self.answer = int(lis[i-1])+int(lis[i+1])
                return int(lis[i-1])+int(lis[i+1])

            elif lis[i] == "-":
                self.answer = int(lis[i-1])-int(lis[i+1])
                return int(lis[i-1])-int(lis[i+1])

            elif lis[i] == "*":
                self.answer = int(lis[i-1])*int(lis[i+1])
                return int(lis[i-1])*int(lis[i+1])  

            elif lis[i] == "/":
                self.answer = int(lis[i-1])/int(lis[i+1])
                return int(lis[i-1])/int(lis[i+1])  
    
    # compares answer with user's answer
    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False



        
                


                
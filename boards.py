from random import choice
import csv
import regex as re

# Initialize boards and counters
"""
El display board es el que el usuario puede ver, el secret board son los problemas que se esconden detras
del display board.
"""

class GameBoard:
    def __init__(self):
        self.display_board = []
        self.secret_board = []

# Create board to display
    def generate_display_board(self):
        j = 0

        for x in range(1,6):
            self.display_board.append([])

            for i in 'ABCDE':
                self.display_board[j].append(str(x)+i)

            j += 1
        
        return self.display_board

    # Create secret board with problems
    def generate_secret_board(self, file):
        c = 0

        # Obtain list of equations from CSV file
        with open(file, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        for i in range(0,5):
            self.secret_board.append([])

            for j in range(0,5):
                self.secret_board[c].append(choice(data)[0])
            c += 1
        
        return self.secret_board

    # Removes already selected coordenates
    def remove_coord(self, row, column):
        self.display_board[row][column] = 'x'

class Problem:
    answer = None

    def __init__(self, choice, dboard, sboard):
        for row in dboard:
            for i in row:
                if i == choice:
                    self.row = dboard.index(row)
                    self.column = row.index(i)
        
        self.problem = sboard[self.row][self.column]

    # Function that calculates the answer
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
    
    # Compares answer with user's answer
    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False



        
                


                
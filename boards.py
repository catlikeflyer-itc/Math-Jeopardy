from random import choice
import csv
import regex as re

# Initialize boards and counters
"""
El display board es el que el usuario puede ver, el secret board son los problemas que se esconden detras
del display board.
"""
display_board = []
secret_board = []

# Create board to display
def generate_display_board():
    j = 0

    for x in range(1,6):
        display_board.append([])

        for i in 'ABCDE':
            display_board[j].append(str(x)+i)

        j += 1
    
    return display_board

# Create secret board with problems
def generate_secret_board():
    c = 0

    # Obtain list of equations from CSV file
    with open('equation.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for i in range(0,5):
        secret_board.append([])

        for j in range(0,5):
            secret_board[c].append(choice(data)[0])
        c += 1
    
    return secret_board

# Retrieves the problem/equation behind the coordenates given by the user
def get_problem(choice, dboard, sboard):
    row_ = None
    column = None

    for row in dboard:
        for i in row:
            if i == choice:
                row_ = dboard.index(row)
                column = row.index(i)
    
    return sboard[row_][column]

class Problem:
    answer = None

    def __init__(self, choice, dboard, sboard):
        for row in dboard:
            for i in row:
                if i == choice:
                    self.row = dboard.index(row)
                    self.column = row.index(i)
        
        self.problem = sboard[self.row][self.column]

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
        
    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False

        
                


                
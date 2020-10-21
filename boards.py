from random import choice
import csv
import re

# Clase para el tablero del juego
class GameBoard:
    def __init__(self):
        self.display_board = []
        self.secret_board = []

    # Metodo para crear la matriz visible
    def generate_display_board(self):
        j = 0

        # Iterar para crear una matriz 5x5
        for x in range(1,6):
            self.display_board.append([])

            for i in 'ABCDE':
                self.display_board[j].append(str(x)+i)

            j += 1
        
        return self.display_board

    # Metodo para crear matriz no visible que contiene las preguntas
    def generate_secret_board(self):
        c = 0
        
        # Generar listas con las preguntas de acuerdo al nivel, estas estan escritas en archivos csv
        with open('easy.csv', newline='') as f:
            reader = csv.reader(f)
            easy = list(reader)
        
        with open('medium.csv', newline='') as f1:
            reader1 = csv.reader(f1)
            medium = list(reader1)
        
        with open('hard.csv', newline='') as f2:
            reader2 = csv.reader(f2)
            hard = list(reader2)

        # Agrega de manera aleatoria las preguntas en la matriz no visible, de acuerdo al nivel
        # Genera las filas
        for i in range(0,5):
            self.secret_board.append([])

        # Poblar las primeras dos filas con preguntas faciles
        for c in range(0,2):
            for j in range(0,5):
                self.secret_board[c].append(choice(easy)[0])
        
        # Poblar la tercera y cuarta fila con preguntas medianas
        for c in range(2,4):
            for j in range(0,5):
                self.secret_board[c].append(choice(medium)[0])
        
        # Poblar ultima fila con preguntas dificiles
        for j in range(0,5):    
            self.secret_board[4].append(choice(hard)[0])

        return self.secret_board

    # Elimina las coordenas que ya seleccionaron por una x
    def remove_coord(self, row, column):
        self.display_board[row][column] = 'x'

# Clase para el problema detras de la coordenada
class Problem:
    answer = None

    def __init__(self, choice, dboard, sboard):

        # Obtencion de la pregunta
        for row in dboard:
            for i in row:
                if i == choice:
                    self.row = dboard.index(row)
                    self.column = row.index(i)
        
        self.problem = sboard[self.row][self.column]

        # Asignacion de puntos dependiendo del nivel
        if '1' in choice or '2' in choice:
            self.points = 3
        elif '3' in choice or '4' in choice:
            self.points = 5
        elif '5' in choice:
            self.points = 10   

    # Funcion que calcula el resultado
    def get_answer(self):
        lis = re.split(r'(\D)', self.problem)

        for i in range(len(lis)):
            if lis[i] == "+":
                self.answer = float(lis[i-1])+float(lis[i+1])
                return float(lis[i-1])+float(lis[i+1])

            elif lis[i] == "-":
                self.answer = float(lis[i-1])-float(lis[i+1])
                return float(lis[i-1])-float(lis[i+1])

            elif lis[i] == "*":
                self.answer = float(lis[i-1])*float(lis[i+1])
                return float(lis[i-1])*float(lis[i+1])  

            elif lis[i] == "/":
                self.answer = float(lis[i-1])/float(lis[i+1])
                return float(lis[i-1])/float(lis[i+1])  
    
    # Compara el resultado del problema con el ingresado por el usuario, regresa un booleano
    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False




        
                


                
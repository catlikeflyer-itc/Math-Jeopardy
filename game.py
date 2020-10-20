from boards import GameBoard, Problem
import time
import threading
import sys

# Funcion para mostrar las intrucciones
def instrucciones():
    print('Bienvenido a GEM')
    print('"Giopardy de Estimulación Matemática"')
    print("No tiene ninguna relación con el famoso show")
    print("Instrucciones: \n1. Escribe la coordenada que quieras contestar, el nivel aumenta de arriba hacia abajo.\n2.Escribe la respuesta correcta con numeros.\n3.Llega a los 30 puntos en 90 segundos, el puntaje aumenta de acuerdo a la dificultad.")
    while True:
        start = input('Presione ENTER para comenzar')

        if start == '':
            return False
        else:
            continue

# Funcion que guarda el juego
def game():
    
    # Iniciar objeto de tablero
    board = GameBoard()
    
    # Generar los tableros
    show_board = board.generate_display_board()
    secret_board = board.generate_secret_board()
    
    # Lista que guarda las coordenadas ya electas
    solved = []

    # Acumulador de puntos
    points = 0

    # Loop que continua hasta alcanzar al puntaje maximo
    while points < 30:
        
        # Imprime la tabla visible
        for i in show_board:
            print(i,'\n')
        
        # Ingreso de coordenadas
        user_choice = input('Enter coordenates: ')

        # Repite pregunta si la coordenada ya esta resuelta
        while user_choice in solved:

            print('Coordenate already solved')
            user_choice = input('Enter coordenates: ')     
        
        # ASCII check
        while(len(user_choice) != 2 or ord(user_choice[1]) < 65 or ord(user_choice[1]) > 69 or ord(user_choice[0]) < 49 or ord(user_choice[0]) > 53 ):
            print(points)
            user_choice = input('Enter coordenates: ')
        
        # Agregar coordenada resuelta a lista
        solved.append(user_choice)

        # Crea el objeto de problema que esta en la coordenada que ingreso el usuario
        problem = Problem(user_choice.upper(), show_board, secret_board)

        # Imprime el problema y el puntaje
        print(problem.problem)
        print(f'Puntos: {points}')

        # Pregunta al usuario por su respuesta
        user_answer = int(input('Resultado >>> '))
        # Calcular respuesta internamente
        problem.get_answer()

        # Si la respuesta es correcta, se suman puntos dependiendo del nivel
        if problem.check_answer(user_answer):
            print(problem.check_answer(user_answer))
            points += problem.points
        else:
            print(problem.check_answer(user_answer))

        # Cambia la coordenada electa por una x en la tabla visible
        board.remove_coord(problem.row, problem.column)
    
    # Si llega a los 30 puntos, gana
    print('Ganaste!')

if __name__ == "__main__":

    # Imprime instrucciones
    instrucciones()

    # Fija temporizador
    timeout = 90
    # Imprime que se acabo el tiempo, y termina la ejecucion
    t = threading.Timer(timeout, print, ["bruh, time's up"])
    t.start()

    # Correr juego
    game()


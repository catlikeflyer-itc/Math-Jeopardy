from boards import GameBoard, Problem
import time
import threading
import sys

def game():
# Initialize gameboard
    board = GameBoard()
    show_board = board.generate_display_board()
    secret_board = board.generate_secret_board('equation.csv')
    #lista que guarda coordenadas usadas
    solved = []
    # Points counter
    points = 0

    # If max points is reached, stops
    while points < 3:
        for i in show_board:
            print(i,'\n')

        user_choice = input('Enter coordenates: ')
        while user_choice in solved:
            #estas bien meco  check
            print('Coordenate already solved')
            user_choice = input('Enter coordenates: ')     
        #ASCII check
        while(len(user_choice) != 2 or ord(user_choice[1]) < 65 or ord(user_choice[1]) > 69 or ord(user_choice[0]) < 49 or ord(user_choice[0]) > 53 ):
            print(points)
            user_choice = input('Enter coordenates: ')
        solved.append(user_choice)
        problem = Problem(user_choice.upper(),show_board,secret_board)

        print(problem.problem)

        user_answer = int(input('Resultado >>> '))
        problem.get_answer()

        if problem.check_answer(user_answer):
            print(problem.check_answer(user_answer))
            points += 1
        else:
            print(problem.check_answer(user_answer))

        board.remove_coord(problem.row, problem.column)
    print('Ganaste!')
#threads y timeout
timeout = 60
t = threading.Timer(timeout, print, ["bruh, time's up"])
t.start()
game()






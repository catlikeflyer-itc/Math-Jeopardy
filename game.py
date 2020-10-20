from boards import GameBoard, Problem
import time
import threading
import sys

def game():
    
    # initialize the object board as a GameBoard from boards.py
    board = GameBoard()
    
    # generate the secret_board and display_board atributes 
    # within the 'board' object instance
    show_board = board.generate_display_board()
    secret_board = board.generate_secret_board('equation.csv')
    
    # list that holds the solved coordinates
    solved = []

    # point counter
    points = 0

    # repeats until points reaches a value of 2
    while points < 3:
        
        # reprints the board each iteration
        for i in show_board:
            print(i,'\n')
        
        # coordinate input, i.e. a1, b5, etc
        user_choice = input('Enter coordenates: ')

        # repeats if the introduced coordinate is in the solved coordinates list
        while user_choice in solved:
            print('Coordenate already solved')
            
            # asks the user to input the coordinate again, until it's not one in the list
            user_choice = input('Enter coordenates: ')     
        
        #ASCII check
        while(len(user_choice) != 2 or ord(user_choice[1]) < 65 or ord(user_choice[1]) > 69 or ord(user_choice[0]) < 49 or ord(user_choice[0]) > 53 ):
            print(points)
            user_choice = input('Enter coordenates: ')
        
        # adds the inputed coordinate into the solved coordinates list
        solved.append(user_choice)

        # creates a Problem type object from boards.py with the atributes it needs
        problem = Problem(user_choice.upper(),show_board,secret_board)

        # prints the equation to solve
        print(problem.problem)

        user_answer = int(input('Resultado >>> '))
        problem.get_answer()

        # compares the user answer input with the actual answer using 
        # a method from the class Problem from boards.py
        if problem.check_answer(user_answer):
            print(problem.check_answer(user_answer))
            points += 1
        else:
            print(problem.check_answer(user_answer))

        # switches the printed coordinate with an x
        board.remove_coord(problem.row, problem.column)
    
    print('Ganaste!')

#threads y timeout
timeout = 60
t = threading.Timer(timeout, print, ["bruh, time's up"])
t.start()

game()

#####
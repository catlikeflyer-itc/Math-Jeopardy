from boards import GameBoard, Problem

# Initialize gameboard
board = GameBoard()
show_board = board.generate_display_board()
secret_board = board.generate_secret_board('equation.csv')

# Points counter
points = 0

# If max points is reached, stops
while points < 3:
    for i in show_board:
        print(i,'\n')

    user_choice = input('Enter coordenates: ')
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








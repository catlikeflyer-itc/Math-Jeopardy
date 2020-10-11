from boards import generate_secret_board, generate_display_board, Problem

show_board = generate_display_board()
secret_board = generate_secret_board()

for i in show_board:
    print(i,'\n')

user_choice = input('Enter coordenates: ')
problem = Problem(user_choice.upper(),show_board,secret_board)

print(problem.problem)

user_answer = int(input('Resultado >>> '))
problem.get_answer()

print(problem.check_answer(user_answer))

""" Tests
for i in show_board:
    print(i,'\n')

print('\n')

for i in secret_board:
    print(i,'\n')
"""





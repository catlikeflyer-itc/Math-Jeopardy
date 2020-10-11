from boards import generate_secret_board, generate_display_board, get_problem

show_board = generate_display_board()
secret_board = generate_secret_board()

### Tests
for i in show_board:
    print(i,'\n')

print('\n')

for i in secret_board:
    print(i,'\n')

user_choice = input('Enter coordenates: ')

print(get_problem(user_choice.upper(),show_board,secret_board))



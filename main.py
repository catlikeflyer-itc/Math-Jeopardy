from random import choice

board = []
choicestring = '012345678/*-+'
for x in range(0,5):
    #This will make the basic list that will eventually become the board
    board.append([choice(choicestring),choice(choicestring),choice(choicestring),choice(choicestring),choice(choicestring)])

for i in board:
    print(i)
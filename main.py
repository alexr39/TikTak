

def display_board(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('- - -')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('- - -')
    print(board[0] + '|' + board[1] + '|' + board[2])


def marker_writer(board, index, mark):
    board[int(index)] = mark
    return board


def choice_mark():
    while True:
        mark = input('Please peak a marker \'x\' or \'o\' ')
        if mark == 'x' or mark == 'o':
            return mark
            break
        else:
            print('You can choice only X or O')


def player1_turn(turns):
    while True:
        index = input('Player one, your turn. ')
        if index in turns:
            print('This cell already marked')
        else:
            return index
            break

def player2_turn(turns):
    while True:
        index = input('Player one, your turn. ')
        if index in turns:
            print('This cell already marked')
        else:

            return index
            break


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
mark1 = choice_mark()
if mark1 == 'x':
    mark2 = 'o'
else:
    mark2 = 'x'

print('Ok, let\'s play. Player 1 mark is {} and player 2 - {}'.format(mark1, mark2))

while True:
    turns = []
    index = player1_turn(turns)
    turns.append(index)
    board = marker_writer(board, index, mark1)
    display_board(board)
    index = player2_turn(turns)
    turns.append(index)
    board = marker_writer(board, index, mark2)
    display_board(board)




# def clear_board(board):
#     for elem in board:
#         elem = ' '
#     return board


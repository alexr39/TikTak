

def display_board(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('- - -')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('- - -')
    print(board[0] + '|' + board[1] + '|' + board[2])


def choice_mark():
    while True:
        mark = input('Please peak a marker \'x\' or \'o\' ')
        if mark == 'x' or mark == 'o':
            return mark
            break
        else:
            print('You can choice only X or O')


mark = choice_mark()
if mark == 'x':
    mark2 = 'o'
else:
    mark2 = 'x'
print('Ok, let\' play')

# def clear_board(board):
#     for elem in board:
#         elem = ' '
#     return board


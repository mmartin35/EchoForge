from home.games.shared import *

'''
returns:
    True: game ended
    False: game ongoing
'''


def game_sokoban(board: list[list[str]], direction: int):

    board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
             ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', '#', 'X', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', 'O', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    sokoban_act(board, direction)
    if sokoban_end(board):
        str_board_init(10, '#')
    return board

# Gameover condition
def sokoban_end(board: list[list[str]]):
    for row in board:
        for elem in row:
            if elem == 'O':
                return False
    return True

'''
directions:
    0 = right
    1 = down
    2 = left
    3 = up
code:
    # = wall
    P = player
    X = box
    O = slot
'''
# Process elements
def sokoban_act(board: list[list[str]], direction: int):
    if direction == 0:
        print('right')
    elif direction == 1:
        print('down')
    elif direction == 2:
        print('left')
    elif direction == 3:
        print('up')
    return board

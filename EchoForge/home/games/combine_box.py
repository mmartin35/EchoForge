import random
from home.games.shared import *
'''
returns:
    True: game ended
    False: game ongoing
'''
def game_combine_box(board: list[list[int]], direction: int, score: int):
    cb_act(board, direction, score)
    if cb_end(board):
        board = [[0] * 4 for _ in range (4)]
    return board

# Gameover condition
def cb_end(board: list[list[int]]):
    for y in range (4):
        for x in range (4):
            if board[y][x] == 0:
                return False
    return True

# Create a new cell
def cb_generate_cell(board: list[list[int]]):
    x, y = random.randint(0, 3), random.randint(0, 3)
    while board[y][x] != 0:
        x, y = random.randint(0, 3), random.randint(0, 3)
    board[y][x] = random.choices([2, 4], weights=[90, 10])[0]
    return board

'''
directions:
    0 = right
    1 = down
    2 = left
    3 = up
'''
# Process elements
def cb_act(board: list[list[int]], direction: int, score: int):
    if direction == 0:
        print('right')
        for y in range (4):
            row = board[y]
            for x in range (2, -1, -1):
                if row[x] == 0:
                    continue
                gap = x
                while gap < 3 and row[gap + 1] == 0:
                    row[gap + 1] = row[gap]
                    row[gap] = 0
                    gap += 1
                if gap < 3 and row[gap + 1] == row[gap] and row[gap] != 0:
                    row[gap + 1] *= 2
                    row[gap] = 0
    elif direction == 1:
        print('down')
        for x in range (4):
            column = [board[y][x] for y in range (4)]
            for y in range (2, -1, -1):
                if column[y] == 0:
                    continue
                gap = y
                while gap < 3 and column[gap + 1] == 0:
                    column[gap + 1] = column[gap]
                    column[gap] = 0
                    gap += 1
                if gap < 3 and column[gap + 1] == column[gap] and column[gap] != 0:
                    column[gap + 1] *= 2
                    column[gap] = 0
            for y in range(4):
                board[y][x] = column[y]
    elif direction == 2:
        print('left')
        for y in range (4):
            row = board[y]
            for x in range (1, 4):
                if row[x] == 0:
                    continue
                gap = x
                while gap > 0 and row[gap - 1] == 0:
                    row[gap - 1] = row[gap]
                    row[gap] = 0
                    gap -= 1
                if gap > 0 and row[gap - 1] == row[gap] and row[gap] != 0:
                    row[gap - 1] *= 2
                    row[gap] = 0
    elif direction == 3:
        print('up')
        for x in range (4):
            column = [board[y][x] for y in range (4)]
            for y in range (1, 4):
                if column[y] == 0:
                    continue
                gap = y
                while gap > 0 and column[gap - 1] == 0:
                    column[gap - 1] = column[gap]
                    column[gap] = 0
                    gap -= 1
                if gap > 0 and column[gap - 1] == column[gap] and column[gap] != 0:
                    column[gap - 1] *= 2
                    column[gap] = 0
            for y in range (4):
                board[y][x] = column[y]
    return cb_generate_cell(board)

'''
returns:
    True: game ended
    False: game ongoing
'''
def game_sokoban(board: list[list[int]], direction: int):
    if board[0][0] == 1:
        sokoban_reset()
    sokoban_act(board, direction)
    if sokoban_end(board):
        sokoban_reset()
    return board

# Reset the board
def sokoban_reset():
    board = [['#'] * 10 for _ in range(10)]
    return board

# Gameover condition
def sokoban_end(board: list[list[int]]):
    for y in range (4):
        for x in range (4):
            if board[y][x] == 0:
                return False
    return True

# Print the board
def sokoban_print(board: list[list[int]]):
    print("=====================")
    for row in board:
        print(row)
    print("=====================")

'''
directions:
    0 = right
    1 = down
    2 = left
    3 = up
'''
# Process elements
def sokoban_act(board: list[list[int]], direction: int):
    if direction == 0:
        print('right')
    elif direction == 1:
        print('down')
    elif direction == 2:
        print('left')
    elif direction == 3:
        print('up')
    return board

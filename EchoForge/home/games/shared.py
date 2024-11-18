def board_print(board: list[list[int]]):
    print("=====================")
    for row in board:
        print(row)
    print("=====================")

def int_board_init(size: int, nb: int):
    return [[nb] * size for _ in range (size)]

def str_board_init(size: int, char: str):
    return [[char] * size for _ in range (size)]

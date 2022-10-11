# sūji wa dokushin ni kagiru (SUDOKU)
from plate import Board


def main():
    board_new = Board.generate()
    print(board_new)


if __name__ == '__main__':
    main()
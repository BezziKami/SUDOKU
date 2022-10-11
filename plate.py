import numpy as np


class Board:
    def __init__(self):
        pass

    def generate(self):
        # test_board()
        board = self.test_board2()
        # test_protocole(board)

    # pierwsza metoda na tworzenie idealnego sudoku
    def test_board(self):
        board = np.zeros([9, 9])
        for i in range(9):
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    board[i, j] = 1
                if i % 3 == 0 and (j + 2) % 3 == 0:
                    board[i, j] = 2
                if i % 3 == 0 and (j + 1) % 3 == 0:
                    board[i, j] = 3
                if (i + 2) % 3 == 0 and j % 3 == 0:
                    board[i, j] = 4
                if (i + 2) % 3 == 0 and (j + 2) % 3 == 0:
                    board[i, j] = 5
                if (i + 2) % 3 == 0 and (j + 1) % 3 == 0:
                    board[i, j] = 6
                if (i + 1) % 3 == 0 and j % 3 == 0:
                    board[i, j] = 7
                if (i + 1) % 3 == 0 and (j + 2) % 3 == 0:
                    board[i, j] = 8
                if (i + 1) % 3 == 0 and (j + 1) % 3 == 0:
                    board[i, j] = 9
        print(board)
        return board

    # druga metoda na tworzenie idealnego sudoku
    def test_board2(self):
        board = np.zeros([9, 9])
        for i in range(0, 3):
            for j in range(0, 9):
                redo = (j + (i * 3)) % 9
                board[i, j] = redo
                if redo == 0:
                    board[i, j] = 9
        for i in range(3, 6):
            for j in range(0, 9):
                redo = (j + 1 + (i * 3)) % 9
                board[i, j] = redo
                if redo == 0:
                    board[i, j] = 9
        for i in range(6, 9):
            for j in range(0, 9):
                redo = (j + 2 + (i * 3)) % 9
                board[i, j] = redo
                if redo == 0:
                    board[i, j] = 9

        print(board)
        return board

    def test_protocole(self, board):
        pass
        # kwadraty

        # rzędy
        if board.sum():
            print('Cała suma się zgadza')
            if board.sum(axis=1):
                print('gay')

        # kolumny


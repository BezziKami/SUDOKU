import numpy as np
from random import randint, shuffle, sample


# testowa tablica, która generuje zawsze tablice o liczbach na tych samych miejscach
def test_board2():
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


# Generator planszy bez żadnych ograniczników (mogą pojawiać się powtórki)
def board_generator():
    board = []
    seed = list(range(1, 10))
    for i in range(9):
        ret = sample(seed, len(seed))
        board.append(ret)
        # print(board)
    return np.array(board)


# Sprawdza zgodność tablicy (czy nie powtarzają się jakieś liczby) i zwraca bool
def compatibility(board):
    dump = []
    # for line in range(9):
    #     for column in range(9):
    #         if board[line, column] in dump:
    #             print("Repeat error: 001")
    #             return False
    #         dump.append(board[line, column])
    #         # print('Error not found')
    #     # print(f"line {line} end")
    #     dump.clear()
    # dump.clear()
    for column in range(9):
        for line in range(9):
            if board[line, column] in dump:
                print("Repeat error: 002")
                return False
            dump.append(board[line, column])
            # print('Error not found')
        # print(f"column {column} end")
        dump.clear()
    dump.clear()
    print("Compatibility test complete!")
    return True


# Sprawdza zgodność niepełnej tablicy
def compatibility2(board_prime):
    board = np.array(board_prime)
    dump = []
    lines = len(board_prime)
    print(lines)
    for column in range(9):
        for line in range(lines):
            if board[line, column] in dump:
                # print("Repeat error: 002")
                return False
            dump.append(board[line, column])
            # print('Error not found')
        # print(f"column {column} end")
        dump.clear()
    dump.clear()
    if lines < 4:
        for i in range(3):
            for column in range(i*3, 3+i*3):
                for line in range(0, lines):
                    if board[line, column] in dump:
                        # print("Repeat error: 002")
                        return False
                    dump.append(board[line, column])
            print(dump)
            dump.clear()
    dump.clear()
    if 3 < lines < 7:
        for i in range(3):
            for column in range(i*3, 3+i*3):
                for line in range(3, lines):
                    if board[line, column] in dump:
                        # print("Repeat error: 002")
                        return False
                    dump.append(board[line, column])
            print(dump)
            dump.clear()
    dump.clear()
    if lines > 6:
        for i in range(3):
            for column in range(i*3, 3+i*3):
                for line in range(3, lines):
                    if board[line, column] in dump:
                        # print("Repeat error: 002")
                        return False
                    dump.append(board[line, column])
            print(dump)
            dump.clear()
    dump.clear()
    print("Compatibility test complete!")
    return True


# Generuje po kolei tablice i sprawdza od razu ich zgodność
def ultimate_board_generator():
    board = []
    seed = list(range(1, 10))
    czas = []

    for i in range(9):
        print("Wiersz:", i)
        timer = 1

        while True:
            # print("Próba numer: ", timer)
            ret = sample(seed, len(seed))
            board.append(ret)

            if compatibility2(board) or timer > 300000:
                czas.append(timer)
                timer = 1
                break

            board.pop(-1)
            timer += 1

    print(czas)
    return np.array(board)


# Generuje całą tablice i sprawdza jej zgodność (mało wydajne)
def true_board():
    print("Begin searching")
    timer = 1
    while True:
        print(f"Próba numer {timer}")
        board = board_generator()
        if compatibility(board) or timer > 100:
            break
        timer += 1
    return board


def main():
    boards = ultimate_board_generator()
    print(boards)
    compatibility(boards)

    # sample = list(range(1, 10))
    # print(sample)
    # print(shuffle(sample))
    # print(sample)
    # print(shuffle(sample))
    # print(sample)
    # print(shuffle(sample))
    # print(sample)

    # b = test_board2()
    # bo = board_generator()
    # print(bo)
    #
    # print(compatibility(b))
    # print(compatibility(bo))

if __name__=="__main__":
    main()



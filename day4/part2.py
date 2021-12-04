#!/usr/bin/env python3

import fileinput


class BoardSquare:
    def __init__(self, number):
        self.checked = False
        self.value = int(number)

    def __repr__(self):
        return f"{self.value}:{self.checked}"


def check_board(number, board):
    for line in board:
        for square in filter(lambda sq: sq.value == number, line):
            square.checked = True
    return board


def is_board_winning(board):
    rows = [line for line in board]
    cols = [[line[i] for line in board] for i in range(5)]

    for row in rows:
        if all([sq.checked for sq in row]):
            return True
    for col in cols:
        if all([sq.checked for sq in col]):
            return True
    return False


def evaluate_board_value(board):
    squares = [square for line in board for square in line]
    unchecked_squares = filter(lambda sq: not sq.checked, squares)
    return sum(map(lambda sq: sq.value, unchecked_squares))


def main():
    lines = [line.strip() for line in fileinput.input()]
    number_order = map(int, lines[0].split(","))
    board_lines = [
        [BoardSquare(number) for number in line.split()]
        for line in lines[2:]
        if line.strip()
    ]
    boards = [board_lines[i : i + 5] for i in range(0, len(board_lines), 5)]

    last_winning_board = []
    for number in number_order:
        boards = [check_board(number, board) for board in boards]
        losing_boards = list(filter(lambda board: not is_board_winning(board), boards))
        if not losing_boards:
            print(evaluate_board_value(last_winning_board) * number)
            return
        last_winning_board = losing_boards[0]


if __name__ == "__main__":
    main()

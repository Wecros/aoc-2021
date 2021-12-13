#!/usr/bin/env python3

import fileinput
from pprint import pprint


def main():
    dots, fold_instructions, width, height = get_input()
    for axis, value in fold_instructions:
        if axis == "x":
            dots = fold_along_x(dots, value, width)
        else:
            dots = fold_along_y(dots, value, height)
        break
    print(len(dots))


def get_input():
    dots = set()
    fold_instructions = []
    width = 0
    height = 0
    for line in fileinput.input():
        if line[0] == "f":
            _, _, instr = line.strip().split()
            axis, value = instr.split("=")
            fold_instructions.append((axis, int(value)))
        elif line.strip():
            x, y = map(int, line.strip().split(","))
            if width < x:
                width = x
            elif height < y:
                height = y
            dots.add((x, y))
    return (dots, fold_instructions, width + 1, height + 1)


def fold_along_x(dots, fold_value, width):
    updated_dots = set()
    for x in range(width):
        if x > fold_value:
            affected_dots = set(filter(lambda coord: coord[0] == x, dots))
            new_dots = set(
                map(
                    lambda coord: (fold_value - (x - fold_value), coord[1]),
                    affected_dots,
                )
            )
            updated_dots |= new_dots
            dots = dots - affected_dots
    return dots | updated_dots


def fold_along_y(dots, fold_value, height):
    updated_dots = set()
    for y in range(height):
        if y > fold_value:
            affected_dots = set(filter(lambda coord: coord[1] == y, dots))
            new_dots = set(
                map(
                    lambda coord: (coord[0], fold_value - (y - fold_value)),
                    affected_dots,
                )
            )
            updated_dots |= new_dots
            dots = dots - affected_dots
    return dots | updated_dots


def visualize_dots(dots, width, height):
    for y in range(height):
        for x in range(width):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    main()

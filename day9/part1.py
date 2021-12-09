#!/usr/bin/env python3

import fileinput
import pprint


def main():
    height_lines = get_input()
    risk = 0
    for y, line in enumerate(height_lines):
        for x, height in enumerate(line):
            adjcent_heights = get_adjacent_heights(height_lines, y, x)
            if all(height < adj for adj in adjcent_heights):
                risk += 1 + height
    print(risk)


def get_input():
    return [list(map(int, line.strip())) for line in fileinput.input()]


def get_adjacent_heights(height_lines, y, x):
    max_y = len(height_lines)
    max_x = len(height_lines[0])
    top = height_lines[y - 1][x] if y - 1 >= 0 else None
    bot = height_lines[y + 1][x] if y + 1 < max_y else None
    left = height_lines[y][x - 1] if x - 1 >= 0 else None
    right = height_lines[y][x + 1] if x + 1 < max_x else None
    return [adj for adj in (top, bot, left, right) if adj is not None]


if __name__ == "__main__":
    main()

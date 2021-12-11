#!/usr/bin/env python3

import fileinput
from pprint import pprint

MAX_ENERGY = 9
GRID_SIZE = 10


def main():
    grid = get_input()
    global GRID_SIZE
    GRID_SIZE = len(grid)

    step = 0
    while True:
        grid, count = process_cycle(grid)
        step += 1
        if count == GRID_SIZE * GRID_SIZE:
            break
    print(step)


def process_cycle(grid):
    flashed_octopuses = set()
    # 1. add 1 to every octopus
    grid = [list(map(lambda x: x + 1, line)) for line in grid]
    # 2. keep flashing octopuses
    flashed = True
    while flashed:
        flashed = process_grid(grid, flashed_octopuses)
    # 3. reset octopuses that flashed
    grid = reset_flashed_octopuses(grid, flashed_octopuses)
    return grid, len(flashed_octopuses)


def process_grid(grid, flashed_octopuses):
    flashed_octopuses_before = flashed_octopuses.copy()
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] > MAX_ENERGY and (x, y) not in flashed_octopuses:
                flash(grid, x, y)
                flashed_octopuses.add((x, y))
    return flashed_octopuses_before != flashed_octopuses


def flash(grid, x, y):
    for y2, x2 in (
        (y + 1, x - 1),
        (y + 1, x),
        (y + 1, x + 1),
        (y, x - 1),
        (y, x + 1),
        (y - 1, x - 1),
        (y - 1, x),
        (y - 1, x + 1),
    ):
        if 0 <= x2 < GRID_SIZE and 0 <= y2 < GRID_SIZE:
            grid[y2][x2] += 1


def reset_flashed_octopuses(grid, flashed_octopuses):
    for (x, y) in flashed_octopuses:
        grid[y][x] = 0
    return grid


def get_input():
    return [list(map(int, line.strip())) for line in fileinput.input()]


if __name__ == "__main__":
    main()

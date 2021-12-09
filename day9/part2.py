#!/usr/bin/env python3

import collections
import fileinput
from pprint import pprint
from functools import reduce


def main():
    height_lines = get_input()

    basins = set()
    for y, line in enumerate(height_lines):
        for x, height in enumerate(line):
            if height == 9:
                continue
            basin = frozenset(get_basin(height_lines, (x, y)))
            basins.add(basin)

    three_largest_basins = sorted(basins, key=len, reverse=True)[:3]
    total_size = reduce(
        lambda a, b: a * b, ([len(basin) for basin in three_largest_basins])
    )
    print(total_size)


def get_input():
    return [list(map(int, line.strip())) for line in fileinput.input()]


def get_basin(grid, start):
    """Modification of BFS where we do not need path, only the seen set."""
    height = len(grid)
    width = len(grid[0])

    wall = 9
    queue = collections.deque([start])
    seen = set([start])
    while queue:
        x, y = queue.popleft()
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= x2 < width
                and 0 <= y2 < height
                and grid[y2][x2] != wall
                and (x2, y2) not in seen
            ):
                queue.append([x2, y2])
                seen.add((x2, y2))
    return seen


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import fileinput
import math
from copy import deepcopy
from pprint import pprint

HEIGHT = 0
WIDTH = 0
DIMENSION_MUL = 5


def main():
    global HEIGHT, WIDTH
    grid = get_input()

    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    # Add blocks to the right
    new_grid = deepcopy(grid)
    for i in range(DIMENSION_MUL - 1):
        for y in range(HEIGHT):
            new_grid[y].extend(list(map(lambda x: ((x + i) % 9) + 1, grid[y])))
    # Add blocks below
    grid = new_grid
    new_grid = deepcopy(grid)
    for i in range(DIMENSION_MUL - 1):
        for y in range(HEIGHT):
            new_grid.append(list(map(lambda x: ((x + i) % 9) + 1, grid[y])))
    # visualize_grid(new_grid, WIDTH, HEIGHT)

    grid = new_grid
    HEIGHT = len(grid)
    WIDTH = len(grid[0])
    start = (0, 0)
    end = (WIDTH - 1, HEIGHT - 1)

    visited = dijkstra(grid, start, end)
    pprint(visited[HEIGHT - 1, WIDTH - 1])


def get_input():
    return [list(map(int, line.strip())) for line in fileinput.input()]


def dijkstra(grid, start, end):
    """Dijsktra algorithm to find the shortest path.

    Returns map with visited nodes as keys and the shortest path possible to them.

    TODO: Rewritten to A* for heurestic optimization, where the heurestic function
    is the Manhattan distance between the current node and end node.
    """
    unvisited = {(x, y): math.inf for x in range(WIDTH) for y in range(HEIGHT)}
    visited = {}

    current = start
    current_risk = 0
    while True:
        x, y = current
        h = abs(x - end[0]) + abs(y - end[1])

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in unvisited or not (0 <= x2 < WIDTH and 0 <= y2 < HEIGHT):
                continue
            risk = grid[y2][x2]
            new_risk = current_risk + risk
            if unvisited[(x2, y2)] > new_risk:
                unvisited[(x2, y2)] = new_risk

        visited[current] = current_risk
        del unvisited[current]
        if current == end:
            break
        candidates = dict(filter(lambda item: item[1] < math.inf, unvisited.items()))
        current = min(candidates, key=candidates.get)
        current_risk = unvisited[current]

    return visited


def visualize_grid(grid, width_sep, height_sep):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
            if ((x + 1) % width_sep) == 0:
                print(" ", end="")
        print()
        if ((y + 1) % height_sep) == 0:
            print()


if __name__ == "__main__":
    main()

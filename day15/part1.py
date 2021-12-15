#!/usr/bin/env python3

import fileinput
import math
from pprint import pprint

HEIGHT = 0
WIDTH = 0


def main():
    grid = get_input()

    global HEIGHT, WIDTH
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    visited = dijkstra(grid, (0, 0), (WIDTH - 1, HEIGHT - 1))
    pprint(visited[HEIGHT - 1, WIDTH - 1])


def get_input():
    return [list(map(int, line.strip())) for line in fileinput.input()]


def dijkstra(grid, start, end):
    """Dijsktra algorithm to find the shortest path.

    Returns map with visited nodes as keys and the shortest path possible to them.
    """
    unvisited = {(x, y): math.inf for x in range(WIDTH) for y in range(HEIGHT)}
    visited = {}

    current = start
    current_risk = 0
    while True:
        x, y = current
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in unvisited or not (0 <= x2 < WIDTH and 0 <= y2 < HEIGHT):
                continue
            risk = grid[y2][x2]
            new_risk = current_risk + risk
            if unvisited[(x2, y2)] > new_risk:
                unvisited[(x2, y2)] = new_risk

        visited[current] = current_risk
        del unvisited[current]
        if current == end or not unvisited:
            break
        candidates = dict(filter(lambda item: item[1] < math.inf, unvisited.items()))
        current = min(candidates, key=candidates.get)
        current_risk = unvisited[current]

    return visited


if __name__ == "__main__":
    main()

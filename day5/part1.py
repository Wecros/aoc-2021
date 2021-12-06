#!/usr/bin/env python3

import fileinput


def parse_input():
    coords = []
    for line in fileinput.input():
        left_coord, _, right_coord = line.split()
        x1, y1 = left_coord.split(",")
        x2, y2 = right_coord.split(",")
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        coordinate = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        coords.append(coordinate)
    return coords


def increment_position(coord, position_map):
    position_map.setdefault(coord, 0)
    position_map[coord] += 1


def get_result(position_map):
    return len({k: v for k, v in position_map.items() if v > 1})


def main():
    coords = parse_input()
    position_map = {}
    for coord in coords:
        x1, y1, x2, y2 = (coord["x1"], coord["y1"], coord["x2"], coord["y2"])
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                increment_position((x1, y), position_map)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                increment_position((x, y1), position_map)

    print(get_result(position_map))


if __name__ == "__main__":
    main()

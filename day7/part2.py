#!/usr/bin/env python3

import fileinput
import sys


def main():
    positions = list(get_input())
    min_pos = min(positions)
    max_pos = max(positions)

    fuel_positions = {}
    for pos in range(min_pos, max_pos + 1):
        fuel_positions[pos] = calculate_position(positions, pos)
    print(int(min(fuel_positions.values())))


def calculate_position(positions, target_pos):
    def gauss_formula(pos, target_pos):
        n = abs(pos - target_pos)
        return n / 2 * (1 + n)
    fuel_positions = [gauss_formula(pos, target_pos) for pos in positions]
    return sum(fuel_positions)


def get_input():
    return map(int, next(fileinput.input()).strip().split(","))


if __name__ == "__main__":
    main()

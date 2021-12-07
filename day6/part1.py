#!/usr/bin/env python3

import fileinput

DAYS_COUNT = 80
RESET_FISH = 6
NEW_FISH = 8


def get_input():
    numbers = next(fileinput.input()).strip().split(",")
    fishes = list(map(int, numbers))
    return fishes


def main():
    fishes = get_input()
    for _ in range(DAYS_COUNT):
        new_fishes = []
        for fish in fishes:
            if fish == 0:
                new_fishes.append(RESET_FISH)
                new_fishes.append(NEW_FISH)
            else:
                new_fishes.append(fish - 1)
        fishes = new_fishes
    print(len(fishes))


if __name__ == "__main__":
    main()

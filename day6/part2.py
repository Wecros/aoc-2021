#!/usr/bin/env python3

import fileinput
import sys

DAYS_COUNT = 256
OLD_FISH = 6
NEW_FISH = 8


def main():
    if len(sys.argv) > 1:
        global DAYS_COUNT
        DAYS_COUNT = int(sys.argv[1])
    fishes = get_input()

    day_keys = {k: 0 for k in range(DAYS_COUNT + 1)}
    day_keys = start_spawning(DAYS_COUNT, day_keys)
    cumulative_day_keys = make_day_keys_cumulative(day_keys)
    cumulative_day_keys |= {k: 0 for k in range(-4, 0)}

    count = 0
    for fish in fishes:
        count += cumulative_day_keys[DAYS_COUNT - fish + 1]
    print(count)


def get_input():
    numbers = sys.stdin.read().strip().split(",")
    fishes = list(map(int, numbers))
    return fishes


def start_spawning(days, day_keys):
    """Calculate every day key for "1" fish number. Other fishes are then get by offsetting
    day keys dictionary."""
    day_keys[0] = 1
    days_fish_count = {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for day in range(1, days + 1):
        day_keys[day] = days_fish_count[0]
        days_fish_count[OLD_FISH + 1] += days_fish_count[0]
        days_fish_count[NEW_FISH + 1] += days_fish_count[0]
        for i in range(NEW_FISH + 1):
            days_fish_count[i] = days_fish_count[i + 1]
            days_fish_count[i + 1] = 0
    return day_keys


def make_day_keys_cumulative(day_keys):
    last_val = 0
    day_keys = {k: v for k, v in sorted(day_keys.items(), key=lambda item: item[0])}
    for k, v in day_keys.items():
        day_keys[k] = v + last_val
        last_val = day_keys[k]
    return day_keys


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import fileinput
import statistics
from pprint import pprint

char_to_score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

open_to_closing_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def main():
    lines = get_input()
    scores = []
    for line in lines:
        score = 0
        corrupted = False
        expected_closing = []
        for char in line:
            if char in open_to_closing_map.keys():
                expected_closing.append(char)
            elif char in open_to_closing_map.values():
                expected = expected_closing.pop()
                if char != open_to_closing_map[expected]:
                    corrupted = True
                    break

        while expected_closing and not corrupted:
            char = expected_closing.pop()
            score *= 5
            score += char_to_score_map[open_to_closing_map[char]]
        if score:
            scores.append(score)

    print(statistics.median(sorted(scores)))


def get_input():
    return map(lambda line: line.strip(), fileinput.input())


if __name__ == "__main__":
    main()

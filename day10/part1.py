#!/usr/bin/env python3

import fileinput
from pprint import pprint

char_to_score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

open_to_closing_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def main():
    lines = get_input()

    corrupted_chars = []
    for line in lines:
        expected_closing = []
        for char in line:
            if char in open_to_closing_map.keys():
                expected_closing.append(char)
            elif char in open_to_closing_map.values():
                expected = expected_closing.pop()
                if char != open_to_closing_map[expected]:
                    corrupted_chars.append(char)
                    break
            else:
                print(f"Syntax error, line: {line}")
                break

    score = sum(map(lambda char: char_to_score_map[char], corrupted_chars))
    print(score)


def get_input():
    return map(lambda line: line.strip(), fileinput.input())


if __name__ == "__main__":
    main()

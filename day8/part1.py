#!/usr/bin/env python3

import fileinput


def main():
    entries = get_input()
    output_digits = {k: 0 for k in range(10)}
    for entry in entries:
        for digit in entry["output"]:
            if len(digit) == 2:
                output_digits[2] += 1
            if len(digit) == 3:
                output_digits[7] += 1
            if len(digit) == 4:
                output_digits[4] += 1
            if len(digit) == 7:
                output_digits[3] += 1
    print(output_digits[2] + output_digits[3] + output_digits[4] + output_digits[7])


def get_input():
    entries = []
    for line in fileinput.input():
        entry = {}
        line_left, line_right = line.strip().split("|")
        entry["patterns"] = line_left.strip().split(" ")
        entry["output"] = line_right.strip().split(" ")
        entries.append(entry)
    return entries


if __name__ == "__main__":
    main()

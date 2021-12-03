#!/usr/bin/env python3

import fileinput


def get_new_list(binary_list, bit, index):
    return [binary for binary in binary_list if binary[index] == bit]


def find_rating(lines, dominant_bit, other_bit):
    index = 0
    binary_list = lines
    while index != (len(binary_list[0])) and len(binary_list) != 1:
        bit_list = [binary[index] for binary in binary_list]
        if bit_list.count("0") > bit_list.count("1"):
            binary_list = get_new_list(binary_list, dominant_bit, index)
        else:
            binary_list = get_new_list(binary_list, other_bit, index)
        index += 1
    return binary_list[0]


def main():
    lines = [line.strip() for line in fileinput.input()]
    oxygen_rating = find_rating(lines, "0", "1")
    co2_rating = find_rating(lines, "1", "0")

    print(int(oxygen_rating, 2) * int(co2_rating, 2))


if __name__ == "__main__":
    main()

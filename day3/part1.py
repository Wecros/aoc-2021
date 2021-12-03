#!/usr/bin/env python3

import fileinput


def main():
    lines = [line.strip() for line in fileinput.input()]
    binary_length = len(lines[0])
    gamma_rate = ""
    epsilon_rate = ""

    binary_lists = [[line[i] for line in lines] for i in range(binary_length)]
    for binary_list in binary_lists:
        if binary_list.count("0") > binary_list.count("1"):
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == "__main__":
    main()

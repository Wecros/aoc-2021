#!/usr/bin/env python3

import fileinput
from typing import List

def get_input() -> List[int]:
    return [int(line.strip()) for line in fileinput.input()]

def main():
    previous_sum = None
    increased_count = 0
    numbers_list = get_input()
    for i in range(len(numbers_list)):
        sum_list = numbers_list[i:i+3]
        if (len(sum_list) != 3):
            break

        number_sum = sum(sum_list)
        if previous_sum and number_sum > previous_sum:
            increased_count += 1
        previous_sum = number_sum

    print(increased_count)


if __name__ == '__main__':
    main()

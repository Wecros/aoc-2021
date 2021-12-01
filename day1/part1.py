#!/usr/bin/env python3

import fileinput


def main():
    previous_number = None
    increased_count = 0
    for number in fileinput.input():
        if previous_number and int(number) > previous_number:
            increased_count += 1
        previous_number = int(number)

    print(increased_count)


if __name__ == '__main__':
    main()

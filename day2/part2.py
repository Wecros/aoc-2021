#!/usr/bin/env python3

import fileinput


def main():
    lines = [line.strip() for line in fileinput.input()]
    depth = 0
    position = 0
    aim = 0
    for line in lines:
        command, value = line.split()
        value = int(value)
        match command:
            case 'forward':
                position += value
                depth += aim * value
            case 'down':
                aim += value
            case 'up':
                aim -= value

    print(position * depth)


if __name__ == "__main__":
    main()

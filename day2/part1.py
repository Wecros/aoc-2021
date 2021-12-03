#!/usr/bin/env python3

import fileinput


def main():
    lines = [line.strip() for line in fileinput.input()]
    instructions = {"forward": 0, "down": 0, "up": 0}
    for line in lines:
        command, value = line.split()
        instructions[command] += int(value)

    print(instructions["forward"] * (instructions["down"] - instructions["up"]))


if __name__ == "__main__":
    main()

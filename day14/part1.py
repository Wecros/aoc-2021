#!/usr/bin/env python3

import fileinput
from collections import Counter
from pprint import pprint

STEPS = 10


def main():
    template, rules = get_input()

    polymer = template
    for step in range(STEPS):
        new_polymer = polymer.copy()
        for i in range(len(polymer) - 1):
            rule = polymer[i] + polymer[i + 1]
            if rule in rules:
                new_polymer.insert(i + 1 + len(new_polymer) - len(polymer), rules[rule])
        polymer = new_polymer

    data = Counter(polymer)
    most_common_length = data.most_common(1)[0][1]
    least_common_length = data.most_common()[-1][1]
    print(most_common_length - least_common_length)


def get_input():
    template = []
    rules = {}
    for line in fileinput.input():
        if not line.strip():
            continue
        elif fileinput.isfirstline():
            template = list(line.strip())
        else:
            line = line.strip()
            left, right = line.split(" -> ")
            # rules.append((left, right))
            rules[left] = right
    return template, rules


if __name__ == "__main__":
    main()

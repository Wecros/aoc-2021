#!/usr/bin/env python3

import fileinput
from pprint import pprint

STEPS = 40


def main():
    template, rules = get_input()
    global_pairs_count_map = {k: 0 for k in rules.keys()}
    rule_to_output = {k: (k[0] + v, v + k[1]) for k, v in rules.items()}
    letters = set([rule[0] for rule in rules.keys()])
    counter = {k: 0 for k in letters}

    pairs = [template[i] + template[i + 1] for i in range(len(template) - 1)]
    for pair in pairs:
        pairs_count_map = calculate_final_pairs(pair, rule_to_output)
        for k, v in pairs_count_map.items():
            global_pairs_count_map[k] += v

    for k, v in global_pairs_count_map.items():
        counter[k[0]] += v
    counter = {k: v for k, v in counter.items() if v != 0}
    result = max(counter.values()) - min(counter.values())
    print(result)


def calculate_final_pairs(pair, rule_to_output):
    counter = {k: 0 for k in rule_to_output.keys()}
    counter[pair] += 1
    for step in range(STEPS):
        new_counter = {k: 0 for k in rule_to_output.keys()}
        for pair, value in counter.items():
            new_rule1, new_rule2 = rule_to_output[pair]
            new_counter[new_rule1] += value
            new_counter[new_rule2] += value
        counter = new_counter
    return counter


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


def get_result(polymer):
    data = Counter(polymer)
    most_common_length = data.most_common(1)[0][1]
    least_common_length = data.most_common()[-1][1]
    return most_common_length - least_common_length


if __name__ == "__main__":
    main()

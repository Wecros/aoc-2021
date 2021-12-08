#!/usr/bin/env python3

"""Number reference:
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""

import fileinput
import pprint


def main():
    entries = get_input()
    count = 0
    for entry in entries:
        pattern_to_original_map = get_pattern_to_original_map(entry)
        displayed_numbers = [
            get_digit_from_mapping(letters, pattern_to_original_map)
            for letters in entry["output"]
        ]
        count += int("".join(map(str, displayed_numbers)))

    print(count)


def get_input():
    entries = []
    for line in fileinput.input():
        entry = {}
        line_left, line_right = line.strip().split("|")
        entry["patterns"] = line_left.strip().split(" ")
        entry["output"] = line_right.strip().split(" ")
        entries.append(entry)
    return entries


def get_pattern_to_original_map(entry):
    patterns = []
    unique_patterns = {}
    unique_segment_len_to_digit_map = {2: 1, 4: 4, 3: 7, 7: 8}

    for letters in entry["patterns"]:
        pattern = create_number(letters)
        patterns.append(pattern)
        active_segments = get_active_segments(pattern)
        if len(active_segments) in unique_segment_len_to_digit_map.keys():
            unique_patterns[
                unique_segment_len_to_digit_map[len(active_segments)]
            ] = pattern

    # comparing unique patterns with each other can get as some correct segments
    [a] = get_nonoverlap(unique_patterns[1], unique_patterns[7])
    possible_c_f = get_overlap(unique_patterns[1], unique_patterns[4])
    [c, f] = possible_c_f

    # get number 4 segments
    possible_b_d = set(get_nonoverlap(unique_patterns[1], unique_patterns[4]))

    # get number 0 by comparing 4 segments with 0, 6, 9 -> only 1 segment is shared with 0
    patterns_0_6_9 = [
        pattern for pattern in patterns if len(get_active_segments(pattern)) == 6
    ]
    for pattern in patterns_0_6_9:
        if not possible_b_d <= get_active_segments(pattern):
            unique_patterns[0] = pattern

    # By comparing 0 segments with 4 segments we can get correct value of "d" segment
    [d] = possible_b_d - get_overlap(unique_patterns[0], unique_patterns[4])
    # The other must logically be b
    [b] = possible_b_d - {d}

    # The only remaining segments to be mapped is e and g
    possible_e_g = patterns[0].keys() - {a, b, c, d, f}

    # We can determine g from digit 9, so first we need to determine digit 9.
    # Possible options with 6 segments are 0,6,9; we already determined 0.
    # To determine 9, we can check if segment c is in digits [6,9]
    patterns_6_9 = [
        pattern for pattern in patterns_0_6_9 if pattern != unique_patterns[0]
    ]
    pattern_9 = [
        pattern for pattern in patterns_6_9 if c in get_active_segments(pattern)
    ]
    # Determine [c,f] ambiguity
    if len(pattern_9) > 1:
        pattern_9 = [
            pattern for pattern in patterns_6_9 if f in get_active_segments(pattern)
        ]
        [f, c] = [c, f]

    [unique_patterns[9]] = pattern_9

    # Now we determine g from digit 9 by comparing it to already known segments
    [g] = get_active_segments(unique_patterns[9]) - {a, b, c, d, f}
    [e] = possible_e_g - set(g)

    return {a: "a", b: "b", c: "c", d: "d", e: "e", f: "f", g: "g"}


def get_digit_from_mapping(letters, pattern_to_original_map):
    mixed_digit = frozenset(letters)
    original_digit = frozenset(
        [pattern_to_original_map[letter] for letter in mixed_digit]
    )
    segments_to_digits_map = {
        frozenset("abcefg"): 0,
        frozenset("cf"): 1,
        frozenset("acdeg"): 2,
        frozenset("acdfg"): 3,
        frozenset("bcdf"): 4,
        frozenset("abdfg"): 5,
        frozenset("abdfeg"): 6,
        frozenset("acf"): 7,
        frozenset("abcdefg"): 8,
        frozenset("abcdfg"): 9,
    }
    return segments_to_digits_map.get(original_digit)


def create_number(letters):
    number = get_default_number_dict()
    for letter in letters:
        number[letter] = 1
    return number


def get_default_number_dict():
    return {chr(k): 0 for k in range(ord("a"), ord("g") + 1)}


def get_overlap(number1, number2):
    active_segments_1 = get_active_segments(number1)
    active_segments_2 = get_active_segments(number2)
    overlap = set()
    for letter in active_segments_1:
        if letter in active_segments_2:
            overlap.add(letter)
    return overlap


def get_nonoverlap(number1, number2):
    active_segments_1 = get_active_segments(number1)
    active_segments_2 = get_active_segments(number2)
    overlap = set()
    for letter in active_segments_1:
        if letter not in active_segments_2:
            overlap.add(letter)
    for letter in active_segments_2:
        if letter not in active_segments_1:
            overlap.add(letter)
    return overlap


def get_active_segments(number):
    return set([k for k, v in number.items() if v])


if __name__ == "__main__":
    main()

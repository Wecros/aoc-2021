#!/usr/bin/env python3

# Inspired by: https://www.python.org/doc/essays/graphs/

import fileinput
from pprint import pprint
from collections import deque


def main():
    paths = get_input()
    graph = create_graph_from_paths(paths)
    paths = find_all_paths(graph, "start", "end")
    print(len(paths))


def get_input():
    return [tuple(line.strip().split("-")) for line in fileinput.input()]


def create_graph_from_paths(paths):
    graph = {}
    for path in paths:
        graph.setdefault(path[0], []).append(path[1])
        graph.setdefault(path[1], []).append(path[0])
    return graph


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if can_visit_node(node, path):
            newpaths = find_all_paths(graph, node, end, path)
            paths.extend(newpaths)
    return paths


def can_visit_node(node, path):
    visited_small_caves = list(
        filter(lambda x: x.islower() and x not in {"start", "end"}, path)
    )
    did_visit_small_caves_twice = len(visited_small_caves) == len(
        set(visited_small_caves)
    ) and node not in {"start", "end"}
    return node not in path or node.isupper() or did_visit_small_caves_twice


if __name__ == "__main__":
    main()

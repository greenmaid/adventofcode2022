#!/usr/bin/env python3

import os
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_tree_map_from_input(path: str) -> List[List[int]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([int(s) for s in line])
    return map


def is_tree_visible_from_top(tree_map: List[List[int]], x: int, y: int) -> bool:
    height = tree_map[y][x]
    for i in range(y):
        if tree_map[i][x] >= height:
            return False
    return True


def compute_top_scenic_score(tree_map: List[List[int]], x: int, y: int) -> int:
    score = 0
    height = tree_map[y][x]
    for i in range(1, y + 1):
        score += 1
        if tree_map[y - i][x] >= height:
            return score
    return score


def is_tree_visible_from_bottom(tree_map: List[List[int]], x: int, y: int) -> bool:
    height = tree_map[y][x]
    max_y = len(tree_map) - 1
    for i in range(max_y - y):
        if tree_map[max_y - i][x] >= height:
            return False
    return True


def compute_bottom_scenic_score(tree_map: List[List[int]], x: int, y: int) -> int:
    score = 0
    height = tree_map[y][x]
    max_y = len(tree_map)
    for i in range(1, max_y - y):
        score += 1
        if tree_map[y + i][x] >= height:
            return score
    return score


def is_tree_visible_from_left(tree_map: List[List[int]], x: int, y: int) -> bool:
    height = tree_map[y][x]
    for i in range(x):
        if tree_map[y][i] >= height:
            return False
    return True


def compute_left_scenic_score(tree_map: List[List[int]], x: int, y: int) -> int:
    score = 0
    height = tree_map[y][x]
    for i in range(1, x + 1):
        score += 1
        if tree_map[y][x - i] >= height:
            return score
    return score


def is_tree_visible_from_right(tree_map: List[List[int]], x: int, y: int) -> bool:
    height = tree_map[y][x]
    max_x = len(tree_map[y]) - 1
    for i in range(max_x - x):
        if tree_map[y][max_x - i] >= height:
            return False
    return True


def compute_right_scenic_score(tree_map: List[List[int]], x: int, y: int) -> int:
    score = 0
    height = tree_map[y][x]
    max_x = len(tree_map[y])
    for i in range(1, max_x - x):
        score += 1
        if tree_map[y][x + i] >= height:
            return score
    return score


def is_tree_visible(tree_map: List[List[int]], x: int, y: int) -> bool:
    if (
        is_tree_visible_from_top(tree_map, x, y)
        or is_tree_visible_from_bottom(tree_map, x, y)
        or is_tree_visible_from_left(tree_map, x, y)
        or is_tree_visible_from_right(tree_map, x, y)
    ):
        return True
    return False


def count_visible_trees(tree_map: List[List[int]]) -> int:
    count = 0
    for y in range(len(tree_map)):
        for x in range(len(tree_map[y])):
            if is_tree_visible(tree_map, x, y):
                count += 1
    return count


def compute_scenic_score(tree_map: List[List[int]], x: int, y: int) -> int:
    top = compute_top_scenic_score(tree_map, x, y)
    if top == 0:
        return 0
    bottom = compute_bottom_scenic_score(tree_map, x, y)
    if bottom == 0:
        return 0
    left = compute_left_scenic_score(tree_map, x, y)
    if left == 0:
        return 0
    right = compute_right_scenic_score(tree_map, x, y)
    if right == 0:
        return 0
    return top * bottom * left * right


def find_best_spot_score(tree_map: List[List[int]]) -> int:
    best = 0
    for y in range(len(tree_map)):
        for x in range(len(tree_map[y])):
            score = compute_scenic_score(tree_map, x, y)
            if score > best:
                best = score
    return best


if __name__ == "__main__":
    tree_map = read_tree_map_from_input(INPUT)
    count1 = count_visible_trees(tree_map)
    print(f"Part 1: visible trees = {count1}")

    score2 = find_best_spot_score(tree_map)
    print(f"Part 2: best scenic score = {score2}")

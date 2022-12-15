#!/usr/bin/env python3

import os
from typing import Tuple, Set

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input_to_rock_list(path: str) -> Set[Tuple[int, int]]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()

    rocks = set()
    for line in lines:
        rock_endpoints_str = line.split(" -> ")

        rock_endpoints = []
        for rc in rock_endpoints_str:
            x, y = rc.split(",", 1)
            rock_endpoints.append((int(x), int(y)))

        X, Y = rock_endpoints[0]
        rocks.add((X, Y))
        for i, (xi, yi) in enumerate(rock_endpoints):
            if i == 0:
                continue
            else:
                if xi == X:
                    for k in range(yi, Y, 1 if yi < Y else -1):
                        rocks.add((xi, k))
                elif yi == Y:
                    for k in range(xi, X, 1 if xi < X else -1):
                        rocks.add((k, yi))
                else:
                    raise Exception("points not aligned ?")
            X, Y = (xi, yi)

    return rocks


def get_max_xy(rocks: Set[Tuple[int, int]]) -> Tuple[int, int]:
    max_x = 0
    max_y = 0
    for r in rocks:
        if r[0] > max_x:
            max_x = r[0]
        if r[1] > max_y:
            max_y = r[1]
    return (max_x, max_y)


def get_min_xy(rocks: Set[Tuple[int, int]]) -> Tuple[int, int]:
    min_x = 500
    min_y = 0
    for r in rocks:
        if r[0] < min_x:
            min_x = r[0]
    return (min_x, min_y)


def print_map(rocks: Set[Tuple[int, int]]) -> str:
    message = ""
    max_x, max_y = get_max_xy(rocks)
    min_x, min_y = get_min_xy(rocks)
    for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
            if (x, y) in rocks:
                message += "#"
            else:
                message += "."
        message += "\n"
    return message


def add_sand_bloc_part1(rocks: Set[Tuple[int, int]], limit: int) -> Tuple[Set[Tuple[int, int]], bool]:
    sand = (500, 0)
    limit_reached = False
    while True:
        if sand[1] >= limit:
            limit_reached = True
            break
        if (sand[0], sand[1] + 1) not in rocks:
            sand = (sand[0], sand[1] + 1)
            continue
        elif (sand[0] - 1, sand[1] + 1) not in rocks:
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        elif (sand[0] + 1, sand[1] + 1) not in rocks:
            sand = (sand[0] + 1, sand[1] + 1)
            continue
        else:
            break
    rocks.add(sand)
    return rocks, limit_reached


def get_y_limit(rocks: Set[Tuple[int, int]]) -> int:
    limit = 0
    for r in rocks:
        if r[1] > limit:
            limit = r[1]
    return limit


def simulate_sand_flow_part1(rocks: Set[Tuple[int, int]]) -> int:
    turn = 0
    limit = get_y_limit(rocks)
    while True:
        rocks, limit_reached = add_sand_bloc_part1(rocks, limit)
        if limit_reached:
            break
        turn += 1
    return turn


def add_sand_bloc_part2(rocks: Set[Tuple[int, int]], limit: int) -> Tuple[Set[Tuple[int, int]], bool]:
    sand = (500, 0)
    limit_reached = False
    while True:
        if sand[1] >= limit:
            break
        if (sand[0], sand[1] + 1) not in rocks:
            sand = (sand[0], sand[1] + 1)
            continue
        elif (sand[0] - 1, sand[1] + 1) not in rocks:
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        elif (sand[0] + 1, sand[1] + 1) not in rocks:
            sand = (sand[0] + 1, sand[1] + 1)
            continue
        else:
            if sand == (500, 0):
                limit_reached = True
            break
    rocks.add(sand)
    return rocks, limit_reached


def simulate_sand_flow_part2(rocks: Set[Tuple[int, int]]) -> int:
    turn = 0
    limit = get_y_limit(rocks) + 1
    while True:
        rocks, limit_reached = add_sand_bloc_part2(rocks, limit)
        if limit_reached:
            break
        turn += 1
    return turn


if __name__ == "__main__":
    rocks = read_input_to_rock_list(INPUT)
    limit_reached_at_turn = simulate_sand_flow_part1(rocks)
    print(f"Part 1: {limit_reached_at_turn}")

    rocks = read_input_to_rock_list(INPUT)
    limit_reached_at_turn = simulate_sand_flow_part2(rocks)
    print(f"Part 2: {limit_reached_at_turn + 1}")

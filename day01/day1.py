#!/usr/bin/env python3

import os
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def count_calories_per_elve(food_list: List[str]) -> List[int]:
    calories = []
    current = 0
    for food in food_list:
        if food:
            current += int(food)
        else:
            calories.append(current)
            current = 0
    calories.append(current)
    return calories


def top3(list: List[int]) -> List[int]:
    if len(list) > 3:
        return sorted(list, reverse=True)[:3]
    return sorted(list)


food_list = read_input(f"{SCRIPT_DIR}/input.txt")
calories_per_elve = count_calories_per_elve(food_list)

max_values = top3(calories_per_elve)
print(f"Max 3 values are {max_values}")
print(f"Part 1 result = {max_values[0]}")
print(f"Part 2 result = {sum(max_values)}")

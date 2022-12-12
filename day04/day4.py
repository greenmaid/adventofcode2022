#!/usr/bin/env python3

import os
import re
from typing import List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()

    result = []
    for line in lines:
        match = re.search(r'(\d*)-(\d*),(\d*)-(\d*)', line)
        if match:
            result.append(
                (
                    (int(match.group(1)), int(match.group(2))),
                    (int(match.group(3)), int(match.group(4)))
                )
            )
    return result


def is_full_overlaping(area1: Tuple[int, int], area2: Tuple[int, int]) -> bool:
    if area1[0] <= area2[0] and area1[1] >= area2[1]:
        return True
    return False


def count_full_overlaps(couples_of_areas: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    count = 0
    for areas in couples_of_areas:
        if is_full_overlaping(areas[0], areas[1]) or is_full_overlaping(areas[1], areas[0]):
            count += 1
    return count


def is_partial_overlaping(area1: Tuple[int, int], area2: Tuple[int, int]) -> bool:
    if area1[0] > area2[0]:
        if area1[0] > area2[1]:
            return False
    else:
        if area2[0] > area1[1]:
            return False
    return True


def count_partial_overlaps(couples_of_areas: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    count = 0
    for areas in couples_of_areas:
        if is_partial_overlaping(areas[0], areas[1]):
            count += 1
    return count


areas = read_input(INPUT)
count1 = count_full_overlaps(areas)
print(f"Part 1: overlaping areas = {count1}")

count2 = count_partial_overlaps(areas)
print(f"Part 2: overlaping areas = {count2}")

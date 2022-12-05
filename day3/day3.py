#!/usr/bin/env python3

import os
from typing import List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def get_score_from_char(char: str) -> int:
    if char == char.lower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27


# Part 1 function
#############################################
def get_rucksack_containers(rucksack: str) -> Tuple[str, str]:
    length = len(rucksack)
    middle = int(length/2)
    return (rucksack[:middle], rucksack[middle:])


def find_common_element_in_container(container: Tuple[str, str]) -> str:
    for i in container[0]:
        if container[1].__contains__(i):
            return i
    raise Exception("Common element not found")
    return ""


# Part 2 functions
###########################################
def get_rucksack_groups(rucksacks: List[str]) -> List[Tuple[str, str, str]]:
    groups = []
    while rucksacks:
        groups.append((rucksacks[0], rucksacks[1], rucksacks[2]))
        rucksacks = rucksacks[3:]
    return groups


def find_common_element_in_group(rucksack_group: Tuple[str, str, str]) -> str:
    for i in rucksack_group[0]:
        if rucksack_group[1].__contains__(i):
            if rucksack_group[2].__contains__(i):
                return i
    raise Exception("Common element not found")
    return ""


# Exec
#########################

rucksacks = read_input(INPUT)

score1 = 0
for r in rucksacks:
    el = find_common_element_in_container(get_rucksack_containers(r))
    score1 += get_score_from_char(el)
print(f"Score part 1 = {score1}")

score2 = 0
for gr in get_rucksack_groups(rucksacks):
    el = find_common_element_in_group(gr)
    score2 += get_score_from_char(el)
print(f"Score part 2 = {score2}")

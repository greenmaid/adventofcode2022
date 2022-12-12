#!/usr/bin/env python3

import os
import re
from typing import List, Dict

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT_TEST = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"

STACKS_TEST = f"{SCRIPT_DIR}/stacks_test.txt"
STACKS = f"{SCRIPT_DIR}/stacks.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def read_stacks(path: str) -> Dict[int, List[str]]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()

    stacks: Dict[int, List[str]] = {}

    stacks_count = len(lines[-1].split())
    lines = lines[:-1]

    for i in range(stacks_count):
        stacks[i+1] = []

    for i in range(stacks_count):
        for line in reversed(lines):
            if len(line) >= 4*i+2 and line[4*i+1] != " ":
                stacks[i+1].append(line[4*i+1])
    return stacks


def apply_order(crate_stacks: Dict[int, List[str]], order: str) -> Dict[int, List[str]]:
    match = re.search(r'move (\d*) from (\d*) to (\d*)', order)
    if match:
        crate_count = int(match.group(1))
        source_stack = int(match.group(2))
        target_stack = int(match.group(3))
        for i in range(crate_count):
            moved = crate_stacks[source_stack].pop()
            crate_stacks[target_stack].append(moved)
    return crate_stacks


def apply_orders(crate_stacks: Dict[int, List[str]], orders: List[str]) -> Dict[int, List[str]]:
    for order in orders:
        crate_stacks = apply_order(crate_stacks, order)
    return crate_stacks


def apply_order_2(crate_stacks: Dict[int, List[str]], order: str) -> Dict[int, List[str]]:
    match = re.search(r'move (\d*) from (\d*) to (\d*)', order)
    if match:
        crate_count = int(match.group(1))
        source_stack = int(match.group(2))
        target_stack = int(match.group(3))
        moved = crate_stacks[source_stack][-crate_count:]
        crate_stacks[source_stack] = crate_stacks[source_stack][:-crate_count]
        crate_stacks[target_stack] += moved
    return crate_stacks


def apply_orders_2(crate_stacks: Dict[int, List[str]], orders: List[str]) -> Dict[int, List[str]]:
    for order in orders:
        crate_stacks = apply_order_2(crate_stacks, order)
    return crate_stacks


def get_top_crates(crate_stacks: Dict[int, List[str]]) -> str:
    result = ""
    for i in range(len(crate_stacks)):
        result += crate_stacks[i+1].pop()
    return result


# Part 1
# test
# orders = read_input(INPUT_TEST)
# stacks = read_stacks(STACKS_TEST)
# moved_crate_stacks = apply_orders(stacks, orders)
# print(f"Final stacks = {moved_crate_stacks}")
# print(f"Top crates = {get_top_crates(moved_crate_stacks)}")

orders = read_input(INPUT)
stacks = read_stacks(STACKS)
moved_crate_stacks = apply_orders(stacks, orders)
print(f"Top crates part 1 = {get_top_crates(moved_crate_stacks)}")

# Part 2
# test
# orders = read_input(INPUT_TEST)
# moved_crate_stacks = apply_orders_2(crate_stacks_test, orders)
# print(f"Final stacks = {moved_crate_stacks}")
# print(f"Top crates = {get_top_crates(moved_crate_stacks)}")

orders = read_input(INPUT)
stacks = read_stacks(STACKS)
moved_crate_stacks = apply_orders_2(stacks, orders)
print(f"Top crates part 2 = {get_top_crates(moved_crate_stacks)}")

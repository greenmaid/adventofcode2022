#!/usr/bin/env python3

import os
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> str:
    with open(path, 'r') as f:
        data = f.read()
    return data


# are chars of the input string all different ?
def are_all_different(data: str) -> bool:
    for i in range(len(data)):
        if data.count(data[i]) > 1:
            return False
    return True


def detect_start_signal(data: str) -> int:
    offset = 4
    while not are_all_different(data[:4]):
        data = data[1:]
        offset += 1
    return offset


def detect_start_message(data: str) -> int:
    offset = 14
    while not are_all_different(data[:14]):
        data = data[1:]
        offset += 1
    return offset


data = read_input(INPUT)
print(f"Part 1 signal offset = {detect_start_signal(data)}")
print(f"Part 2 message offset = {detect_start_message(data)}")

#!/usr/bin/env python3

import os
from functools import cmp_to_key
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


class PacketPair():
    def __init__(self, id: int, left: str, right: str):
        self.id = id
        self.left = left
        self.right = right


def read_input_as_pair(path: str) -> List[PacketPair]:
    with open(path, 'r') as f:
        pairs = f.read().split("\n\n")
    pair_list = []
    for i in range(len(pairs)):
        packets = pairs[i].splitlines()
        pair_list.append(PacketPair(id=i+1, left=packets[0], right=packets[1]))
    return pair_list


def str_to_list(data: str) -> List[str]:
    if data.startswith("["):
        inner = data[1:-1]
        result = []
        buffer = ""
        depth = 0
        for char in inner:
            if char == ',' and depth == 0:
                result.append(buffer)
                buffer = ""
            else:
                buffer += char
                if char == '[':
                    depth += 1
                elif char == ']':
                    depth -= 1
        result.append(buffer)
        if depth != 0:
            raise Exception("Wrong parsing")
    else:
        result = [data]
    return [x for x in result if x]  # remove empty string values


def is_in_order(a: str, b: str) -> int:
    left = str_to_list(a)
    right = str_to_list(b)

    for i in range(min(len(left), len(right))):
        # print(f"Compare {left[i]} vs {right[i]}")
        if left[i].startswith("[") or right[i].startswith("["):
            result = is_in_order(left[i], right[i])
            if result != 0:
                return result
        else:
            result = int(right[i]) - int(left[i])
            if result != 0:
                return result
    return len(right) - len(left)


def count_valid_pairs(pairs: List[PacketPair]) -> int:
    ordered = []
    for p in pairs:
        # print(f"{p.id}: {p.left}  /  {p.right}")
        if is_in_order(p.left, p.right) >= 0:
            ordered.append(p.id)
    # print(ordered)
    return sum(ordered)


# Part 2

def read_input_as_list(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return [x for x in lines if x]


def sort_packet_list(packets: List[str]) -> List[str]:
    return sorted(packets, key=cmp_to_key(is_in_order), reverse=True)


def compute_decoder_key(packets: List[str]) -> int:
    packets.append("[[2]]")
    packets.append("[[6]]")

    sorted_packets = sort_packet_list(packets)

    divider1 = sorted_packets.index("[[2]]") + 1
    divider2 = sorted_packets.index("[[6]]") + 1

    return divider1 * divider2


if __name__ == "__main__":
    pair_list = read_input_as_pair(INPUT)
    result = count_valid_pairs(pair_list)
    print(f"Part 1: {result}")

    packets = read_input_as_list(INPUT)
    key = compute_decoder_key(packets)
    print(f"Part 2: {key}")

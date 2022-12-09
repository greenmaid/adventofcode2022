#!/usr/bin/env python3

import os
from dataclasses import dataclass
from math import sqrt
from typing import List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


# in fact I reinvent the Tuple ^^
class Position:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        if other.x == self.x and other.y == self.y:
            return True
        return False

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def __str__(self) -> str:
        return f"Pos({self.x},{self.y})"


class Rope:
    def __init__(self):
        self.head = Position(0, 0)
        self.tail = Position(0, 0)
        self.visited = {Position(0, 0)}  # set ensures unicity

    def move(self, head_move_direction: str, head_move_value: int):
        for i in range(head_move_value):
            if head_move_direction == "U":
                self.head.y += 1
            elif head_move_direction == "D":
                self.head.y -= 1
            elif head_move_direction == "R":
                self.head.x += 1
            elif head_move_direction == "L":
                self.head.x -= 1
            else:
                raise Exception(f"Unknown direction {head_move_direction}")
            self._move_tail()

    def _move_tail(self):
        dist = sqrt((self.head.x - self.tail.x)**2 + (self.head.y - self.tail.y)**2)
        if dist > sqrt(2) + 0.1:
            vect = Position(self.head.x - self.tail.x, self.head.y - self.tail.y)
            if vect.x > 0:
                self.tail.x += 1
            elif vect.x < 0:
                self.tail.x -= 1
            if vect.y > 0:
                self.tail.y += 1
            elif vect.y < 0:
                self.tail.y -= 1
        self.visited.add(self.tail)


def apply_moves(rope: Rope, moves: List[str]):
    for move in moves:
        rope.move(move[0], int(move[2:]))


if __name__ == "__main__":
    my_rope = Rope()
    moves = read_input(INPUT)
    apply_moves(my_rope, moves)
    print(f"Part 1: tail visites = {len(my_rope.visited)}")

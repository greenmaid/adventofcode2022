#!/usr/bin/env python3

import os
from math import sqrt
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


# in fact I reinvent the Tuple ^^
class Position:
    def __init__(self, x: int, y: int):
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
    def __init__(self, length: int = 1):
        self.length = length
        self.knots = [Position(0, 0) for i in range(length + 1)]
        self.visited = {(0, 0)}  # set ensures unicity

    def move(self, head_move_direction: str, head_move_value: int):
        for i in range(head_move_value):
            if head_move_direction == "U":
                self.knots[0].y += 1
            elif head_move_direction == "D":
                self.knots[0].y -= 1
            elif head_move_direction == "R":
                self.knots[0].x += 1
            elif head_move_direction == "L":
                self.knots[0].x -= 1
            else:
                raise Exception(f"Unknown direction {head_move_direction}")
            self._move_knots()

    def _move_knots(self):
        for i in range(self.length):
            head = self.knots[i]
            tail = self.knots[i+1]
            dist = sqrt((head.x - tail.x)**2 + (head.y - tail.y)**2)
            if dist > sqrt(2):
                vect = (head.x - tail.x, head.y - tail.y)
                if vect[0] > 0:
                    self.knots[i+1].x += 1
                elif vect[0] < 0:
                    self.knots[i+1].x -= 1
                if vect[1] > 0:
                    self.knots[i+1].y += 1
                elif vect[1] < 0:
                    self.knots[i+1].y -= 1
        self.visited.add((self.knots[-1].x, self.knots[-1].y))


def apply_moves(rope: Rope, moves: List[str]):
    for move in moves:
        rope.move(move[0], int(move[2:]))


if __name__ == "__main__":
    rope1 = Rope()
    moves = read_input(INPUT)
    apply_moves(rope1, moves)
    print(f"Part 1: tail visites = {len(rope1.visited)}")

    rope2 = Rope(length=9)
    moves = read_input(INPUT)
    apply_moves(rope2, moves)
    print(f"Part 1: tail visites = {len(rope2.visited)}")

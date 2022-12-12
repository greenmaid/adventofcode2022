#!/usr/bin/env python3

import os
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


class Device:
    def __init__(self) -> None:
        self.cycle: int = 0
        self.value: int = 1
        self.store: List[int] = []
        self.message: str = ""

    def noop(self):
        self.cycle += 1

    def addx1(self):
        self.cycle += 1

    def addx2(self, v: int):
        self.cycle += 1
        self.value += v

    def apply(self, instruction: str, step=0):
        previous = self.value
        if instruction.startswith("noop"):
            self.noop()
        elif instruction.startswith("addx"):
            if step == 0:
                self.apply(instruction, step=1)
                self.apply(instruction, step=2)
                return None
            elif step == 1:
                self.addx1()
            elif step == 2:
                self.addx2(int(instruction[5:]))

        self._store(previous)
        self._print(previous)

    # for part 1
    def _store(self, value: int):
        if (self.cycle % 40 - 20) == 0:
            self.store.append(self.cycle * value)

    # for part 2
    def _print(self, value: int):
        crt_position = (self.cycle - 1) % 40
        sprite_position = value
        if crt_position == 0:
            self.message += "\n"
        if crt_position in [sprite_position-1, sprite_position, sprite_position+1]:
            self.message += "#"
        else:
            self.message += " "


if __name__ == "__main__":
    instructions = read_input(INPUT)
    device = Device()
    for instruct in instructions:
        device.apply(instruct)
    print(f"Part 1 : {sum(device.store)}")
    print(f"Part 2 : {device.message}")

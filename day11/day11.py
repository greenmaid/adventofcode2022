#!/usr/bin/env python3

import os
from typing import List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


class Monkey:
    def __init__(self, monkey_id: int, operation: str, test: int, if_true: int, if_false: int, modulo: int = 0):
        self.id = monkey_id
        self.objects: List[int] = []
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected: int = 0
        self.modulo = modulo

    def set_objects(self, objects: List[int]):
        self.objects = objects

    def __str__(self) -> str:
        return f"Monkey{self.id} Objects({self.objects}) Operation({self.operation}) Test({self.test}) IfTrue({self.if_true}) IfFalse({self.if_false}) Inspected({self.inspected})"

    def inspect_object(self) -> Tuple[int, int]:
        item = self.objects.pop(0)
        self.inspected += 1
        new_value = eval(self.operation.replace("old", str(item)))
        if self.modulo == 0:
            new_value = int(new_value / 3)
        else:
            new_value = new_value % self.modulo
        if (new_value % self.test) == 0:
            return (new_value, self.if_true)
        else:
            return (new_value, self.if_false)


def parse_monkey(data: List[str], modulo: int) -> Monkey:
    if not data[0].startswith("Monkey "):
        raise Exception("Invalid monkey")
    monkey_id = int(data[0][7:-1])

    if not data[1].startswith("  Starting items: "):
        raise Exception(f"{monkey_id} Invalid starting items")
    starting_objects_str = data[1][18:].split(", ")
    starting_objects = list(map(int, starting_objects_str))

    if not data[2].startswith("  Operation: new = "):
        raise Exception(f"{monkey_id} Invalid operation")
    operation = data[2][19:]

    if not data[3].startswith("  Test: divisible by "):
        raise Exception(f"{monkey_id} Invalid test")
    test = int(data[3][21:])

    if not data[4].startswith("    If true: throw to monkey "):
        raise Exception(f"{monkey_id} Invalid if true action")
    if_true = int(data[4][29:])

    if not data[5].startswith("    If false: throw to monkey "):
        raise Exception(f"{monkey_id} Invalid if false action")
    if_false = int(data[5][30:])

    monkey = Monkey(monkey_id, operation, test, if_true, if_false, modulo)
    monkey.set_objects(starting_objects)
    return monkey


def parse_monkeys(data: List[str], modulo: int = 0) -> List[Monkey]:
    monkeys = []
    while len(data) > 0:
        monkeys.append(parse_monkey(data[:7], modulo))
        data = data[7:]
    return monkeys


def play_round(monkeys: List[Monkey]):
    for monkey in monkeys:
        while monkey.objects != []:
            thrown = monkey.inspect_object()
            monkeys[thrown[1]].objects.append(thrown[0])


def get_monkey_business(monkeys: List[Monkey]) -> int:
    top_inspected = sorted([m.inspected for m in monkeys])
    return top_inspected[-2] * top_inspected[-1]


if __name__ == "__main__":

    data = read_input(INPUT)
    monkeys = parse_monkeys(data)
    for i in range(20):
        play_round(monkeys)
    result1 = get_monkey_business(monkeys)
    print(f"Part 1: monkey business = {result1}")

    data = read_input(INPUT)
    modulo = 3 * 11 * 19 * 5 * 2 * 7 * 17 * 13
    monkeys = parse_monkeys(data, modulo=modulo)
    for i in range(10000):
        play_round(monkeys)
    result2 = get_monkey_business(monkeys)
    print(f"Part 2: monkey business = {result2}")

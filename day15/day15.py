#!/usr/bin/env python3

import os
import re
from typing import List, Tuple, Optional, Set

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


class Sensor:
    def __init__(self, coordinates: Tuple[int, int], beacon: Tuple[int, int]):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.beacon = beacon
        self.distance = abs(coordinates[0] - beacon[0]) + abs(coordinates[1] - beacon[1])


def read_input_to_sensors(path: str) -> List[Sensor]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    sensors = []
    for line in lines:
        match = re.search(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', line)
        if match:
            new_sensor = Sensor(
                    (int(match.group(1)), int(match.group(2))),
                    (int(match.group(3)), int(match.group(4)))
                )
            sensors.append(new_sensor)
    return sensors


def get_sensor_covered_range_at_y(sensor: Sensor, y: int, maximum: int) -> Optional[Tuple[int, int]]:
    if abs(sensor.y - y) > sensor.distance:
        return None
    remain = sensor.distance - abs(sensor.y - y)
    if os.getenv("ADVENTOFCODE_PART", "1") == "1":
        return (sensor.x - remain, sensor.x + remain)
    else:
        return (max(0, sensor.x - remain), min(sensor.x + remain, maximum))


def fusion_range(a: Set[int], b: Tuple[int, int]) -> Set[int]:
    return a.union(set([*range(b[0], b[1]+1)]))


def get_all_covered_points_at_y(sensors: List[Sensor], y, maximum: int = 4000000) -> Set[int]:
    result: Set[int] = set()
    for sensor in sensors:
        covered_range = get_sensor_covered_range_at_y(sensor, y, maximum)
        if covered_range:
            result = fusion_range(result, covered_range)
    return result


def get_beacons_at_y(sensors: List[Sensor], y) -> Set[int]:
    result: Set[int] = set()
    for sensor in sensors:
        if sensor.beacon[1] == y:
            result.add(sensor.beacon[0])
    return result


# Part2
def get_all_covered_ranges_at_y(sensors: List[Sensor], y: int, maximum: int = 4000000) -> List[Tuple[int, int]]:
    result = []
    for sensor in sensors:
        covered_range = get_sensor_covered_range_at_y(sensor, y, maximum)
        if covered_range:
            result.append(covered_range)
    return result


def reduce_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    ranges.sort()
    new_ranges = []
    left, right = ranges[0]
    for r in ranges[1:]:
        next_left, next_right = r
        if right + 1 < next_left:
            new_ranges.append((left, right))
            left, right = r
        else:
            right = max(right, next_right)
    new_ranges.append((left, right))
    return new_ranges


if __name__ == "__main__":
    os.environ["ADVENTOFCODE_PART"] = "1"
    sensors = read_input_to_sensors(INPUT)
    y = 2000000
    covered = get_all_covered_points_at_y(sensors, y)
    beacons = get_beacons_at_y(sensors, y)
    result = covered - beacons
    print(f"Part 1: {len(result)}")

    os.environ["ADVENTOFCODE_PART"] = "2"
    maximum = 4000000
    for y in range(maximum):
        ranges = get_all_covered_ranges_at_y(sensors, y)
        ranges = reduce_ranges(ranges)
        if len(ranges) > 1:
            x = ranges[0][1] + 1
            print(f"Part 2: missing point ({x},{y})  =>  tuning frequency = {maximum * x + y}")
            break

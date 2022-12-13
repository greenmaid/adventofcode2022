#!/usr/bin/env python3

import igraph as ig  # type: ignore
import os
from typing import List, Tuple


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_grid_from_input(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    grid = []
    for line in lines:
        grid.append([s for s in line])
    return grid


def parse_data_to_heightgraph(data: List[List[str]]) -> Tuple[int, int, ig.Graph]:
    row_count = len(data)
    column_count = len(data[0])
    vertices_count = column_count * row_count
    edges: List[Tuple[int, int]] = []
    for y in range(row_count):
        for x in range(column_count):
            current_id = _get_id_from_coordinates(x, y, column_count)

            if data[y][x] == 'S':
                starting_id = current_id
                data[y][x] = 'a'

            if data[y][x] == 'E':
                ending_id = current_id
                data[y][x] = 'z'

    for y in range(row_count):
        for x in range(column_count):
            current_id = _get_id_from_coordinates(x, y, column_count)

            # check up
            if y > 0 and is_possible_path(data[y][x], data[y-1][x]):
                edges.append((current_id, _get_id_from_coordinates(x, y-1, column_count)))

            # check down
            if y < row_count-1 and is_possible_path(data[y][x], data[y+1][x]):
                edges.append((current_id, _get_id_from_coordinates(x, y+1, column_count)))

            # check left
            if x > 0 and is_possible_path(data[y][x], data[y][x-1]):
                edges.append((current_id, _get_id_from_coordinates(x-1, y, column_count)))

            # check right
            if x < column_count-1 and is_possible_path(data[y][x], data[y][x+1]):
                edges.append((current_id, _get_id_from_coordinates(x+1, y, column_count)))

    heightgraph = ig.Graph(vertices_count, edges, directed=True)
    return (starting_id, ending_id, heightgraph)


def _get_id_from_coordinates(x: int, y: int, column_count: int) -> int:
    return y*column_count + x


def _get_heights_as_int(height: str) -> int:
    return ord(height) - ord('a')


def is_possible_path(height1: str, height2: str) -> bool:
    height1_value = _get_heights_as_int(height1)
    height2_value = _get_heights_as_int(height2)
    if height2_value - height1_value <= 1:
        return True
    return False


def get_all_starting_points(data: List[List[str]]) -> List[int]:
    starting_points = []
    row_count = len(data)
    column_count = len(data[0])
    for y in range(row_count):
        for x in range(column_count):
            if data[y][x] == 'a' or data[y][x] == 'S':
                starting_points.append(_get_id_from_coordinates(x, y, column_count))
    return starting_points


if __name__ == "__main__":

    data = read_grid_from_input(INPUT)
    start_node, end_node, heightgraph = parse_data_to_heightgraph(data)
    distance = heightgraph.distances(source=start_node, target=end_node)
    print(f"Part 1: {distance[0][0]}")

    start_points = get_all_starting_points(data)
    distances = [heightgraph.distances(source=start_node, target=end_node)[0][0] for start_node in start_points]
    distances.sort()
    print(f"Part 2: {distances[0]}")

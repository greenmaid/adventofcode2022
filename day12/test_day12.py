import day12

INPUT_TEST = f"{day12.SCRIPT_DIR}/input_test.txt"


def test_part1():
    data = day12.read_grid_from_input(INPUT_TEST)
    start_node, end_node, heightgraph = day12.parse_data_to_heightgraph(data)

    distance = heightgraph.distances(source=start_node, target=end_node)
    print(f"{start_node} -> {end_node}")
    print(heightgraph)
    print(distance)
    assert distance[0][0] == 31


def test_part2():
    data = day12.read_grid_from_input(INPUT_TEST)
    start_node, end_node, heightgraph = day12.parse_data_to_heightgraph(data)
    start_points = day12.get_all_starting_points(data)
    print(start_points)
    distances = [heightgraph.distances(source=start_node, target=end_node)[0][0] for start_node in start_points]
    distances.sort()
    print(distances)
    assert distances[0] == 29

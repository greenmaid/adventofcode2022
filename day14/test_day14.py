import day14

INPUT_TEST = f"{day14.SCRIPT_DIR}/input_test.txt"


def test_parse_input():
    rocks = day14.read_input_to_rock_list(INPUT_TEST)
    print(day14.print_map(rocks))
    assert (498, 5) in rocks
    assert (502, 7) in rocks
    assert (500, 5) not in rocks


def test_part1():
    rocks = day14.read_input_to_rock_list(INPUT_TEST)
    limit_reached_at_turn = day14.simulate_sand_flow_part1(rocks)
    assert limit_reached_at_turn == 24


def test_part2():
    rocks = day14.read_input_to_rock_list(INPUT_TEST)
    limit_reached_at_turn = day14.simulate_sand_flow_part2(rocks)
    assert limit_reached_at_turn == 92

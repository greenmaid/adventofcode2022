import day8

INPUT_TEST = f"{day8.SCRIPT_DIR}/input_test.txt"
test_map = day8.read_tree_map_from_input(INPUT_TEST)


def test_parse_input():
    assert len(test_map) == 5
    assert len(test_map[0]) == 5
    assert test_map[0][0] == 3
    assert test_map[-1][-1] == 0
    assert test_map[2][2] == 3
    assert test_map[3][2] == 5


def test_top_visibility():
    assert day8.is_tree_visible_from_top(test_map, 0, 0) == True
    assert day8.is_tree_visible_from_top(test_map, 1, 1) == True
    assert day8.is_tree_visible_from_top(test_map, 1, 2) == False
    assert day8.is_tree_visible_from_top(test_map, 4, 3) == True
    assert day8.is_tree_visible_from_top(test_map, 3, 2) == False


def test_bottom_visibility():
    assert day8.is_tree_visible_from_bottom(test_map, 0, 0) == False
    assert day8.is_tree_visible_from_bottom(test_map, 1, 1) == False
    assert day8.is_tree_visible_from_bottom(test_map, 1, 2) == False
    assert day8.is_tree_visible_from_bottom(test_map, 4, 3) == True
    assert day8.is_tree_visible_from_bottom(test_map, 4, 2) == False
    assert day8.is_tree_visible_from_bottom(test_map, 3, 2) == False


def test_left_visibility():
    assert day8.is_tree_visible_from_left(test_map, 0, 0) == True
    assert day8.is_tree_visible_from_left(test_map, 1, 1) == True
    assert day8.is_tree_visible_from_left(test_map, 1, 2) == False
    assert day8.is_tree_visible_from_left(test_map, 4, 3) == True
    assert day8.is_tree_visible_from_left(test_map, 4, 2) == False
    assert day8.is_tree_visible_from_left(test_map, 3, 2) == False


def test_right_visibility():
    assert day8.is_tree_visible_from_right(test_map, 0, 0) == False
    assert day8.is_tree_visible_from_right(test_map, 1, 1) == False
    assert day8.is_tree_visible_from_right(test_map, 1, 2) == True
    assert day8.is_tree_visible_from_right(test_map, 4, 3) == True
    assert day8.is_tree_visible_from_right(test_map, 4, 2) == True
    assert day8.is_tree_visible_from_right(test_map, 3, 2) == True


def test_visibility():
    assert day8.is_tree_visible(test_map, 1, 1) == True
    assert day8.is_tree_visible(test_map, 1, 2) == True
    assert day8.is_tree_visible(test_map, 3, 1) == False
    assert day8.is_tree_visible(test_map, 2, 2) == False


def test_part1():
    assert day8.count_visible_trees(test_map) == 21


def test_scenic_score():
    assert day8.compute_scenic_score(test_map, 2, 1) == 4
    assert day8.compute_scenic_score(test_map, 2, 3) == 8
    assert day8.compute_scenic_score(test_map, 0, 3) == 0
    assert day8.compute_scenic_score(test_map, 2, 4) == 0

def test_part2():
    assert day8.find_best_spot_score(test_map) == 8

import day9
from day9 import Position


def test_rope_step_by_step():
    rope = day9.Rope()
    rope.move("R", 1)
    assert rope.knots[0] == Position(1, 0)
    print(rope.knots[0])
    print(rope.knots[1])
    assert rope.knots[-1] == Position(0, 0)

    rope.move("R", 3)
    assert rope.knots[0] == Position(4, 0)
    assert rope.knots[-1] == Position(3, 0)

    rope.move("U", 4)
    assert rope.knots[0] == Position(4, 4)
    assert rope.knots[-1] == Position(4, 3)

    rope.move("L", 3)
    assert rope.knots[0] == Position(1, 4)
    assert rope.knots[-1] == Position(2, 4)

    rope.move("D", 1)
    assert rope.knots[0] == Position(1, 3)
    assert rope.knots[-1] == Position(2, 4)

    rope.move("R", 4)
    assert rope.knots[0] == Position(5, 3)
    assert rope.knots[-1] == Position(4, 3)

    rope.move("D", 1)
    assert rope.knots[0] == Position(5, 2)
    assert rope.knots[-1] == Position(4, 3)

    rope.move("L", 5)
    assert rope.knots[0] == Position(0, 2)
    assert rope.knots[-1] == Position(1, 2)

    rope.move("R", 2)
    assert rope.knots[0] == Position(2, 2)
    assert rope.knots[-1] == Position(1, 2)

    assert len(rope.visited) == 13


def test_position_set():
    test_set = {day9.Position(0, 0)}
    assert len(test_set) == 1
    test_set.add(day9.Position(1, 0))
    test_set.add(day9.Position(0, 1))
    assert len(test_set) == 3
    test_set.add(day9.Position(1, 0))
    test_set.add(day9.Position(0, 1))
    assert len(test_set) == 3
    test_set.add(day9.Position(-1, 0))
    test_set.add(day9.Position(0, -1))
    assert len(test_set) == 5
    test_set.add(day9.Position(-1, 1))
    test_set.add(day9.Position(1, -1))
    assert len(test_set) == 7
    test_set.add(day9.Position(0, -1))
    test_set.add(day9.Position(1, -1))
    assert len(test_set) == 7


def test_tail_move():
    rope = day9.Rope()
    rope.knots[0] = day9.Position(2, 2)
    rope.knots[-1] = day9.Position(1, 1)
    rope._move_knots()
    assert rope.knots[-1] == day9.Position(1, 1)
    rope.knots[0] = day9.Position(2, 3)
    rope._move_knots()
    assert rope.knots[-1] == day9.Position(2, 2)
    rope.knots[0] = day9.Position(3, 2)
    rope.knots[-1] = day9.Position(1, 1)
    rope._move_knots()
    assert rope.knots[-1] == day9.Position(2, 2)
    for loc in rope.visited:
        print(loc)
    assert len(rope.visited) == 3


def test_part1():
    INPUT_TEST = f"{day9.SCRIPT_DIR}/input_test.txt"
    moves = day9.read_input(INPUT_TEST)
    rope = day9.Rope()
    day9.apply_moves(rope, moves)
    assert len(rope.visited) == 13


def test_part2():
    INPUT_TEST = f"{day9.SCRIPT_DIR}/input_test2.txt"
    moves = day9.read_input(INPUT_TEST)
    rope = day9.Rope(length=9)
    day9.apply_moves(rope, moves)
    assert len(rope.visited) == 36

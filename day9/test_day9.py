import day9
from day9 import Position

INPUT_TEST = f"{day9.SCRIPT_DIR}/input_test.txt"
moves = day9.read_input(INPUT_TEST)


def test_rope_step_by_step():
    rope = day9.Rope()
    rope.move("R", 1)
    assert rope.head == Position(1, 0)
    assert rope.tail == Position(0, 0)

    rope.move("R", 3)
    assert rope.head == Position(4, 0)
    assert rope.tail == Position(3, 0)

    rope.move("U", 4)
    assert rope.head == Position(4, 4)
    assert rope.tail == Position(4, 3)

    rope.move("L", 3)
    assert rope.head == Position(1, 4)
    assert rope.tail == Position(2, 4)

    rope.move("D", 1)
    assert rope.head == Position(1, 3)
    assert rope.tail == Position(2, 4)

    rope.move("R", 4)
    assert rope.head == Position(5, 3)
    assert rope.tail == Position(4, 3)

    rope.move("D", 1)
    assert rope.head == Position(5, 2)
    assert rope.tail == Position(4, 3)

    rope.move("L", 5)
    assert rope.head == Position(0, 2)
    assert rope.tail == Position(1, 2)

    rope.move("R", 2)
    assert rope.head == Position(2, 2)
    assert rope.tail == Position(1, 2)

    assert len(rope.visited) == 13


def test_part1():
    rope = day9.Rope()
    day9.apply_moves(rope, moves)
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
    rope.head = day9.Position(2, 2)
    rope.tail = day9.Position(1, 1)
    rope._move_tail()
    assert rope.tail == day9.Position(1, 1)
    rope.head = day9.Position(2, 3)
    rope._move_tail()
    assert rope.tail == day9.Position(2, 2)
    rope.head = day9.Position(3, 2)
    rope.tail = day9.Position(1, 1)
    rope._move_tail()
    assert rope.tail == day9.Position(2, 2)
    for loc in rope.visited:
        print(loc)
    assert len(rope.visited) == 3

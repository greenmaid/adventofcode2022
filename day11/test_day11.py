import day11

INPUT_TEST = f"{day11.SCRIPT_DIR}/input_test.txt"


monkey0_description = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

""".splitlines()


def test_parse_monkey():
    monkey0 = day11.parse_monkey(monkey0_description)
    print(monkey0)
    assert monkey0.id == 0
    assert monkey0.operation == "old * 19"
    assert monkey0.if_true == 2
    assert monkey0.objects == [79, 98]


def test_parse_monkeys():
    data = day11.read_input(INPUT_TEST)
    monkeys = day11.parse_monkeys(data)
    for m in monkeys:
        print(m)
    assert len(monkeys) == 4


def test_inspect_object():
    monkey0 = day11.parse_monkey(monkey0_description)

    result1 = monkey0.inspect_object()
    assert len(monkey0.objects) == 1
    assert result1[0] == 500
    assert result1[1] == 3

    result2 = monkey0.inspect_object()
    assert len(monkey0.objects) == 0
    assert result2[0] == 620
    assert result2[1] == 3


def test_play_round():
    data = day11.read_input(INPUT_TEST)
    monkeys = day11.parse_monkeys(data)
    day11.play_round(monkeys)
    assert monkeys[0].objects == [20, 23, 27, 26]
    assert monkeys[1].objects == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].objects == []
    assert monkeys[3].objects == []


def test_part1():
    data = day11.read_input(INPUT_TEST)
    monkeys = day11.parse_monkeys(data)
    for i in range(20):
        day11.play_round(monkeys)

    for m in monkeys:
        print(m)
    print()
    assert day11.get_monkey_business(monkeys) == 10605

import day10

INPUT_TEST = f"{day10.SCRIPT_DIR}/input_test.txt"
instructions = day10.read_input(INPUT_TEST)


def test_part1():
    device = day10.Device()
    for instruct in instructions:
        print(f">> {instruct}")
        device.apply(instruct)
    print(device.store)
    assert sum(device.store) == 13140

import day13


INPUT_TEST = f"{day13.SCRIPT_DIR}/input_test.txt"


def test_parse_input():
    pair_list = day13.read_input_as_pair(INPUT_TEST)
    for p in pair_list:
        print(f"{p.id}: {p.left}  /  {p.right}")
    assert pair_list[0].id == 1
    assert pair_list[0].left == "[1,1,3,1,1]"
    assert pair_list[0].right == "[1,1,5,1,1]"
    assert pair_list[7].id == 8
    assert pair_list[7].right == "[1,[2,[3,[4,[5,6,0]]]],8,9]"


def test_parse_imbricated_list():
    assert day13.str_to_list("[1,1,3,1,1]") == ["1", "1", "3", "1", "1"]
    assert day13.str_to_list("[[1],[2,3,4]]") == ["[1]", "[2,3,4]"]
    assert day13.str_to_list("[[8,7,6]]") == ["[8,7,6]"]
    assert day13.str_to_list("[1,[2,[3,[4,[5,6,7]]]],8,9]") == ["1", "[2,[3,[4,[5,6,7]]]]", "8", "9"]
    assert day13.str_to_list("1") == ["1"]


def test_ordering():
    assert day13.is_in_order("[1,1,3,1,1]", "[1,1,5,1,1]") == 2
    assert day13.is_in_order("[[1],[2,3,4]]", "[[1],4]") == 2
    assert day13.is_in_order("[9]", "[[8,7,6]]") == -1
    assert day13.is_in_order("[[4,4],4,4]", "[[4,4],4,4,4]") == 1
    assert day13.is_in_order("[7,7,7,7]", "[7,7,7]") == -1
    assert day13.is_in_order("[]", "[3]") == 1
    assert day13.is_in_order("[[[]]]", "[[]]") == -1
    assert day13.is_in_order("[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]") == -7
    assert day13.is_in_order("[3]", "[3]") == 0
    assert day13.is_in_order("[0,0,0]", "2") == 2


def test_part1():
    pair_list = day13.read_input_as_pair(INPUT_TEST)
    result = day13.count_valid_pairs(pair_list)
    assert result == 13


def test_part2():
    packets = day13.read_input_as_list(INPUT_TEST)
    key = day13.compute_decoder_key(packets)
    assert key == 140

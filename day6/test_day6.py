import day6


def test_signal_detection():
    data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    assert day6.are_all_different(data[:4]) == False

    data = "jpqmgbljsphdztnvjfqwrcgsmlb"
    assert day6.are_all_different(data[:4]) == True


def test_detect_signal():
    data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    assert day6.detect_start_signal(data) == 7

    data2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    assert day6.detect_start_signal(data2) == 5

    data3 = "nppdvjthqldpwncqszvftbrmjlhg"
    assert day6.detect_start_signal(data3) == 6

    data4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    assert day6.detect_start_signal(data4) == 10

    data5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    assert day6.detect_start_signal(data5) == 11


def test_detect_message():
    data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    assert day6.detect_start_message(data) == 19

    data2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    assert day6.detect_start_message(data2) == 23

    data3 = "nppdvjthqldpwncqszvftbrmjlhg"
    assert day6.detect_start_message(data3) == 23

    data4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    assert day6.detect_start_message(data4) == 29

    data5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    assert day6.detect_start_message(data5) == 26

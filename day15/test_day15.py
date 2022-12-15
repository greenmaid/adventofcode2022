import day15

INPUT_TEST = f"{day15.SCRIPT_DIR}/input_test.txt"


def test_parse_sensors():
    sensors = day15.read_input_to_sensors(INPUT_TEST)
    for sensor in sensors:
        print(f"Sensor x={sensor.x} y={sensor.y} => nearest beacon={sensor.beacon} distance={sensor.distance}")
    assert len(sensors) == 14
    assert sensors[0].distance == 7
    assert sensors[0].x == 2
    assert sensors[1].y == 16
    assert sensors[1].distance == 1
    assert sensors[13].distance == 7


def test_get_sensor_covered_range_at_y():
    sensor = day15.Sensor((8, 7), (2, 10))
    assert day15.get_sensor_covered_range_at_y(sensor, 16, maximum=20) == (8, 8)
    assert day15.get_sensor_covered_range_at_y(sensor, 10, maximum=20) == (2, 14)


def test_fusion_range():
    inital_set = {1, 2, 3}
    assert day15.fusion_range(inital_set, [5, 6]) == {1, 2, 3, 5, 6}
    assert day15.fusion_range(inital_set, [1, 6]) == {1, 2, 3, 4, 5, 6}
    assert day15.fusion_range(inital_set, [-1, 2]) == {-1, 0, 1, 2, 3}


def test_part1():
    sensors = day15.read_input_to_sensors(INPUT_TEST)
    covered = day15.get_all_covered_points_at_y(sensors, 10)
    print(covered)
    assert len(covered) == 27

    beacons = day15.get_beacons_at_y(sensors, 10)
    result = covered - beacons
    assert len(result) == 26


def test_reduce_ranges():
    assert day15.reduce_ranges([(10, 20), (30, 50)]) == [(10, 20), (30, 50)]
    assert day15.reduce_ranges([(30, 50), (10, 20)]) == [(10, 20), (30, 50)]
    assert day15.reduce_ranges([(30, 50), (10, 20), (15, 35)]) == [(10, 50)]
    assert day15.reduce_ranges([(30, 50), (10, 20), (15, 35), (0, 60)]) == [(0, 60)]

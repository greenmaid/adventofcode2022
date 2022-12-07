import day7

INPUT_TEST = f"{day7.SCRIPT_DIR}/input_test.txt"
test_listing = day7.read_input(INPUT_TEST)


def test_add_directory():
    root = day7.Directory("root")
    sub_dir = day7.Directory("sub_dir")
    root.add_dir(sub_dir)
    assert len(root.dirs) == 1
    assert len(sub_dir.dirs) == 0


def test_add_file():
    root = day7.Directory("root")
    F1 = day7.File("file1", 100)
    root.add_file(F1)
    assert len(root.files) == 1
    F2 = day7.File("file2", 1000)
    root.add_file(F2)
    assert len(root.files) == 2


def test_imbricated_directories():
    root = day7.Directory("root")
    sub_dir = day7.Directory("sub_dir")
    sub_sub_dir = day7.Directory("sub_sub_dir")

    root.add_dir(sub_dir)
    sub_dir.add_dir(sub_sub_dir)

    print([d.name for d in root.dirs])
    assert len(root.dirs) == 1
    assert len(sub_dir.dirs) == 1
    assert len(sub_sub_dir.dirs) == 0


def test_list_sub_directories():
    root = day7.build_fs_tree(test_listing)
    print(root)
    assert len(root.list_sub_directories()) == 3


def test_directory_size_count():
    root = day7.build_fs_tree(test_listing)
    assert root.count_directory_size() == 48381165


def test_part1():
    root = day7.build_fs_tree(test_listing)
    selected_dir = root.list_sub_directories_with_max_size(max_size=100000)
    assert len(selected_dir) == 2
    count = 0
    for d in selected_dir:
        count += d.count_directory_size()
    assert count == 95437

def test_part2():
    root = day7.build_fs_tree(test_listing)
    result = root.find_smallest_dir_greater_than(21618835)
    assert result.name == "d"
    assert result.count_directory_size() == 24933642

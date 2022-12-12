#!/usr/bin/env python3

import os
import re
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT = f"{SCRIPT_DIR}/input.txt"


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.dirs: List[Directory] = []
        self.files: List[File] = []

    def __str__(self) -> str:
        message = f"{self.name}: "
        for f in self.files:
            message += f"{f.name}({f.size}) "
        for d in self.dirs:
            message += f"dir({d.__str__()}) "
        return message

    def add_dir(self, new_directory: 'Directory'):
        self.dirs.append(new_directory)

    def add_file(self, new_file: File):
        self.files.append(new_file)

    def get_dir_by_name(self, name: str) -> 'Directory':
        for directory in self.dirs:
            if directory.name == name:
                return directory
        raise Exception("Directory not found")

    def count_directory_size(self) -> int:
        size = 0
        for f in self.files:
            size += f.size
        for d in self.dirs:
            size += d.count_directory_size()
        return size

    def list_sub_directories(self) -> List['Directory']:
        result = []
        for d in self.dirs:
            result.append(d)
            result += d.list_sub_directories()
        return result

    def list_sub_directories_with_max_size(self, max_size: int) -> List['Directory']:
        result = []
        for d in self.list_sub_directories():
            if d.count_directory_size() <= max_size:
                result.append(d)
        return result

    def find_smallest_dir_greater_than(self, size: int) -> 'Directory':
        best_result = self
        for d in self.list_sub_directories():
            current_size = d.count_directory_size()
            if current_size >= size and current_size < best_result.count_directory_size():
                best_result = d
        return best_result


def build_fs_tree(listing: List[str]) -> Directory:
    root = Directory("/")
    path = [root]
    for line in listing:
        if line.startswith("$ cd "):
            entering_dir = line[5:]
            if entering_dir == "..":
                path.pop()
            elif entering_dir == "/":
                path = [root]
            else:
                current_dir = path[-1]
                entering_directory = current_dir.get_dir_by_name(entering_dir)
                path.append(entering_directory)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            new_dir = line[4:]
            current_dir = path[-1]
            current_dir.add_dir(Directory(new_dir))
        else:
            current_dir = path[-1]
            match = re.search(r'^(\d*) (.*)$', line)
            if match:
                size = int(match.group(1))
                filename = match.group(2)
                new_file = File(filename, size)
                current_dir.add_file(new_file)
            else:
                raise Exception(f"Undefined input : {line}")
    return root


if __name__ == "__main__":
    listing = read_input(INPUT)
    root = build_fs_tree(listing)
    selected_dir = root.list_sub_directories_with_max_size(max_size=100000)

    count = 0
    for d in selected_dir:
        count += d.count_directory_size()
    print(f"Part 1 : Sum = {count}")

    current_used = root.count_directory_size()
    free = 70000000 - root.count_directory_size()
    needed = 30000000 - free

    best_target = root.find_smallest_dir_greater_than(needed)
    print(f"Part 2 : needed space = {needed}, best directory to delete is {best_target.name} with size {best_target.count_directory_size()}")

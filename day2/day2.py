import os
from typing import List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[Tuple[str, str]]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()

    return [(line[0],line[2]) for line in lines]


def compute_score_part1(match: Tuple[str, str]) -> int:
    score = 0
    if match[1] == 'X':
        score += 1
        if match[0] == 'A':
            score += 3
        elif match[0] == 'C':
            score += 6
    elif match[1] == 'Y':
        score += 2
        if match[0] == 'B':
            score += 3
        elif match[0] == 'A':
            score += 6
    elif match[1] == 'Z':
        score += 3
        if match[0] == 'C':
            score += 3
        elif match[0] == 'B':
            score += 6
    return score


def compute_score_part2(match: Tuple[str, str]) -> int:
    score = 0
    if match[1] == 'X':
        if match[0] == 'A':
            score += 3
        elif match[0] == 'B':
            score += 1
        elif match[0] == 'C':
            score += 2
    elif match[1] == 'Y':
        score += 3
        if match[0] == 'A':
            score += 1
        elif match[0] == 'B':
            score += 2
        elif match[0] == 'C':
            score += 3
    elif match[1] == 'Z':
        score += 6
        if match[0] == 'A':
            score += 2
        elif match[0] == 'B':
            score += 3
        elif match[0] == 'C':
            score += 1
    return score


def compute_scores(match_list: List[Tuple[str, str]]):
    score1 = 0
    for match in match_list:
        score1 += compute_score_part1(match)
    print(f"Part 1 final score = {score1}")

    score2 = 0
    for match in match_list:
        score2 += compute_score_part2(match)
    print(f"Part 2 final score = {score2}")


matches = read_input(f"{SCRIPT_DIR}/input.txt")
compute_scores(matches)

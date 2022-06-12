from collections import Counter
from typing import List, Callable

def read_lines(path: str) -> List[str]:
    with open(path) as f:
        lines = f.read().split()
    return lines 


def generate_rating(
    lines: List[str], length: int, func: Callable, d: str
    ) -> str:
    rows = set(lines)
    for i in range(length):
        nums = Counter([row[i] for row in rows])
        if nums['0'] == nums['1']:
            delete = d
        else:
            delete = func(nums, key=nums.get)
        to_delete = {row for row in rows if row[i] == delete} 
        rows = rows - to_delete
        if len(rows) == 1:
            return str(*rows)


def part_2(path):
    lines = read_lines(path)
    l = len(lines[0])
    co2 = generate_rating(lines, l, min, '0')
    oxygen = generate_rating(lines, l, max, '1')
    if co2 and oxygen:
        return int(co2, 2) * int(oxygen, 2)
    return False


part_2('3/input.txt')








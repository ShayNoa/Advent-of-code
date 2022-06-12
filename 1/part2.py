from typing import List

def read_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines


def window(iterable: List[str], n: int) -> List[str]:
    for i in range(len(iterable) - n + 1):
        yield iterable[i:i+n]


def count_increases(path:str) -> int:
    counter = prev = 0
    lines = read_lines(path)
    for rows in window(lines, 3):
        rows_sum = sum(int(row) for row in rows)
        if rows_sum > prev:
            counter += 1
        prev = rows_sum
    return counter - 1


print(count_increases('1/input.txt')) 


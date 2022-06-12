from dataclasses import dataclass

@dataclass
class Position:
    horizontal: int 
    depth: int


def read_lines(path: str) -> int:
    for row in open(path, 'r'):
        direction, num = row.strip().split()
        yield direction, int(num) 


def part_1(path: str) -> int:
    position = Position(0, 0)
    for direction, num in read_lines(path):
        if direction == 'down':
            position.depth += num
        elif direction == 'up':
            position.depth -= num
        else:
            position.horizontal += num
    return position.depth * position.horizontal


part_1('2/input.txt')
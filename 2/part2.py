from dataclasses import dataclass

@dataclass
class Position:
    horizontal: int 
    depth: int
    aim: int


def read_lines(path: str) -> int:
    for row in open(path, 'r'):
        direction, num = row.strip().split()
        yield direction, int(num) 


def part_2(path: str) -> int:
    position = Position(0, 0, 0)
    for direction, num in read_lines(path):
        if direction == 'down':
            position.aim += num
        elif direction == 'up':
            position.aim -= num
        else:
            position.horizontal += num
            position.depth += (position.aim * num)
    return position.depth * position.horizontal


part_2('2/input.txt')

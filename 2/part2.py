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


def calc_position(path: str) -> int:
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


print(calc_position('2/input.txt')) # 2044620088

from pathlib import Path
import numpy

MARKED = -1

class Board:
    def __init__(self, nums): 
        pass

def read_input():
    with open('4/input.txt') as f:
        nums = list(map(int, next(f).split(",")))
        is_next = next(f, None)
        while is_next:
            yield [list(map(int, next(f, None).split())) for i in range(5)]
            is_next = next(f, None)

for board in read_input():
    print(board)
    
        


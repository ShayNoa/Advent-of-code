
def generate_lines(path: str) -> int:
    for row in open(path, 'r'):
        yield int(row.strip())
        

def count_increased(path: str) -> int: 
    counter = 0
    prev = 0
    for num in generate_lines(path):
        if num > prev:
            counter += 1
        prev = num
    return counter - 1
        
print(count_increased('1/input.txt')) 

    
from collections import Counter


def read_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines


def count_vertival(path):
    lines = read_lines(path)
    length = len(lines[0].strip())
    gamma, espilon = '', ''
    for i in range(length):
        nums = Counter([line[i] for line in lines])
        gamma += max(nums, key=nums.get)
        espilon += min(nums, key=nums.get)
    return int(gamma, 2) * int(espilon, 2)


print(count_vertival('3/input.txt')) # 693486







        

    
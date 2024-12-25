from openFile import openFile
from itertools import product

data = []

openFile(data, "data/day7.txt")

def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def join(num1, num2):
    return int(str(num1) + str(num2))

func_tup = (add, mul, join)


def binary_options(size):
    return [bits for bits in product([0, 1, 2], repeat=size)]


def calculation(key, value, possibilities, size):
    if size == 1:
        for func_index in range(2):
            result = func_tup[func_index](value[0], value[1])  
            if result == int(key):
                return True
        return False

    else:
        length = len(possibilities)
        for l_index in range(length):
            result = value[0]
            for num, tup_index in zip(range(1, len(value)), range(len(possibilities[l_index]))):
                result = func_tup[possibilities[l_index][tup_index]](result, value[num])
            if result == int(key):
                return True
        return False  



lines = {}

for line in data:
    lines[line.split(":")[0]] = tuple(int(num) for num in line.split(":")[1].split(" ")[1:])

valid_nums = []

for answer, input_list in lines.items():
    length = len(input_list) - 1
    carry_over = 0
    possibilities = binary_options(length)
    if calculation(answer, input_list, possibilities, length):
        valid_nums.append(int(answer))

print(sum(valid_nums))

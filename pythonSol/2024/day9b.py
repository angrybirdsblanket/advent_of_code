from openFile import openFile
import copy

data = []

file_block_size = []
file_gap_size = []

openFile(data, "data/day9test.txt")

for i in range(len(data[0])):
    if i % 2 == 0:
        file_block_size.append(data[0][i])
    else:
        file_gap_size.append(data[0][i])

file_table = []

for i in range(len(file_block_size)):
    file_table.extend([str(i)] * int(file_block_size[i]))
    
    if i < len(file_block_size) - 1:
        file_table.extend(['.'] * int(file_gap_size[i]))

old_file_table = copy.deepcopy(file_table)

print(file_gap_size)

for i in range(-1, -(len(file_block_size)), -1):
    gap_index = 0
    for j in range(len(file_gap_size)):
        if int(file_block_size[i]) < int(file_gap_size[j]):
            length = len(file_block_size[i]) * int(file_block_size[i])

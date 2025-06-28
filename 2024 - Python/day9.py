from openFile import *
import copy

file_block_size = []
file_gap_size = []

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

# old_file_table = copy.deepcopy(file_table)
#
# for i in range(len(file_table) - 1, -1, -1):
#     dot = file_table.index(".")
#     if old_file_table[i] != "." and dot < i:
#         file_table[i], file_table[dot] = file_table[dot], file_table[i]
#
# checksum = 0
#
# for i in range(len(file_table)):
#     if file_table[i] != ".":
#         checksum += int(file_table[i]) * i
#
print(file_table)


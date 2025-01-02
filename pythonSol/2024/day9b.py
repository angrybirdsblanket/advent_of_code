from openFile import openFile
import copy

def find_gap_that_fits(file_table, size):
    gap_start = -1
    gap_size = 0
    
    for i in range(len(file_table)):
        if file_table[i] == '.':
            if gap_start == -1:
                gap_start = i
            gap_size += 1
            if gap_size >= size:
                return gap_start
        else:
            gap_start = -1
            gap_size = 0
    return -1

def find_file_range(file_table, file_id):
    indices = [i for i, x in enumerate(file_table) if x == file_id]
    if indices:
        return min(indices), max(indices) + 1
    return -1, -1

data = []
file_block_size = {}
file_gap_size = []
openFile(data, "data/day9.txt")

# Parse input
for i in range(len(data[0])):
    if i % 2 == 0:
        file_block_size[i//2] = int(data[0][i])  # Remove str() conversion
    else:
        file_gap_size.append(int(data[0][i]))

# Build file table
file_table = []
for i, (block_id, size) in enumerate(file_block_size.items()):
    file_table.extend([block_id] * size)  # Keep block_id as integer
    if i < len(file_gap_size):
        file_table.extend("." * file_gap_size[i])

# Process files in reverse ID order
for file_id in range(len(file_block_size) - 1, -1, -1):
    file_start, file_end = find_file_range(file_table, file_id)  # Pass integer file_id
    if file_start == -1:
        continue
        
    file_size = file_end - file_start
    gap_start = find_gap_that_fits(file_table, file_size)
    
    if gap_start != -1 and gap_start < file_start:
        file_table[gap_start:gap_start + file_size] = file_table[file_start:file_end]
        file_table[file_start:file_end] = ['.'] * file_size

checksum = sum(block * i for i, block in enumerate(file_table) if block != '.')
print(checksum)

from openFile import openFile
import sys
from collections import deque

data = []

openFile(data, sys.argv[1])

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(data, row, col, char):
    queue = deque([(row, col)])
    row_length = len(data)
    col_length = len(data[0])
    visited = set()
    group_coordinates = []
    count = 0

    while queue:
        c_row, c_col = queue.popleft()
        if (c_row, c_col) in visited:
            continue
        visited.add((c_row, c_col))
        group_coordinates.append((c_row, c_col))
        count += 1
        for direction in DIRECTIONS:
            new_row, new_col = c_row + direction[0], c_col + direction[1]
            if (
                0 <= new_row < row_length
                and 0 <= new_col < col_length
                and data[new_row][new_col] == char
                and (new_row, new_col) not in visited
            ):
                queue.append((new_row, new_col))

    group_coordinates.sort()
    return tuple(group_coordinates), count

def neighbours(data, row, col):
    count = 0
    char = data[row][col]
    for direction in DIRECTIONS:
        n_row, n_col = row + direction[0], col + direction[1]
        if 0 <= n_row < len(data) and 0 <= n_col < len(data[0]):
            if data[n_row][n_col] == char:
                count += 1
    
    return count

def cal_perimeter(data, set_data):
    count = 0
    
    for char in set_data:
        count += (4 - neighbours(data, char[0], char[1]))

    return count


groups = set()  

sum = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if any((i, j) in group for group in groups):
            continue
        group, area = bfs(data, i, j, data[i][j])
        groups.add(group)
        sum += area * cal_perimeter(data, group)

print(sum)

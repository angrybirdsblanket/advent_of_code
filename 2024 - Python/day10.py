from openFile import data

def bfs(data, row, col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [(row, col, int(data[row][col]))]
    row_length = len(data)
    col_length = len(data[0])
    visited = set()
    count = 0

    while len(queue) > 0:
        curr_row, curr_col, num = queue.pop(0)
        
        if (curr_row, curr_col) in visited:
            continue

        visited.add((curr_row, curr_col)) 

        if num == 9:
            count += 1
            continue
        
        for direction in directions:
            new_row, new_col = curr_row + direction[0], curr_col + direction[1]
            if 0 <= new_row < row_length and 0 <= new_col < col_length:
                next_num = int(data[new_row][new_col])
                if next_num == num + 1 and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, next_num))
    return count


count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if int(data[i][j]) == 0:
           count += bfs(data, i, j)

print(count)

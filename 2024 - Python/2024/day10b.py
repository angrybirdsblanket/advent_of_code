# to whoever finds this, funnily enough turns out while trying to do part 1 i got the solution for part 2 so that saves me a lot of time, since i know how it works

from openFile import openFile

data = []

openFile(data, "data/day10.txt")

def step_through(data, row, col, num):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0

    if num == 8:
        for direction in directions:
            new_row, new_col = direction[0] + row, direction[1] + col
            if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and int(data[new_row][new_col]) == 9:
                count += 1
        return count
    else:
        for direction in directions:
            new_row, new_col = direction[0] + row, direction[1] + col
            if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]) and int(data[new_row][new_col]) == num + 1:
                count += step_through(data, new_row, new_col, num + 1)

    return count


count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if int(data[i][j]) == 0:
            count += step_through(data, i, j, 0)

print(count)

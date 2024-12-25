from openFile import openFile

def walls(tup_1, tup_2, data):
    count = 0
    direction = (-(tup_1[0] - tup_2[0]), -(tup_1[1] - tup_2[1]))
    col = len(data)
    length = len(data[0])
    
    if 0 <= tup_1[0] - direction[0] and 0 <= tup_1[1] - direction[1] < length and data[tup_1[0] - direction[0]][tup_1[1] - direction[1]] == ".":
        count += 1
        # print(tup_1, tup_2)

    if col > tup_2[0] + direction[0] and 0 <= tup_2[1] + direction[1] < length and data[tup_2[0] + direction[0]][tup_2[1] + direction[1]] == ".":
        count += 1
        # print(tup_1, tup_2)

    return count
    
data = []

openFile(data, "data/day8.txt")

indices = []
for index, line in enumerate(data):
    for i in range(len(line)):
        if line[i].isalnum():
            indices.append((index, i))

count = 0
for i in range(len(indices)):
    for j in range(i + 1, len(indices)):
        if data[indices[i][0]][indices[i][1]] == data[indices[j][0]][indices[j][1]]:
            count += walls(indices[i], indices[j], data)

print(count)

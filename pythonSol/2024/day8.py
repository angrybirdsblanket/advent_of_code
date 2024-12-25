from openFile import openFile

data = []

openFile(data, "data/day8test.txt")

indices = []
for index, line in enumerate(data):
    for i in range(len(line)):
        if line[i].isalnum():
            indices.append((index, i))

for index in indices:
    print(index)

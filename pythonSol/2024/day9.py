from openFile import openFile

data = []

file_block_size = []

file_gap_size = []

openFile(data, "data/day9test.txt")

for i in range(len(data[0])):
    if i % 2 == 0:
        file_block_size.append(data[0][i])
    else:
        file_gap_size.append(data[0][i])


file_table = ""

for i in range(len(file_block_size)):
    if i < len(file_block_size) - 1:
        file_table += str(i) * int(file_block_size[i]) 
        file_table += "." * int(file_gap_size[i])
    else:
        file_table += str(i) * int(file_block_size[i])

print(data[0])
print(file_table)

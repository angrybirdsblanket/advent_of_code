import re
from openFile import openFile

arr = []
file = "data/day3.txt"

result = []
openFile(arr, file)
for i in range(0, len(arr)):
    result.append(re.findall(r"mul\(\d+,\d+\)", arr[i]))

pairs = []
sum = 0
# print(result)
for i in range(0, len(result)):
    for j in range(0, len(result[i])):
        result[i][j] = result[i][j][4:-1]
        pairs.append(result[i][j].split(","))
for pair in pairs:
    sum += int(pair[0]) * int(pair[1])
print(sum)

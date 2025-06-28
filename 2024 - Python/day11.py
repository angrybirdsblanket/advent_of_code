from openFile import *

def blink(line):
    new_line = []
    for num in line:
        match num:
            case 0:
                new_line.append(1)
            case _ if len(str(num)) % 2 == 0:
                new_num, mid = str(num), len(str(num)) // 2
                new_line.append(int(new_num[:mid]))
                new_line.append(int(new_num[mid:]))
            case _:
                new_line.append(num * 2024)
    return new_line

data = data[0].split(" ")

for i in range(len(data)):
    data[i] = int(data[i])

for i in range(25):
    data = blink(data)

print(len(data))

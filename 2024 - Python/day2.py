from openFile import *

def clean_data(data):
    temp = []
    for item in data:
        temp.append(item.split(" "))
    return temp

data = clean_data(data)

safe = 0

for i in range(0, len(data)):
    data[i][len(data[i])-1] = data[i][len(data[i])-1][0:-1]

    for j in range(0, len(data[i])):
        data[i][j] = int(data[i][j])

    if data[i] in [sorted(data[i], reverse = True), sorted(data[i])]:
        arr = []
        for j in range(0, len(data[i])-1):
            difference = abs(data[i][j] - data[i][j + 1])
            arr.append(difference)
        if max(arr) <= 3 and min(arr) >= 1:
            safe += 1
            
print(safe)
exit(0)

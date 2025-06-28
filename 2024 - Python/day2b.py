data = []

def calculateDifference(input, arr):
    for i in range (0, len(input) - 1):
        difference = abs(input[i] - input[i+1])
        arr.append(difference)

with open("data/2024/day2.txt", "r") as db: 
    x = db.readlines()
    for i in range(len(x)):
        arr = x[i].split(" ")
        arr[len(arr) - 1] = arr[len(arr) - 1][0:-1]
        for j in range(0, len(arr)):
            arr[j] = int(arr[j])
        data.append(arr)

safe = 0

for row in data:
    arr = []
    if row in [sorted(row), sorted(row, reverse=True)]:
        calculateDifference(row, arr)
        if max(arr) <= 3 and min(arr) >= 1:
            safe += 1
        else:
            for j in range(len(row)):
                arr = []
                subset = row[:j] + row[j+1:]
                if subset in [sorted(subset), sorted(subset, reverse=True)]:
                    calculateDifference(subset, arr)
                    if max(arr) <= 3 and min(arr) >= 1:
                        safe += 1
                        break
                        
    else:
        for j in range(len(row)):
            arr = []
            subset = row[:j] + row[j+1:]
            if subset in [sorted(subset), sorted(subset, reverse=True)]:
                calculateDifference(subset, arr)
                if max(arr) <= 3 and min(arr) >= 1:
                    safe += 1
                    break
print(safe)
exit(0)

from openFile import openFile

data = []

openFile(data, "data/day1.txt")

list1 = []
list2 = []

for line in data:
    list1.append(line.split("   ")[0])
    list2.append(line.split("   ")[1])



list1.sort()
list2.sort()
sum = 0
for i in range (0, len(list1)):
        sum += abs(int(list1[i]) - int(list2[i]))
print(sum)

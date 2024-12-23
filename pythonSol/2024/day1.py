with open("../../data/day1victoria.txt", "r") as db:
    x = db.readlines()
    list1 = []
    list2 = []
    for line in x:
        listtemp = line.split("   ")
        listtemp[1] = listtemp[1][0:-1]
        list1.append(listtemp[0])
        list2.append(listtemp[1])

list1.sort()
list2.sort()
sum = 0
for i in range (0, len(list1)):
        sum += abs(int(list1[i]) - int(list2[i]))
print(sum)

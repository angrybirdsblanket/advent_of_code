with open("data/2024/day1.txt", "r") as db:
    x = db.readlines()
    list1 = []
    list2 = []
    for line in x:
        listtemp = line.split("   ")
        listtemp[1] = listtemp[1][0:-1]
        list1.append(int(listtemp[0]))
        list2.append(int(listtemp[1]))

similarity = 0

for i in range(0, len(list1)):
     similarity += list1[i] * list2.count(list1[i])

print(similarity)

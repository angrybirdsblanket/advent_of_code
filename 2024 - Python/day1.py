with open("data/2024/day1.txt", "r") as data:
    x = data.readlines()
    list1 = []
    list2 = []

    for line in x:
        list1.append(line.split("   ")[0])
        list2.append(line.split("   ")[1])

    list1.sort()
    list2.sort()
    sum = 0
    for i in range (0, len(list1)):
            sum += abs(int(list1[i]) - int(list2[i]))
    print(sum)

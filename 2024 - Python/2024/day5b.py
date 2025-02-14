def is_valid_line(line, before, after):
    for b, a in zip(before, after):
        if b in line and a in line:  
            if line.index(b) > line.index(a):  
                return False  
    return True

def generate_data(line, before, after):
    dataset = []
    dataSet = {}
    for i in range(len(before)):
        if before[i] in line and after[i] in line:
            dataset.append([before[i], after[i]])
    for index, line in enumerate(dataset):
        dataSet[index] = line
    return dataSet

def is_invalid(data, before, after, output):
    count = 0
    for line in data:
        invalid = False
        for b, a in zip(before, after):
            if b in line and a in line:  
                if line.index(b) > line.index(a):  
                    invalid = True
                    break
        if invalid:
            output.append(line)
    return count

def sorter(line, dataSet, sortedlist):
    
    if len(line) == 1:
        sortedlist.append(line[0])
        return sortedlist

    bCount = {}
    aCount = {}

    
    for item in line:
        bCount[item] = 0
        aCount[item] = 0

    
    for pair in dataSet.values():  
        b, a = pair
        bCount[b] += 1
        aCount[a] += 1

    
    in0 = None
    inLast = None

    for index, item in enumerate(line):
        if aCount[item] == 0:  
            in0 = item
            line.pop(index)  
            break

    for index, item in enumerate(line):
        if bCount[item] == 0:  
            inLast = item
            line.pop(index)  
            break

    
    indexToRemove = []
    for index, pair in dataSet.items():  
        if pair[0] == in0 or pair[1] == inLast:
            indexToRemove.append(index)

    for i in indexToRemove:
        dataSet.pop(i)

    
    sortedlist = sorter(line, dataSet, sortedlist)
    sortedlist.insert(0, in0)  
    sortedlist.append(inLast)  

    return sortedlist

def main():
    rules = []
    data = []

    with open("../data/day5.txt") as db:
        lines = db.readlines()
        for line in lines:
            if "|" in line:
                rules.append(line.strip())
            elif "," in line:
                data.append(line.strip())

    before = []
    after = []

    for rule in rules:
        b, a = map(int, rule.split("|"))
        before.append(b)
        after.append(a)


    data = [[int(num) for num in line.split(",")] for line in data]



    invalid_lines = []
    is_invalid(data,before, after, invalid_lines)

    for index, line in enumerate(invalid_lines):
        dataset = generate_data(line, before, after)
        invalid_lines[index] = sorter(line, dataset, [])
    
    sum = 0

    for i in range (len(invalid_lines)):
        sum += invalid_lines[i][len(invalid_lines[i]) // 2]

    print(sum)

if __name__ == "__main__":
    main()

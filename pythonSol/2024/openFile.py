def openFile(data, file):
    with open(file, "r") as db:
        x = db.readlines()
        for line in x:
            data.append(line)

    for i in range(len(data)):
        data[i] = data[i][0:-1]

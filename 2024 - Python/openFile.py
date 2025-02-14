import sys

data = []

with open(sys.argv[1], "r") as db:
    x = db.readlines()

for line in x:
    stripped_line = line.strip()
    if stripped_line:  
        data.append(stripped_line)

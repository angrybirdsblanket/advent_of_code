rules = []
data = []

# couldnt implement openFile here and part 2
with open("../../data/day5.txt") as db:
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

valid_lines = []


def is_valid_line(line, before, after):
    for b, a in zip(before, after):
        if b in line and a in line:  
            if line.index(b) > line.index(a):  
                return False  
    return True



for line in data:
    if is_valid_line(line, before, after):
        valid_lines.append(line)

sum = 0
for line in valid_lines:
    sum += line[len(line)//2 ] 

print(sum)

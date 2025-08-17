import re
from openFile import data

def cramers_rule(a, b, sol):
    a = (int(a[0][0]), int(a[0][1]))
    b = (int(b[0][0]), int(b[0][1]))
    sol = (int(sol[0][0]) + 1*10**13, int(sol[0][1]) + 1*10**13)

    det = a[0] * b[1] - a[1] * b[0]
    if det == 0: 
        return None, None

    a_val = (sol[0] * b[1] - sol[1] * b[0]) / det
    b_val = (a[0] * sol[1] - a[1] * sol[0]) / det

    if a_val == int(a_val) and b_val == int(b_val):
        return int(a_val), int(b_val)
    else:
        return None, None

a_group = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
a_values = []

b_group = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
b_values = []

c_group = re.compile(r"Prize: X=(\d+), Y=(\d+)")
prize_values = []

for line in data:
    if a_group.findall(line):
        a_values.append(a_group.findall(line))
    if b_group.findall(line):
        b_values.append(b_group.findall(line))
    if c_group.findall(line):
        prize_values.append(c_group.findall(line))


sum = 0
for a, b, sol in zip(a_values, b_values, prize_values):
    a_presses, b_presses = cramers_rule(a, b, sol)
    
    if a_presses is None or b_presses is None:
        continue
    sum += a_presses * 3 + b_presses

print(sum)
print(1 * 10**13)


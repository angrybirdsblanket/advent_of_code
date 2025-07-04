from openFile import *

antinodes = set()

grid = []

for line in data:
    if line.strip() == "": continue
    grid.append(line.strip())

rows = len(grid)
cols = len(grid[0])

nodes = {}

for i in range(rows):
    for j in range(cols):
        if grid[i][j] != ".":
            if grid[i][j] in nodes:
                nodes[grid[i][j]].append((i,j))
            else:
                nodes[grid[i][j]] = [(i,j)]

def antinode(pr1, pr2):
    x1, y1 = pr1
    x2, y2 = pr2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    antinodes.add((x2,y2))
    while newx >= 0 and newx < rows and newy >= 0 and newy < cols:
        antinodes.add((newx,newy))
        newx += (x2 - x1)
        newy += (y2 - y1)

for k in nodes:
    node_list = nodes[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            node1 = node_list[i]
            node2 = node_list[j]
            antinode(node1, node2)
            antinode(node2, node1)

print(len(antinodes))

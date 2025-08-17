import numpy as np
from external_funcs import move
from openFile import data

UP    = np.array([-1,  0])
DOWN  = np.array([ 1,  0])
LEFT  = np.array([ 0, -1])
RIGHT = np.array([ 0,  1])
DIRECTIONS = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}

lines = [line for line in data]

grid_lines = []
move_lines = []
in_moves = False

for line in data:
    if not in_moves and line.startswith("#"):
        grid_lines.append(line)
    else:
        in_moves = True
        move_lines.append(line)

# Collapse into one string
moves = "".join(move_lines)

warehouse_map = np.array([list(row) for row in grid_lines], dtype="<U1")

robot_pos = np.argwhere(warehouse_map == "@")[0]

for char in moves:
    direction = DIRECTIONS[char]
    robot_pos = move(robot_pos, direction, warehouse_map)

row, col = np.where(warehouse_map == "O")

sum = 0
for x, y in zip (row, col):
    sum += y + 100*x

print(sum)

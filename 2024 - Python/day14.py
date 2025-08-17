from openFile import data
import re

WIDTH = 101
HEIGHT = 103

bot_right = 0
top_right = 0
bot_left = 0
top_left = 0

line_pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
for line in data:
    x, y, dx, dy = line_pattern.findall(line)[0]

    x = ((int(x) + int(dx) * 100) % WIDTH)
    y = ((int(y) + int(dy) * 100) % HEIGHT)

    if x > WIDTH // 2:
        if y > HEIGHT // 2:
            bot_right += 1
        elif y < HEIGHT // 2:
            top_right += 1
    elif x < WIDTH // 2:
        if y > HEIGHT // 2:
            bot_left += 1
        elif y < HEIGHT // 2:
            top_left += 1

print(bot_left*bot_right*top_right*top_left)

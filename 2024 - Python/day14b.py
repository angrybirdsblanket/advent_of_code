from openFile import data
import re
from math import gcd

WIDTH, HEIGHT = 101, 103

line_pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
robots = []
for line in data:
    x0, y0, dx, dy = map(int, line_pattern.findall(line)[0])
    robots.append((x0, y0, dx, dy))

def pos_at_t(x0, y0, dx, dy, t):
    return ((x0 + dx * t) % WIDTH, (y0 + dy * t) % HEIGHT)

def lcm(a, b): 
    return a * b // gcd(a, b)
PERIOD = lcm(WIDTH, HEIGHT)

def circular_span(values, circumference):
    vals = sorted(values)
    if not vals:
        return 0, 0
    gaps = []
    for i in range(len(vals) - 1):
        gaps.append(vals[i+1] - vals[i])
    gaps.append(vals[0] + circumference - vals[-1])
    gi = max(range(len(gaps)), key=lambda i: gaps[i])
    max_gap = gaps[gi]
    span = circumference - max_gap
    seam_at = vals[(gi + 1) % len(vals)]
    return span, seam_at

NEI8 = [(-1,-1),(0,-1),(1,-1),
        (-1, 0),        (1, 0),
        (-1, 1),(0, 1),(1, 1)]

def largest_component_size(pts):
    s = set(pts)
    seen = set()
    best = 0
    for p in s:
        if p in seen: 
            continue
        stack = [p]
        seen.add(p)
        size = 0
        while stack:
            x, y = stack.pop()
            size += 1
            for dx, dy in NEI8:
                q = ((x+dx) % WIDTH, (y+dy) % HEIGHT)
                if q in s and q not in seen:
                    seen.add(q)
                    stack.append(q)
        if size > best:
            best = size
    return best

def unwrap_positions(positions):
    xs = [x for x, _ in positions]
    ys = [y for _, y in positions]
    spanx, seamx = circular_span(xs, WIDTH)
    spany, seamy = circular_span(ys, HEIGHT)
    unwrapped = [((x - seamx) % WIDTH, (y - seamy) % HEIGHT) for x, y in positions]
    return unwrapped, (spanx + 1) * (spany + 1)

def render(positions):
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for (x, y) in positions:
        grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)

best_t = 0
best_comp = -1
best_area = None
best_positions = None

for t in range(PERIOD):
    positions = [pos_at_t(x0, y0, dx, dy, t) for (x0, y0, dx, dy) in robots]
    comp = largest_component_size(positions)
    _, area = unwrap_positions(positions)

    better = False
    if comp > best_comp:
        better = True
    elif comp == best_comp and (best_area is None or area < best_area):
        better = True

    if better:
        best_comp = comp
        best_area = area
        best_t = t
        best_positions = positions

print(best_t)

unwrapped, _ = unwrap_positions(best_positions)
print(render(unwrapped))

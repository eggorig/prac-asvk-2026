from math import *

def scale(a, b, A, B, x):
    return (x - a) / (b - a) * (B - A) + A


w, h, a, b, f = input().split(maxsplit=4)
w, h = int(w), int(h)
a, b = float(a), float(b)
values = []

for i in range(w):
    x = scale(0, w - 1, a, b, i) if w > 1 else a
    values.append(eval(f))

ymin, ymax = min(values), max(values)

screen = [[' '] * w for i in range(h)]
rows = []

for y in values:
    if ymin == ymax:
        row = h // 2
    else:
        row = round(scale(ymin, ymax, h - 1, 0, y))
    rows.append(row)

for i in range(w):
    screen[rows[i]][i] = '*'
    if i > 0:
        prev = rows[i - 1]
        cur = rows[i]
        for row in range(min(prev, cur) + 1, max(prev, cur)):
            screen[row][i - 1] = '*'

print('\n'.join(''.join(line) for line in screen))

from math import sin

def scale(a, b, A, B, x):
	return (x - a) / (b - a) * (B - A) + A

a, b, w, h = eval(input())
screen = [['.'] * w for i in range(h)]

for i in range(w):
	x = scale(0, w - 1, a, b, i)
	y = sin(x)
	s = int(scale(-1, 1, 0, h - 1, y))
	screen[int(s)][i] = '*'

print('\n'.join(''.join(k) for k in screen))

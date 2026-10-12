from math import sin

def scale(a, b, A, B, x):
	return (x - a) / (b - a) * (B - A) + A

a, b, w, h = eval(input())
for i in range(h):
	x = scale(0, h - 1, a, b, i)
	y = sin(x)
	s = int(scale(-1, 1, 0, w - 1, y))
	print(f'{" " * s}*')

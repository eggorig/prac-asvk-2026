from timeit import Timer

def f1(s):
	d = {}
	for i in s:
		d[i] = d.get(i, 0) + 1
	print(d)
	
def f2(s):
	count = Counter(s)
	print(count)
	
s = input().split()
tC = Timer('f2(s)', globals=globals())
tD = Timer('f1(s)', globals=globals())
print('Counter:', tC.autorange())
print('Dict:'tD.autorange)

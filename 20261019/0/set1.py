import string
from timeit import Timer
gls = set('eioua')
sgl = set(string.ascii_lowercase) - gls

def check(s):
	return len(s & gls), len(s & sgl)

s = set(input())
t = Timer('check(s)', globals=globals())
print(t.autorange())

from string import ascii_letters
class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

class Slotter:
	__slots__ = tuple(ascii_letters)
	
	def __init__(self):
		for attr in ascii_letters:
			setattr(self, attr, attr)
			
t = Trad()
s = Slotter()

import sys
print(f"Trad: {sys.getsizeof(Trad)} t: {sys.getsizeof(t)}")
print(f"Slotter: {sys.getsizeof(Slotter)} s: {sys.getsizeof(s)}")

from pympler.asizeof import asizeof

t_lst = [Trad() for _ in range(1000)]
s_lst = [Slotter() for _ in range(1000)]

print(f"1000 Trad: {asizeof(t_lst)}")
print(f"1000 Slotter: {asizeof(s_lst)}")

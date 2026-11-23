class Counter:
	def __init__(self):
		self.n = 0
	
	def __get__(self, obj, cls):
		return self.n
	
	def __set__(self, obj, num):
		self.n = num

class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1

c = C()
print(c.counter)
d = C()
print(d.counter)
del c
print(d.counter)

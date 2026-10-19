from timeit import Timer

s = input()
t = Timer(s)
num, tim = t.autorange()
print(f"{num} loops / {tim} seconds = {tim / num}")

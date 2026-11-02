from itertools import dropwhile, islice

def genf():
    s = 0
    i = 1
    while True:
        s += 1 / (i * i)
        yield s
        i += 1

g = genf()
print(list(islice(dropwhile(lambda x: x <= 1.6, g), 10)))

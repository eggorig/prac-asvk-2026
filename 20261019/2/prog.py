from math import *

funcs = {}
lines = 0

while True:
    line = input()
    lines += 1
    if line[0] == ':':
        p = line[1:].split()
        funcs[p[0]] = (p[1:-1], p[-1])
    else:
        p = line.split(maxsplit=1)
        func = p[0]
        argum = p[1] if len(p) > 1 else ''
        if func == 'quit':
            print(eval(argum).format(len(funcs) + 1, lines))
            break
        param, body = funcs[func]
        if len(param) == 0:
            val = []
        elif len(param) == 1:
            val = [eval(argum)]
        else:
            val = [eval(i) for i in argum.split()]

        sop = dict(zip(param, val))
        print(eval(body, globals(), sop))

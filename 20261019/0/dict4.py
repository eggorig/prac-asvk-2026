s = input()
a, b = eval(input())
print(eval(s, locals={'x': a, 'y':b}))
print(eval(s, locals={'x': b, 'y':a}))

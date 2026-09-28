a, b = eval(input())
print(*[i for i in range(a,b) if i % 2 != 0 and '3' not in str(i)])

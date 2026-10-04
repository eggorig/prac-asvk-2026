m, n = eval(input())
print([num for num in range(m, n) if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))])

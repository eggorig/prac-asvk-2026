res = 0
while res <= 21:
    num = int(input())
    if num <= 0:
        print(num)
        break
    res += num
else:
    print(res)

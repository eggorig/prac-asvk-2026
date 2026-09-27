n = int(input())
i = n
while i <= n + 2:
    j = n
    while j <= n + 2:
        mul_res = i * j
        mul = mul_res
        summ = 0
        while mul > 0:
            summ += mul % 10
            mul //= 10
        if summ == 6:
            mul_res = ':=)'

        if j == n + 2:
            print(i, '*', j, '=', mul_res)
        else:
            print(i, '*', j, '=', mul_res, end=' ')
        j += 1
    i += 1

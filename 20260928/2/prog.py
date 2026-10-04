lst = list(map(int, input().split(',')))
for i in range(1, len(lst)):
    num = lst[i]
    key = (num ** 2) % 100
    j = i - 1
    while j >= 0 and (lst[j] ** 2) % 100 > key:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = num
print(lst)

def Pareto(*arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][0] <= arr[j][0] and arr[i][1] <= arr[j][1] and (arr[i][0] < arr[j][0] or arr[i][1] < arr[j][1]):
                break
        else:
            res.append(arr[i])
    return tuple(res)

print(Pareto(*eval(input())))

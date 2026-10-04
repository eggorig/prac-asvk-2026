A, B = [], []
A.append(eval(input()))
n = len(A[0])
for _ in range(n - 1):
    A.append(eval(input()))
for _ in range(n):
    B.append(eval(input()))

res = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        res[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
for i in res:
    print(*i, sep=',')

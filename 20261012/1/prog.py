from fractions import Fraction

def compute(x, C):
    res = Fraction(0)
    for c in C:
        res = res * x + c
    return res

def check_s(s, w, A, B):
    val_A = compute(s, A)
    val_B = compute(s, B)
    return val_B != 0 and val_A / val_B == w


inp = [i.strip() for i in input().split(',')]

s, w = Fraction(inp[0]), Fraction(inp[1])
A = [Fraction(inp[i]) for i in range(3, 4 + int(inp[2]))]
B = [Fraction(inp[i]) for i in range(5 + int(inp[2]), len(inp))]

print(check_s(s, w, A, B))

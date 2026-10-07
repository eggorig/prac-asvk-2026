from math import *

def Calc(s, t, u):
    def F(x):
        sx = eval(s)
        ty = eval(t)
        x, y = sx, ty
        return eval(u)
    return F

F = Calc(*eval(input()))
print(F(eval(input())))

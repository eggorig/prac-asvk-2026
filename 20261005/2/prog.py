def sub(obj1, obj2):
    if isinstance(obj1, (list, tuple)):
        res = [i for i in obj1 if i not in obj2]
        if isinstance(obj1, tuple):
            return tuple(res)
        return res
    return obj1 - obj2
print(sub(*eval(input())))

class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception:
        raise InvalidInput
    
    try:
        square = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    except Exception:
        raise BadTriangle
    if square == 0:
        raise BadTriangle
    return square

while True:
    try:
        s = input()
        square = triangleSquare(s)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{square:.2f}")
        break

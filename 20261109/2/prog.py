class Triangle:
    def __init__(self, a, b, c):
        self.k = (tuple(a), tuple(b), tuple(c))

    def vec(self, a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def __abs__(self):
        v = self.vec(self.k[0], self.k[1], self.k[2])
        return abs(v) / 2 if v else 0

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __contains__(self, other):
        if not other:
            return True
        if not self:
            return False

        for p in other.k:
            m1 = self.vec(p, self.k[0], self.k[1])
            m2 = self.vec(p, self.k[1], self.k[2])
            m3 = self.vec(p, self.k[2], self.k[0])
            if not ((m1 >= 0 and m2 >= 0 and m3 >= 0) or (m1 <= 0 and m2 <= 0 and m3 <= 0)):
                return False
        
        return True

    def __and__(self, other):
        if not self or not other:
            return False

        for t1, t2 in ((self, other), (other, self)):
            for i in range(3):
                a = t1.k[i]
                b = t1.k[(i + 1) % 3]
                c = t1.k[(i + 2) % 3]
                side = self.vec(a, b, c)
                values = [self.vec(a, b, p) for p in t2.k]

                if all(v * side < 0 for v in values):
                    return False

        return True


import sys
exec(sys.stdin.read())

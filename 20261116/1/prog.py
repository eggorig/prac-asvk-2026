import collections

class DivStr(collections.UserString):
    def __init__(self, s=''):
        super().__init__(s)
    
    def __floordiv__(self, n):
        k = len(self) // n
        return (self[k * i:k * (i + 1)] for i in range(n))
    
    def __mod__(self, n):
        k = len(self) % n
        return self[len(self) - k:]

import sys
exec(sys.stdin.read())

class Omnibus:
    _count = {}

    def __init__(self):
        object.__setattr__(self, '_atr', set())

    def __setattr__(self, name, val):
        if name not in self._atr:
            self._atr.add(name)
            self.__class__._count[name] = self.__class__._count.get(name, 0) + 1

    def __getattr__(self, name):
        if name in self._atr:
            return self.__class__._count[name]

    def __delattr__(self, name):
        if name in self._atr:
            self._atr.remove(name)
            self.__class__._count[name] -= 1


import sys
exec(sys.stdin.read())

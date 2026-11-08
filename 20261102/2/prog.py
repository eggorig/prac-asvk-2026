from itertools import tee, islice

def slide(seq, n):
    if n <= 0:
        return
    end = object()
    
    while True:
        seq, window = tee(seq)
        yield from islice(window, n)
        if next(seq, end) is end:
            break

import sys
exec(sys.stdin.read())

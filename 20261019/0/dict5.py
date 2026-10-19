from collections import Counter

c1 = Counter(input().split())
c2 = Counter(input().split())

print('yes' if c1 - c2 else 'no')

from itertools import product

print([f'{name}{num}' for name, num in product('abcdefgh', '12345678')])

from itertools import product
print(', '.join(filter(lambda x: x.count('TOR') == 2, map(''.join, product('ORT', repeat=int(input()))))))

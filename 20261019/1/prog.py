s = input()
res = set()
prev = None
for char in s.lower():
    if char.isalpha():
        if prev is not None:
            res.add(prev + char)
        prev = char
    else:
        prev = None

print(len(res))

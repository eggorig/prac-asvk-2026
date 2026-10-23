w = int(input())
res = {}

while line := input():
    line = ''.join(char if char.isalpha() else ' ' for char in line)
    for word in line.lower().split():
        if len(word) == w:
            res[word] = res.get(word, 0) + 1
if res:
    val = max(res.values())
    print(*sorted(i for i in res if res[i] == val))

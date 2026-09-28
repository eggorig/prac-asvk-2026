a = []
while s := input():
	a.append(list(eval(s)))

for i in range(len(a)):
	for j in range(i + 1, len(a)):
		a[i][j], a[j][i] = a[j][i], a[i][j]
for el in a:
	print(el)

while num := input():
	if int(num) % 2 == 0:
		print(num)
	elif int(num) == 13:
		print("thirteen!")
		break
else:
	print("no thirteen")

while True:
	try:
		num = int(input())
		break
	except ValueError:
		print("не число")
print(f"число {num}")

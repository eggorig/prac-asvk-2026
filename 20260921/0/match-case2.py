while num := input():
	match int(num):
		case 1:
			print("один")
		case 2:
			print("два")
		case 3:
			print("три")
		case n if n % 2 == 0:
			print("четное")
		case odd:
			print(odd, "-- это много")


def div(a, b, eps):
	if abs(b) < eps:
		raise ZeroDivisionError
	return a / b


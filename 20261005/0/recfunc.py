def recfunc(x):
	return recfunc(x - 1) if x > 0 else "!!!"

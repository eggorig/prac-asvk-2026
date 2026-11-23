def isint(f):
	def newf(*args):
		if not all(isinstance(i, int) for i in n):
			raise TypeError
		return f(*args)
	return newf

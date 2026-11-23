from functools import wraps

def istype(typ):
	def isint(fun):
		@wraps(fun)
		def newfun(*args):
			if not all(isinstance(i, typ) for i in args):
				raise TypeError
			return fun(*args)
		return newfun
	return isint

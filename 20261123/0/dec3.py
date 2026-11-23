from functools import wraps

class istype:
	def __init__(self, typ):
		self.typ = typ
	
	def __call__(self, fun):
		@wraps(self.typ)
		def newfun(*args):
			if not all(isinstance(i, self.typ) for i in args):
				raise TypeError
			return fun(*args)
		return newfun

class C:
	_age = 0
	@property
	def age(self):
		if self._age == 42:
			print('secret value!')
			return -1
		return self._age
	
	@age.setter
	def age(self, n):
		if n > 128:
			print('too old!')
			raise ValueError('too old!')
		self._age = n

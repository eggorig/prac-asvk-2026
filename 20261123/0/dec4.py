class Sender:
	first = True
	
	@classmethod
	def report(cls):
		if cls.first:
			print("Greetings!")
			cls.first = False
		else:
			print("Get away!")
	
class Asker:
	@staticmethod
	def askall(lst):
		for i in lst:
			i.report()

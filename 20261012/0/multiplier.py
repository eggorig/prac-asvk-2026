from fractions import Fraction
from decimal import Decimal
def multiplier(x, y, Type):
	return Type(x) * Type(y)
	
for a, b, t in (("2.32434", "5.141155", float),
				("2.32434", "5.141155", Decimal),
				("1/6", "2/3", Fraction)):
	print(f"{a} * {b} = {multiplier(a, b, t)}")
		

import decimal
def esum(N, one):
	summ = el = one
	for i in range(1, N):
		el /= i
		summ += el
	return summ
N = int(input())
print(esum(N, 1.))
print(esum(N, decimal.Decimal(1)))
decimal.getcontext().prec=100
print(esum(N, decimal.Decimal(1)))

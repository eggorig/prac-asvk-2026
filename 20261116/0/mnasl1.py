class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

not_ok = 0
for i in (A, B, D):
	try:
		class E(C, i): pass
		print(C.__name__, i.__name__, 'ok')
	except TypeError:
		print(C.__name__, i.__name__, 'not ok')
		not_ok += 1
	try:
		class E(i, C): pass
		print(i.__name__, C.__name__, 'ok')
	except TypeError:
		print(i.__name__, C.__name__, 'not ok')
		not_ok += 1

print(f"исключений: {not_ok}")
print(f"создалось нормально: {6 - not_ok}")

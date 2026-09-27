num = int(input())
a, b, c = list('---')
if num % 50 == 0:
    a = '+'
elif num % 25 == 0:
    b = '+'
if num % 8 == 0:
    c = '+'
print(f"A {a} B {b} C {c}")

import string
gls = set('eioua')
sgl = set(string.ascii_lowercase) - gls
s = set(input())
print(len(s & gls), len(s & sgl))

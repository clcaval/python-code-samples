import re

f = open('bodyguard.dat', 'r')
p = f.read()

pattern = r'(?<=)[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'

a = re.findall(pattern, p)
print(a)

x = ''
for s in a:
	x += s[4]

print(x)


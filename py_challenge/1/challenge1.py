
f = open('text.dat', 'r')
p = f.read()
f.close()
y = ''
url = 'map.html'

# by hand v
for i in p:	
	for j in i:
		if j not in ('.()\''):
			if not ord(j) >= 121:
				x = ord(j) + 2
				y += chr(x)
			else:
				x = ord(j) % 121
				y += chr(97 + x)
	y += ' '

print(y)

#using maketrans
alphabet = 'abcdefghijklmnopqrstuvwxyz'
corrAlphabet = ''

for i in alphabet:
        if not ord(i) >= 121:
                x = ord(i) + 2
                y = chr(x)
        else:
                x = ord(i) % 121
                y = chr(97 + x)
                
        corrAlphabet += y

trans = str.maketrans(alphabet, corrAlphabet)

print(p.translate(trans))
print(url.translate(trans))



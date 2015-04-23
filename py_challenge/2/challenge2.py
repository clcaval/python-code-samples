f = open('rare.dat', 'r')
p = f.read()

# use dictionary
listaChar = []
listaCont = []

dics = {}

for i in p:
	if i not in listaChar:
		listaChar.append(i)
		listaCont.append(1)

	else:
		listaCont[listaChar.index(i)] += 1


# 'e', 'q', 'u', 'a', 'l', 'i', 't', 'y'
print(listaChar)
print(listaCont)

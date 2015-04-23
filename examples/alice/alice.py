"""
    counter of prepositions
    1. replace punctuations from the text
    2. 
"""

import string

texto = open('alice.txt').read().lower()

for c in string.punctuation:
    texto = texto.replace(c, ' ')

palavras = texto.split()

print(palavras)

wc = {}

for p in palavras:
    if p in wc:
        wc[p] += 1
    else:
        wc[p] = 1

def contador(dupla):
    return dupla[1]

duplas = sorted(wc.items(), key=contador, reverse=True)

for dupla in duplas[:10]:
    print (dupla[0], dupla[1])

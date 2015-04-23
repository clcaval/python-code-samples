import urllib3

http = urllib3.PoolManager()

def getData(numb):
        
        r = http.request('GET', 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'%str(numb))        
        return r.data

def getNumber(r):
        text = str(r)
        ind = text.rfind('is ')
        texto = text[ind+3:len(text)]
        texto = texto[:-1]
        return int(texto)

ret = getData(12345)

for i in range(0, 400):
        
        nextNum = getNumber(ret)
        
        if nextNum == 16044:
               nextNum = nextNum / 2
        if nextNum == 82683:
                nextNum = 63579

        ret = getData(nextNum)
        
        print(ret)


"""
#python 2.7 
page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
text = page.read().decode('utf-8')

ind = text.find('is ')
texto = text[ind+3:len(text)]
print(text[ind+3:len(text)])

for i in range(0, 400):
	if int(texto) == 16044:
		texto = 16044 / 2
	if int(texto) == 82682:
		texto = 63579

	page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' %texto)
	text = page.read().decode('utf-8')
	ind = text.find('is ')
	texto = text[ind+3:len(text)]
	print(text)
"""

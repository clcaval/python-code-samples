import urllib2
import datetime

page = urllib2.urlopen('http://beans.itcarlow.ie/prices.html')
text = page.read().decode('utf-8')

print("o preco do cafe em %s e' %s " %(str(datetime.datetime.now()), text[text.find(">$")+1:text.find("</strong")]))

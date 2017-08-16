#!/usr/bin/python

## http://lottery.merseyworld.com/cgi-bin/lottery?days=2&Machine=Z&Ballset=0&order=1&show=1&year=0&display=CSV


import urllib

u = urllib.urlopen('http://lottery.merseyworld.com/cgi-bin/lottery?days=2&Machine=Z&Ballset=0&order=1&show=1&year=0&display=CSV')

data = u.read()
f = open('lotto.csv', 'wb')
f.write(data)
f.close()



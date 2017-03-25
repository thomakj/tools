import urllib

f = urllib.urlopen('http://www.tu.no/lunch/striper/194')
print f.read
f.close()
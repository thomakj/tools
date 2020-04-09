import hashlib
import sys

known_hash = 'a82a2b4d7299e69eef6138b8777c81a5'
timestamp = '1391949706.7103'
your_secret = 'test'

#f = open('/home/thomas/tools/dictionary/english.txt','r')
f = open('/home/thomas/tools/dictionary/passwords.txt','r')
wordlist = f.read()
f.close()

#print wordlist

for word in wordlist.split():
	m = hashlib.md5()
	m.update(word + 'your_secret' + '1391949706.7103')
	if m.hexdigest() == known_hash:
		print word
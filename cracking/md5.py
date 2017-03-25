import hashlib

m = hashlib.md5()

print 'Type message you want to encrypt'
message = raw_input('>>')

m.update(message)
output = m.hexdigest()

print output

with open("/home/thomas/Dropbox/python/cracking/md5_hashes.txt","a") as myfile:
	myfile.write(message+"-"+output)

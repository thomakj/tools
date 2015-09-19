#!/usr/bin/python

import sys

def main(argv):
	numberOfArguments = len(sys.argv)

	if numberOfArguments < 4 :
		print ("You need to add some arguments:\n\t-e: encrypt\tOR\t-d: decrypt\n\t[number of shift]\n\t[text to be changed]")
		sys.exit()
	elif numberOfArguments > 4 :
		print ("You need too remove some arguments:\n\t-e: encrypt\tOR\t-d: decrypt\n\t[number of shift]\n\t[text to be changed]" )
		sys.exit()
	text = list(sys.argv[3])
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	shift = int(sys.argv[2])

	if sys.argv[1] == '-e':
		print (encrypt(text, alphabet, shift))
	if sys.argv[1] == '-d':
		print (decrypt(text, alphabet, shift))
	if sys.argv[1] == '-b':
		bruteforce(text, alphabet)

def encrypt(text, alphabet, shift):
	cipher = ''
	for c in text:
		if c in alphabet:
			cipher += alphabet[(alphabet.index(c)+shift)%(len(alphabet))]
		elif c.lower() in alphabet:
			cipher += alphabet[(alphabet.index(c.lower())-shift)%(len(alphabet))].upper()
		else:
			cipher += c
	return cipher

def decrypt(text, alphabet, shift):
	plaintext = ''
	for c in text:
		if c in alphabet:
			plaintext += alphabet[(alphabet.index(c)-shift)%(len(alphabet))]
		elif c.lower() in alphabet:
			plaintext += alphabet[(alphabet.index(c.lower())-shift)%(len(alphabet))].upper()
		else:
			plaintext += c
	return plaintext

def bruteforce(text, alphabet):
	for x in range(0,26):
		print (decrypt(text, alphabet, x))

if __name__ == "__main__":
	main(sys.argv[1:])

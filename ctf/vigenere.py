# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)
import pyperclip
import sys

#LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def main():
	# This text can be copy/pasted from http://invpy.com/vigenereCipher.py
	myMessage = 'ucoizsbtkxhtadcg'
	myKey = 'adsf'
	translated = []

	for word in sys.stdin:
		decrypted = translateMessage(word, myMessage)
		translated.append(decrypted)

	print(translated)

	print('')

def translateMessage(key, message):
	translated = [] # stores the encrypted/decrypted message string
	keyIndex = 0
	for symbol in message:
   		num = LETTERS.find(symbol)
		num -= LETTERS.find(key[keyIndex]) # subtract if decrypting
		num %= len(LETTERS)
		translated.append(LETTERS[num])
		keyIndex += 1 # move to the next letter in the key
		if keyIndex == len(key):
			keyIndex = 0
       	
	return ''.join(translated)+key
# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()

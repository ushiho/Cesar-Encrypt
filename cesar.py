from tkinter import *
from tkinter import messagebox

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
res = ""

def checkKey(key):
	if key >= 26:
		key = key % 26;
	return key

def encrypt(key, char):
	newIndex = alpha.index(char) + key
	if newIndex >= 26:
		newIndex -= 26
	return alpha[newIndex]

def decrypt(key, char):
	newIndex = alpha.index(char) - key
	if newIndex < 0:
		newIndex += 26
	return alpha[newIndex]

while True:
	try:
		text = input("Text To Cipher: ")
		key = checkKey(int(input("Give the Key: ")))
		print("Your text is: '{}'".format(text))
		break
	except ValueError as e:
		print("The key's format is invalid!")

for char in text.lower():
	if char not in alpha:
		res += char
	else:
		# to decrypt change encrypt by decrypt
		res += encrypt(key, char)


print("your text is {} & the cipher text is '{}'".format(text, res))
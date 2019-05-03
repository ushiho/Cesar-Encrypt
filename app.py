from tkinter import *
from tkinter import messagebox

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
root = Tk()

# check the key's value
def checkKey(key):
	if key >= 26:
		key = key % 26;
	return key

def encrypt(event):
	text, key = getData()[0], getData()[1]
	res = ""
	for char in text.lower():
		if char not in alpha:
			res += char
		else:
			newIndex = alpha.index(char) + key
			if newIndex >= 26:
				newIndex -= 26
			res += alpha[newIndex]
	cipher_entry.insert(0, res)

def decrypt(event):
	text, key = getData()[0], getData()[1]
	res = ""
	for char in text.lower():
		if char not in alpha:
			res += char
		else:
			newIndex = alpha.index(char) - key
			if newIndex < 0:
				newIndex += 26
			res += alpha[newIndex]
	cipher_entry.insert(0, res)

def getData():
	try:
		text = plain_entry.get()
		key = checkKey(int(key_entry.get()))
		return (text, key)
	except ValueError as e:
		msg = Message(root, text="The key's format is invalid!", width=500, justify=LEFT)
		msg.config(fg='red', font=('arial', 12),)
		msg.grid(pady=5, row=3, columnspan=5, )



# View generated
msg = Message(root, text="Cesar Encrypt & Decrypt", width=500)
msg.config(fg='black', font=('times', 16), padx=150, pady=10)
msg.grid(columnspan=6)
plain_lab = Label(root, text="PlainText:")
key_lab = Label(root, text="Key:")
cipher_lab = Label(root, text="Result:")
plain_entry = Entry(root, width=30,)
key_entry = Entry(root, width=30)
cipher_entry = Entry(root, width=30)
plain_lab.grid(row=1)
key_lab.grid(row=2)
cipher_lab.grid(row=4)

plain_entry.grid(row=1, column=1, pady=10)
key_entry.grid(row=2, column=1, pady=10)
cipher_entry.grid(row=4, column=1, padx=50)




encrypt_btn = Button(root, text="Encrypt", bg='white', fg="black", width=15)
encrypt_btn.bind("<Button-1>", encrypt)
encrypt_btn.grid(row=7, column=0, padx=50, pady=10)
decrypt_btn = Button(root, text="Decrypt", bg='white', fg="black", width=15)
decrypt_btn.bind("<Button-1>", decrypt)
decrypt_btn.grid(row=7, column=2, padx=50, pady=10)
quit_btn = Button(root, text="Quit", fg='black', command=root.quit, width=15)
quit_btn.grid(row=7, column=1, padx=10, pady=10)

root.mainloop()
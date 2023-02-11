import random,os,sys
fff = open("files.txt","w",encoding="utf-8")

def zxc(path):
	global txt,png,jpg,jpeg,zipp,rar,py,cs,cpp,h,c,hpp,gif,exe,msi,mp3,mp4,webm,html
	try:
		for f in os.listdir(path):
			file = os.path.join(path, f)
			if(os.path.isfile(file)):
				if(file.endswith(".txt")):
					txt += 1
				elif(file.endswith(".py")):
					py += 1
				elif(file.endswith(".py")):
					cs += 1
				elif(file.endswith(".cpp")):
					cpp += 1
				elif(file.endswith(".hpp")):
					hpp += 1
				elif(file.endswith(".c")):
					c += 1
				elif(file.endswith(".h")):
					h += 1
				elif(file.endswith(".zip")):
					zipp += 1
				elif(file.endswith(".rar")):
					rar += 1
				elif(file.endswith(".png")):
					png += 1
				elif(file.endswith(".jpg")):
					jpg += 1
				elif(file.endswith(".jpeg")):
					jpeg += 1
				elif(file.endswith(".gif")):
					gif += 1
				elif(file.endswith(".exe")):
					exe += 1
				elif(file.endswith(".msi")):
					msi += 1
				elif(file.endswith(".mp3")):
					mp3 += 1
				elif(file.endswith(".mp4")):
					mp4 += 1
				elif(file.endswith(".webm")):
					webm += 1
				elif(file.endswith(".html")):
					html += 1
					
			else: 
				zxc(file)
	except:
		pass

txt = 0
png = 0
jpg = 0
jpeg = 0
zipp = 0
rar = 0
py = 0
cs = 0
cpp = 0
h = 0
c = 0
hpp = 0
gif = 0
exe = 0
msi = 0
mp3 = 0
mp4 = 0
webm = 0
gtml = 0

def main():
	n = input("Path: ")
	if not (os.path.exists(n)):
		print("Path does not exists!")
		sys.exit(1)
	zxc(n)

	fff.write(f"txt: {txt}\n")
	fff.write(f"py: {py}\n")
	fff.write(f"cs: {cs}\n")
	fff.write(f"cpp: {cpp}\n")
	fff.write(f"hpp: {hpp}\n")
	fff.write(f"c: {c}\n")
	fff.write(f"h: {h}\n")
	fff.write(f"rar: {rar}\n")
	fff.write(f"zip: {zipp}\n")
	fff.write(f"png: {png}\n")
	fff.write(f"jpg: {jpg}\n")
	fff.write(f"jpeg: {jpeg}\n")
	fff.write(f"gif: {gif}\n")
	fff.close()

def main1():
	pass

if __name__ == '__main__':
	main()
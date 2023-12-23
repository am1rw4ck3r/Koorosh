# Amir Zare / KooRoSH

import zipfile

# Colors
class colors():
	W  = '\033[0m'  # white
	R  = '\033[31m' # red
	G  = '\033[32m' # green
	O  = '\033[33m' # orange
	B  = '\033[34m' # blue
	P  = '\033[35m' # purple
	C  = '\033[36m' # cyan
	GR = '\033[37m' # gray
	T  = '\033[93m' # tan
	Y = '\033[93m' # yello
	M = '\033[1;35;32m' # magenta

# ZipFile cracker

def zipfile():
	print colors.P + "Files have to be in the same directory - Include .zip or .txt" + colors.W
	zipfilename = raw_input('Zip file : ')
	dictionary = raw_input('Dictionary file : ')
	print (colors.G + "[*]" + "Cracking..." + colors.W)
	password = None
	zip_file = zipfilename
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found : %s' % password
			except:
				pass
	print colors.G + "Password found : " + password + colors.W

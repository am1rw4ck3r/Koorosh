# Amir Zare / KooRoSH

import pythonwhois
import os

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

# def for whois web, i'm using this http://cryto.net/pythonwhois

def whoisweb():
    print( colors.W + ' Example => example.com' + colors.G)
    # enter your website address
    os.system('read -p " WebSite Address : " site && echo && pwhois $site')
    print colors.W

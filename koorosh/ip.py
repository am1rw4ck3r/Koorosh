# Amir Zare / KooRoSH

# import some modules

import socket
import urllib
import urllib2
from urllib import urlopen
import sys

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

# type your ip address and get ip location

def ip():
	ip = raw_input(' IP : ')
	if ip is None or ip == "":
	    sys.exit(' > Enter your ip address : ')
	geoip = urllib.urlopen('http://api.hackertarget.com/geoip/?q=' + ip).read()
	print colors.G + '\n Ip info : '
	print geoip + colors.W + '\n'

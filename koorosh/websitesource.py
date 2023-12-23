# Amir Zare / KooRoSH
import urllib2

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

# def for clone web site source(html)

def websitesource():
    try:
		url = raw_input( colors.G + ' Enter your url Address : ')
		response = urllib2.urlopen(url)
		webContent = response.read()
		websitesource = open('websitesource.html', 'w')
		websitesource.write(webContent)
		print colors.G + ' source saved in /opt/koorosh/websitesource.html' + colors.W
		websitesource.close
    except:
		print colors.R + ' Error, check help or websitesource' + colors.W

# Amir Zare / KooRoSH

# colors

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

# def for helping you can use it with 'help'

def help():
    print ( colors.B + """
  whoisweb > take a whois from webpage |
  insta passgen > generate password list with your arguments |
  website source > clone website source |
  time > you can see time |
  admin page finder > find admin page |
  ip > you can see location with ip address |
  clear > clear your terminal |
  help > print this help manual |
  calendar > you can see date |
  zipfile cracker > crack zipfile password |
  sql dorks > get sql dorks |
  wifi cracker > crack routers password (coming soon) |
  sql > basic check for a sql vulnerability |
  xss > simple check for a xss vulnerability (coming soon) |
  support > developer information for ask Q |
""" + colors.W )

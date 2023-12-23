#!/usr/bin/python2

# Import some modules
import os
import sys
import shutil
import platform

os.system("clear")

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

# Use Gnu/Linux :)
if platform.system() != "Linux":
	print colors.R + "\n" + " You are not using Gnu/Linux Based Os" + colors.W + "\n"
	sys.exit()

# You must run uninstaller as root
if not os.geteuid() == 0:
	print colors.R + "\n" + ' Must be run az Root!' + colors.W + "\n"
	sys.exit()

main = raw_input(' Do you really want to uninstall KooRoSH ? ')
if main == 'y' or 'Y' or 'Yes' or 'yes' or 'yes':
    try:
        shutil.rmtree('/opt/koorosh')
        shutil.rmtree('/opt/icon')
        os.remove('/usr/share/applications/Koorosh.desktop')
        os.remove('/usr/bin/koorosh')
        print colors.G + 'KooRoSH Successfully removed!' + colors.W
    except:
        print colors.R + 'Error : KooRoSH is already uninstalled or not yet installed!' + colors.W
else:
    print colors.O + ' uninstall canceled!' + colors.W
    sys.exit()

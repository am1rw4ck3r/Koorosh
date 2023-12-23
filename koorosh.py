#!/usr/bin/python2

############ Informatin Box ###############
#                                         #
#   Coded by Amir Zare | KooRoSh          #
#   Version Num | 1.1 V                   #
#   Licence GPLv3                         #
#   Use linux based os                    #
#   AmirZare@protonmail.com               #
#   Have Good Time :)                     #
#                                         #
###########################################

################# Python Modules ################

import os
import re
import platform
import subprocess
import urllib
import sys
import time
import socket
import urllib2
import zipfile
import httplib
from time import time, sleep
import time
import calendar

# Append koorosh folder
sys.path.append('koorosh/')

# Import python files in /koorosh folder
from whoisweb import *
from passgen import *
from help import *
from websitesource import *
from calendar import *
from support import *
from ip import *
from zip import *
from sqldorks import *
from adminpagefinder import *
from sql import *

os.system("clear")

# Import modules. 
# You installed them with installer.py

try:
    import pythonwhois
except ImportError as e:
    print '\033[31m' + '''
 Import Error, please run install.py and try again
''' + '\033[0m'
    # Exit from script
    sys.exit()

# If you didn't install(pip, requests, pythonwhois)
# you should install them and after that you can run script

#################### Colors #####################

# Set colors in class.
class colors:
	W  = '\033[0m'  # white
	R  = '\033[31m' # red
	G  = '\033[32m' # green
	O  = '\033[33m' # orange
	B  = '\033[34m' # blue
	P  = '\033[35m' # purple
	C  = '\033[36m' # cyan
	GR = '\033[37m' # gray
	T  = '\033[93m' # tan
	Y = '\033[93m' # yellow
	M = '\033[1;35;32m' # magenta

#################################################

# Koorosh is only for Gnu/linux based operating systems.
if platform.system() != "Linux":
	print (colors.R + "\n You are not using Gnu/Linux Based Os\n" + colors.W)
	# Exit from script
	sys.exit()

# Some tools need root permission
if not os.geteuid() == 0:
	# Exit from script
	sys.exit( colors.R + '\n Must be run az Root!\n' + colors.W)

#################################################

banner ='''
 "========================================"
  (1) WhoISWeb
  (2) Insta PassGen
  (3) WebSite Source
  (4) Time
  (5) Admin Page Finder
  (6) Ip
  (7) Clear
  (8) Help
  (9) Calendar
 (10) ZipFile Cracker
 (11) Sql Dorks
 (12) Wifi cracker
 (13) Sql
 (14) Xss
 (15) Support
 
 (99) Exit
          < Type Num To Use Tools >
 "========================================"
'''
print colors.C + banner + colors.W

while True:
    # Get number for start one of the tools
    main = raw_input(' > select option : ')
    if main == "1":
        whoisweb() # /koorosh/whoisweb.py
    elif main == "2":
        print colors.G
	name = raw_input(' > Enter your arg : ') # /koorosh/passgen.py
        Generator(name).ai()
        print '[!] Saved in /opt/koorosh/password.lst'
	print colors.W
    elif main == "3":
        print colors.G
	websitesource() # /koorosh/websitesource.py
	print colors.W
    elif main == "4":
	if __name__ == "__main__":
	    print "\n" + colors.G + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + colors.W + "\n"
	else:
	    print colors.R + ' Error please try again or check help/support!' + colors.W
    elif main == "5": # [!] I didn't write admin page finder
	print colors.G
	adminpagefinder(var1, var2) # /koorosh/adminpagefinder.py
	print colors.W
    elif main == "6":
    	ip() # /koorosh/ip.py
    elif main == "7":
	os.system('clear') # clear terminal
	print colors.C + banner + colors.W
    elif main == "8":
    	help() # /koorosh/help.py
    elif main == "9":
        if __name__ == "__main__":
	    print colors.G
	    os.system("cal")
	    print colors.W
	else:
	    print colors.R + ' Error please try again or check help/support!' + colors.W
    elif main == "10":
    	print colors.G
	zipfile() # /koorosh/zip.py
	print colors.W
    elif main == "11":
    	sqldorks() # /koorosh/sqldorks.py
    elif main == "12":
    	# mainwifi()
	print colors.R + "\n coming soon!\n" + colors.W
    elif main == "13":
	print colors.G
    	sql() # /koorosh/sql.py
	print colors.W
    elif main == "14":
	# xss()
	print colors.R + "\n coming soon!\n" + colors.W
    elif main == "15":
    	support() # /koorosh/support.py
    elif main == "99":
    	print colors.R
	# Print time of exit
	os.system('echo " Session Exited in : $(date +%H:%M)"')
	print colors.W
    	# exit from script
	exit()
    else:
        # Error for wrong number
	print colors.R + "[!] Enter a num from 1 to 14 or Enter 99 to exit!" + colors.W
        continue

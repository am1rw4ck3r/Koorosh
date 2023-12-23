#!/usr/bin/python2

# Import modules
import os, sys, time, platform
from time import sleep

os.system("clear")

# Colors
W  = '\033[0m'  # white
R  = '\033[31m' # red
G  = '\033[32m' # green

# Use Gnu/Linux :)
if platform.system() != "Linux":
	print R + "\n" + " You are not using Gnu/Linux Based Os" + W + "\n"
	sys.exit()

# You must run installer as root for install modules
if not os.geteuid() == 0:
	print R + "\n" + ' Must be run as Root!' + W + "\n"
	sys.exit()

header = G + '''

 < KooRoSH Installer >

                 ^__^
    _____________(oo)
 <<|            /(__)
   |            |
    ||==========||
    ||          ||
    ||          ||
'''
print header

print W + "\n" + '''
 Select your package Manager :
 1. apt or apt-get ( Debian, Ubuntu )
 2. pacman ( Arch, Manjaro )
 3. yum ( Fedora 21, CentOS, RHEL )
 4. dnf ( Fedora 22+ )
 5. zipper ( openSUSE )
 6. Exit installing
 ''' + '\n'

# Type num for start or stop install
main = raw_input(' Type Num : ')

# For apt/apt-get package manager
if main == "1":
	print G + "[+] Loding..."
	time.sleep(2)
	if __name__ == "__main__":
		os.system('apt-get update')
	else:
		pass
	os.system('apt install python-pip')
	os.system('apt install python-socks')
	os.system('apt install python-mechanize')
	os.system('pip2 install pythonwhois')
	os.system('pip2 install requests')
	os.system('pip2 install requests[security]')
	os.system('sudo cp -R koorosh/ /opt/ && sudo cp koorosh.py /opt/koorosh && sudo cp -R icon/ /opt/ \
	    && sudo cp Koorosh.desktop /usr/share/applications && sudo cp koorosh.sh /opt/koorosh && sudo cp koorosh.sh /usr/bin/koorosh && sudo chmod +x /usr/bin/koorosh')
	if __name__ == "__main__":
		import pip
		pip.main(["install", "pythonwhois", "requests"])
		os.system('clear')
	else:
		pass
	print '\033[93m' + " installing finished type 'koorosh' in terminal:)" + W
	sys.exit()

# For pacman package manager
elif main == "2":
	print G + "[+] Loding..."
	time.sleep(2)
	if __name__ == "__main__":
		os.system('pacman -Syy')
	else:
		pass
	os.system('pacman -S python2-pip')
	os.system('pacman -S python2-pysocks')
	os.system('pacman -S python2-mechanize')
	os.system('pip2 install pythonwhois')
	os.system('pip2 install requests')
	os.system('pip2 install requests[security]')
	os.system('sudo cp -R koorosh/ /opt/ && sudo cp koorosh.py /opt/koorosh && sudo cp -R icon/ /opt/ \
	    && sudo cp Koorosh.desktop /usr/share/applications && sudo cp koorosh.sh /opt/koorosh && sudo cp koorosh.sh /usr/bin/koorosh && sudo chmod +x /usr/bin/koorosh')
	if __name__ == "__main__":
		import pip
		pip.main(["install", "pythonwhois", "requests"])
		os.system('clear')
	else:
		pass
	print '\033[93m' + " installing finished type 'koorosh' in terminal:)" + W
	sys.exit()

# For yum package manager
elif main == "3":
	print G + "[+] Loding..."
	time.sleep(2)
	if __name__ == "__main__":
		os.system("yum -y update")
	else:
		pass
	os.system('yum install python-pip')
	os.system('pip2 install pythonwhois')
	os.system('pip2 install requests')
	os.system('pip2 install requests[security]')
	os.system('sudo cp -R koorosh/ /opt/ && sudo cp koorosh.py /opt/koorosh && sudo cp -R icon/ /opt/ \
	    && sudo cp Koorosh.desktop /usr/share/applications && sudo cp koroosh.sh /opt/koorosh && sudo cp koorosh.sh /usr/bin/koorosh && sudo chmod +x /usr/bin/koorosh')
	if __name__ == "__main__":
		import pip
		pip.main(["install", "pythonwhois", "requests"])
		os.system('clear')
	else:
		pass
	print '\033[93m' + " installing finished type 'koorosh' in terminal:)" + W

# For dnf package manager
elif main == "4":
	print G + "[+] Loding..."
	time.sleep(2)
	if __name__ == "__main__":
		os.system("dnf -y update")
	else:
		pass
	os.system('dnf install python-pip')
	os.system('pip2 install requests')
	os.system('pip2 install pythonwhois')
	os.system('pip2 install requests[security]')
	os.system('sudo cp -R koorosh/ /opt/ && sudo cp koorosh.py /opt/koorosh && sudo cp -R icon/ /opt/ \
	    && sudo cp Koorosh.desktop /usr/share/applications && sudo cp koorosh.sh /opt/koorosh && sudo cp koorosh.sh /usr/bin/koorosh && sudo chmod +x /usr/bin/koorosh')
	if __name__ == "__main__":
		import pip
		pip.main(["install", "pythonwhois", "requests"])
		os.system('clear')
	else:
		pass
	print '\033[93m' + " installing finished type 'koorosh' in terminal:)" + W

# For zypper package manager
elif main == "5":
	print G + "[+] Loding..."
	time.sleep(2)
	os.system('zypper install python-pip')
	os.system('pip2 install requests')
	os.system('pip2 install pythonwhois')
	os.system('pip2 install requests[security]')
	os.system('sudo cp -R koorosh/ /opt/ && sudo cp koorosh.py /opt/koorosh && sudo cp -R icon/ /opt/ \
	    && sudo cp Koorosh.desktop /usr/share/applications && sudo cp koorosh.sh /opt/koorosh && sudo cp koorosh.sh /usr/bin/koorosh && sudo chmod +x /usr/bin/koorosh')
	if __name__ == "__main__":
		import pip
		pip.main(["install", "pythonwhois", "requests"])
		os.system('clear')
	else:
		pass
	print '\033[93m' + " installing finished type 'koorosh' in terminal:)" + W

elif main == "6": 
	print '\033[35m' + ' Good bye!' + W
	time.sleep(0.5)
	sys.exit()
else:
	print R + " ops, installing faild!" + W

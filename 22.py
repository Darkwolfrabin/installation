import os
import datetime
import sys
import time


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

#___________MY CLOLOURS______#


black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"
HBF ='{ HBF }'

#__________MY LOGO__________#


logo = """'\033[1;92m########:::::'###::::'########::'####:'##::: ##:
\033[1;91m ##.... ##:::'## ##::: ##.... ##:. ##:: ###:: ##:
\033[1;94m ##:::: ##::'##:. ##:: ##:::: ##:: ##:: ####: ##:
\033[1;93m ########::'##:::. ##: ########::: ##:: ## ## ##:
 \033[1;91m########::'##:::. ##: ########::: ##:: ## ## ##:
\033[1;92m ##::. ##:: ##.... ##: ##:::: ##:: ##:: ##:. ###:
\033[1;93m ##:::. ##: ##:::: ##: ########::'####: ##::. ##:
\033[1;91m..:::::..::..:::::..::........:::....::..::::..::
♦♦♦\033[1;96m=================☠️😈☠️==================\♦️♦️♦️
"""

#_______________MAIN MENU _____________#

os.system('clear')

print(logo)
print("")
print("♦♦♦\033[1;91m==========☠️MAIN MENU☠️=============♦♦♦")
print("\033[1;93m [1] FOLLOW MY GITHUB ACCOUNT😎   ");time.sleep(3)
print("\033[1;94m [2] MY FACEBOOK I'D ☠️ ");time.sleep(1)
print("\033[1;96m [3] EXIT😈 ");time.sleep(1)
print("\033[1;96m [*type any number*] BASIC TERMUX INSTALLATION ");time.sleep(1)
print("♦♦♦=======DARK-WOLF======♦♦♦")
print("")
rabin = input (" \033[1;92mCHOOSE:: ")
if rabin in ["1","01"]:
         os.system("xdg-open https://github.com/Darkwolfrabin ")
         exit()
elif rabin in["2","02"]:
	os.system("xdg-open https://www.facebook.com/master.mafia22 ")
	exit()
	
if rabin in ["3","03"]:
            exit()
if rabin in ["*","**"]:
	     print("\033[1;96m                 ♦️INSTALLATION IS STARTED ♦️ ")
os.system("clear")
print("")
print(logo)
os.system("apt  upgrade -y")
print()
os.system("pkg install git -y")
print()
os.system("apt apt-get update -y")
print()
os.system("pkg update && pkg upgrade -y")
print()
os.system("apt upgrade && apt install -y")
print()
os.system("apt  install python2 -y")
print()
os.system("apt install ruby -y && gem install lolcat -y")
print()
os.system("apt-get install python -y ")
print()
os.system("pkg install git -y")
print()
os.system("pkg install nano -y")
print()
os.system("apt install python3 ")
print()
os.system("apt install curl ")
print()
os.system("pkg install python2 ")
print()
os.system("pkg install python -y  ")
print()
print(logo)
print("                  \33[0;91mTHANKS FOR USING DARK WOLF TOOL ")
print()
print("                  \33[0;93mSEE YOU SOON WITH NEW TOOL")
print()
print("                \33[0;96m THIS TOOL IS ONLY MADE FOR BEGINNERS  ")
print()
print("                  \33[0;94m*******DARK WOLF HACKS**************")
print("")



    















print("                  \33[0;93m⚠️INSTALLATION IS FINISHED⚠️ ")
print("")       



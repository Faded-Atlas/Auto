import os
import time
from sleep import time
import sys

if os.geteuid() != 0:
    exit("Error: Insufficient permissions. Try running as root.")

a = input("This will clone Linux-Updater to your machine and run it. Are you sure you want to continue?")
if "yes" "y" in a:
    while true:
        print("Lets get started")
        os.system("curl https://https://raw.githubusercontent.com/Faded-Atlas/Linux-Updater/master/Updater.py | python3")
        sleep(2)
        os.system(cd ./Linux-Updater")
        sleep(2)
        os.system(sudo python3 Updater.py)
else:
    exit("Well this is embarassing...") 

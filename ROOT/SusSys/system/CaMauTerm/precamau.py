import subprocess
from NICENTOSH import dev
import os

os.system("clear")

print ("-+[ Welcome To CaMau On Shell ]+-")
print ("Or ( MauSh ) is a simple python shell.")
print ("By Dv5N")

if dev == 1:
	print ("WARN: In DEVELOPER Mode!")

subprocess.call(["python", "camauprogress.py"])


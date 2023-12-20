import subprocess
from NICENTOSH import dev, LOAD_NORMAL, legacy, legacylegacy, LEGACYTXT, fastboot
import os

if fastboot == 0:
	LOAD_NORMAL()

os.system("clear")

if legacy == 1:
	LEGACYTXT()
if legacylegacy == 1:
	LEGACYTXT()
else:
	print ("----------------------------------------")
	print ("----- [ Welcome To CaMau On Shell ] -----")
	print ("----------------------------------------")
	print ("Or ( MauSh ) is a simple python shell.")
	print ("By Dv5N")

if dev == 1:
	print ("WARN: In DEVELOPER Mode!")

subprocess.call(["python", "camauprogress.py"])


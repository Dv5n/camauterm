###############################################################################################################################
# FREE AND OPEN SOURCE, SHOULD NOT BE SOLD, YOU HAVE BEEN WARNED! ------ MIT LICENSE ------######################################################
#################################################################################################################################
# This can be moded. But if you want to mod this, YOU MUST INCLUDE THE ORIGINAL AUTHOR OF THIS SHELL! EX: (Original author: Dv5N)#
##################################################################################################################################
#
# |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# CHANGELOG!!
# (06-01-2024) -DEV_0.0.1 Initial Release. Merry Christmas, everyone.
# |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# Boring STUFF.
import os
import subprocess

from NICENTOSH import dev, vers

from datetime import date
datey = date.today()

# Starting on an adventure, to coolness
def main():
	while True:
		# HappyCow :-), Muu, Is HappyCat better? Mau. You Can Change If You Want.
		if dev == 1:
			cmd = input("DEV+Happycow :-) ")
		else:
			cmd = input("HappyCow :-) ")

		if cmd == "help":
			# ONLY IF YOU ARE A DEVELOPER.
			if dev == 1:
				print ("Welcome to, the one and only, CAMAU ON SHELL\n")
				print ("--Warning: Developer Mode--")
				print ("Commands:")
				print ("<<-sadq = Sadly, exits the shell.")
				print ("<<-help = Shows this.")
				print ("<<-ds   = Short for 'destroy screen' (clears screen).")
				print ("<<-reload = Reloads the shell")
				print ("Developer Only Commands:")
				print ("<<-ver = Shows current version.")
				print ("Date:Time")
				print ("|-------------|")
				print ("Mau: ", datey)
				print ("|-------------|")
				# Normal Help
			else:
				print ("Welcome to, the one and only, CAMAU ON SHELL\n")
				print ("Commands:")
				print ("<<-sadq = Sadly, exits the shell.")
				print ("<<-help = Shows this.")
				print ("<<-ds   = Short for 'destroy screen' (clears screen).")
				print ("<<-reload = Reloads the shell")
				print ("Date:Time")
				print ("|-------------|")
				print ("Mau: ", datey)
				print ("|-------------|")

		# Sadly, Exits the shell
		if cmd == "sadq":
			break

		if cmd == "reload":
			subprocess.run(["python", "precamau.py"])
			return 0

		if cmd == "ds":
			os.system("clear")

		# WARNING: DEV ONLY STUFF

		# DEV ONLY, Shows version.
		if dev == 1:
			if cmd == "ver":
				print("Version: ", vers)
	
if __name__ == "__main__":
	main()
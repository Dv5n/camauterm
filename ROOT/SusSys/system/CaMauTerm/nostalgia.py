import os
from NICENTOSH import dev, verc
from camau import datey

def nmain():

	while True:
		if dev == 1:
			cmd = input ("DEV+HappyCow :-) ")
		else:
			cmd = input ("HappyCow :-) ")

		if cmd == "help":
			if dev == 1:
				print ("Welcome to CaMau On Shell")
				print ("DEV ONLY COMMANDS:")
				print ("<-ver = Shows the version")
				print ("Commands:")
				print ("<-Help = Shows This")
				print ("<-sadq = Sadly, exits the shell")
				print ("<-ds = Short for 'destroy screen' (clears screen)")
				print ("----------")
				print ("Mau: ", datey)
				print ("----------")
			else:
				print ("Welcome to CaMau On Shell")
				print ("Commands:")
				print ("<-Help = Shows This")
				print ("<-sadq = Sadly, exits the shell")
				print ("<-ds = Short for 'destroy screen' (clears screen)")
				print ("----------")
				print ("Mau: ", datey)
				print ("----------")
		
		if cmd == "sadq":
				break
		if cmd == "ds":
			os.system("clear")
		if dev == 1:
			if cmd == "ver":
				print (verc)
if __name__ == "__main__":
	nmain()

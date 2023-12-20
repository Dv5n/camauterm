# The first version that I writed on my phone. The exact code. (DEV_0.0.1). A bit changed at the top but that's all.
import os
from NICENTOSH import n, n1

def main():

	if n == 0:
		print("Stop Code: 0")
		return 0
	
	if n1 == 1:
		print("Hmm...")
		return 0
	
	else:
		while True:
			# Displays this before command.
			cmd = input("HappyCow :-) ")

			if cmd == "help":
				print ("Welcome to, the one and only, CAMAU ON SHELL")
				print ("Commands:")
				print ("<-sadq = Sadly, exits the shell.")
				print ("<-help = Shows this.")
				print ("<-ds   = Short for 'destroy screen' (clears screen)")

			if cmd == "sadq":
				break

			if cmd == "ds":
				os.system("clear")

if __name__ == "__main__":
	main()
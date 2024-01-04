################################################################################################################################
# FREE AND OPEN SOURCE, SHOULD NOT BE SOLD, YOU HAVE BEEN WARNED! ------ MIT LICENSE ------######################################
##################################################################################################################################
# This can be moded. But if you want to mod this, YOU MUST INCLUDE THE ORIGINAL AUTHOR OF THIS SHELL! EX: (Original author: Dv5N)#
##################################################################################################################################
#
#
#
# |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# CHANGELOG!!!!
# 
# (13-12-2023) -DEV_0.0.1 Initial Release. Merry Christmas, everyone.
# (13-12-2023) -DEV_0.0.2 Added Date and Time To "help". Added DEVELOPER Mode. Added "ver", DEVELOPER ONLY COMMAND.
# (14-12-2023) -DEV_0.0.3 Added Comments To this, And this cool changelog, Added "legacy-ver" A DEV ONLY command, shows previous Versions. 
# (15-12-2023) -DEV_0.0.4 I have a problem, the n,n1,etc, was in every file that required them, that means that if I put here the bit "dev = 1" And in "precamau.py" is set to 0, It will say that im in developer mode but im not. So I put ALL of them in a separate file.
# (15-12-2023) -DEV_0.0.5 Improved the imports mentioned above. But it's still a problem, it does work (No Errors), but the stuff (n,n1,etc) is, i don't know, set to garbage?. I set "dev = 1" but it's not?.
# (16-12-2023) -DEV_0.0.6 FINALLY, DONEEE. Sooooo, the fix was pretty easy. Improved the, nostalgia. Improved Help. A, the nostalgia, is accesed by setting the legacy bit to 1, has the look an fell of the version DEV_0.0.2.
# (17-12-2023) -DEV_0.0.7 Improved the, nostalgia. Again. Improved more stuff.
# (17-12-2023) -DEV_0.0.7_2 Added LOAD_LOOP, LOAD_NORMAL, cool loading screen, LOAD_LOOP just loops the loading screen until the end of time. Restricted user creation, for users that doesn't swant to change a bit. Have you watched "Home Alone"???
# (17-12-2023) -DEV_0.0.8 Added the date to every version in this changelog.
# (17-12-2023) -DEV_0.0.9 Added "fakecrthome" same as "crthome" but it doesn't create the user folder for users that doesn't want to change a bit. Entering the pre-release faze of the development.
# (17-12-2023) -PRE_0.1.0 Improved this changelog. Added "legacylegacy" yup, it's just DEV_0.0.1 and "legacy" is the same, DEV_0.0.2.
# (17-12-2023) -PRE_0.1.1 (Happy Music) change the bit "cmusic" to 1 and enjoy a nice music.
# (17-12-2023) -PRE_0.1.2 Added "fastboot" skips the loading screen. But it will never skip the "LOAD_LOOP".
# (18-12-2023) -PRE_0.1.3 Added "happycats" just changes HappyCow to HappyCat. And because of this, I changed the comment "... Is HappyCat better? ..." to "... Is HappyDog better? ...".
# (19-12-2023) -PRE_0.1.4 Improved the warning at the top, added a notice about moding. Improved the "NICENTOSH" file. And from here, I finaly archive the versions, sorry for the older versions. I think I can still archive the old versions using this changelog. And my memory. Hopefuly these older versions can be recovered.
# (19-12-2023) -PRE_0.1.5 Improved "Help" and this changelog.
# (20-12-2023) -PRE_0.1.6 Improved everything. Getting ready for github. Finally on GitHub! Yey.
# (21-12-2023) -0.1.7 Finally, release! I wanted at 1.0.0 to be release. But, it's OK. Improved More Stuff. Add "nugget-play", Just plays mp3 files, nothing interesting, like all cheap mp3 players (nuggets). Added "reload", Reloads the shell.
# (04-01-2024) -0.1.8 Happy New Year. Added "FANCY_LOAD", and the "FANCY" setting. Deleted "DEV Only Stuff" from help. Finally added the "usr" command, for some reason, I forget to put it in help. Added "Debug" setting, but does nothin'.
#
#
#
#
#
#
#
# |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
#
# Boring STUFF.
import os
import subprocess

from NICENTOSH import n, n1, n2, dev, il, legacy, legacylegacy, cmusic, happycats, vers, verz

from playsound import playsound

from datetime import date
datey = date.today()

# Starting on an adventure, to coolness
def main():

	# No info Here.
	if n == 0:
		print("Stop Code: 0")
		return 0
	
	if n1 == 1:
		print("Hmm...")
		return 0
	if il == 1:
		print ("ilegal.")
		subprocess.run(["python", "exit.py"])
		return 0

	if legacy == 1:
		subprocess.run(["python", "nostalgia.py"])

	if cmusic == 1:
		playsound("quack.mp3")

	if legacylegacy == 1:
		subprocess.run(["python", "nostalgia2.py"])
	
	else:

		while True:
			# HappyCow :-), Muu, or HappyCat :-), Mau, Is HappyDog better? Ham. You Can Change If You Want.
			if n2 == 0:
				if dev == 1:
					if happycats == 1:
						cmd = input("DEV+HappyCat :-) ")
					else:
						cmd = input("DEV+Happycow :-) ")
				else:
					if happycats == 1:
						cmd = input("HappyCat :-) ")
					else:
						cmd = input("HappyCow :-) ")
				# HappyCow Is Now Sad. :-(
			else:
				if dev == 1:
					if happycats == 1:
						cmd = input("NODEV-SadCat :-( ")
					else:
						cmd = input("NODEV-Sadcow :-( ")
				else:
					if happycats == 1:
						cmd = input("SadCat :-( ")
					else:
						cmd = input("SadCow :-( ")

			if cmd == "help":
				if n2 == 0:
				# ONLY IF YOU ARE A DEVELOPER.
					if dev == 1:
						print ("Welcome to, the one and only, CAMAU ON SHELL\n")
						print ("--Warning: Developer Mode--")

						print ("Commands:")
						print ("<<-sadq = Sadly, exits the shell.")
						print ("<<-help = Shows this.")
						print ("<<-ds   = Short for 'destroy screen' (clears screen).")
						print ("<<-usr = Create a new user folder.")
						print ("<<-nugget-play = Plays MP3 files like any nugget. (MP3 Player)")
						print ("<<-reload = Reloads the shell")

						print ("Developer Only Commands:")
						print ("<<-ver = Shows current version.")
						print ("<<-legacy-ver = Shows The Previous Version.")
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
						print ("<<-usr = Create a new user folder.")
						print ("<<-nugget-play = Plays MP3 files like any nugget. (MP3 Player)")
						print ("<<-reload = Reloads the shell")
						print ("Date:Time")
						print ("|-------------|")
						print ("Mau: ", datey)
						print ("|-------------|")
				else:
				# Yup. Ho help for you.
					print ("Sadly, no help for u.")
					print ("Only <<-sadq")
					return 0
			# Sadly, Exits the shell
			if cmd == "sadq":
				break


			if cmd == "usr":
				if n2 == 1:
					subprocess.run(["python", "crthome.py"])
				else:
					subprocess.run(["python", "fakecrthome.py"])

			# Please Play Only Nice Music.
			if cmd == "nugget-play":
				os.chdir("media")
				print ("NOTE: MUST BE WITH .MP3 EXTENSION.")
				print ("EX: Meow.mp3")
				coolsound = input("Enter MP3 Name: ")
				playsound(coolsound)
				os.chdir("..")

			if cmd == "reload":
				subprocess.run(["python", "precamau.py"])
				return 0

			if cmd == "ds":
				if n2 == 0:
					os.system("clear")
			
				else:
				# For users that are too lazy to change a bit.
					spm = 1
					while (spm): 
						spm = spm + 1
						print("Mau :-( :-(")

		# WARNING: DEV ONLY STUFF

			# DEV ONLY, Shows version.
			if dev == 1:
				if cmd == "ver":
					print("Version: ", vers)
			# DEV ONLY, Shows Previous Versions.
			if dev == 1:
				if cmd == "legacy-ver":
					print("Older Versions: ", verz)
if __name__ == "__main__":
	main()
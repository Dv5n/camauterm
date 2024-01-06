import os
import time
###############
# Legal Stuff:
n = 1
n1 = 0
n2 = 0
il = 0
###############
# Settings:
# (1 = TRUE(ON), 0 = FALSE(OFF), ONLY)
###################################################################
dev = 0 # DEVELOPER Mode (Only if you are a Developer).
legacy = 0 # For "DEV_0.0.2" Experience.
legacylegacy = 0 # For "DEV_0.0.1" Experience.
cmusic = 0 # For A Nice Duck Sound At The Startup.
fastboot = 1 # Skips loading screens. But never "LOAD_LOOP".
happycats = 0 # For displaying instead of Happycow, Happycat.
FANCY = 0 # Makes All Loading Stuff, More Fancy.
debug = 0 # Enables some debug stuff. (Does nothing now. Sorry.)
###################################################################
# Versions:
vers = "0.1.8"
verz = "0.1.7, PRE_0.1.6, PRE_0.1.5, PRE_0.1.4, PRE_0.1.3, PRE_0.1.2, PRE_0.1.1, PRE_0.1.0, DEV_0.0.9, DEV_0.0.8, DEV_0.0.7_2, DEV_0.0.7, DEV_0.0.6, DEV_0.0.5, DEV_0.0.4, DEV_0.0.3, DEV_0.0.2, DEV_0.0.1"
verc = "DEV_0.0.2"
#####################################################################################################################################################################
# Stuff:
LOAD1 = "."
LOAD2 = ".."
LOAD3 = "..."

LOADF1 = "|"
LOADF2 = "/"
LOADF3 = "-"
LOADF4 = "\\"

def LOAD_LOOP():
    spm = 2048
    while (spm): 
        spm = spm + 2

        os.system("clear")
        print ("Loading: ", LOAD1)
        time.sleep(0.32)

        os.system("clear")
        print ("Loading: ", LOAD2)
        time.sleep(0.32)

        os.system("clear")
        print ("Loading: ", LOAD3)
        time.sleep(0.32)
def LOAD_NORMAL():
    spm = 16
    while (spm): 
        spm = spm - 8

        os.system("clear")
        print ("Loading: ", LOAD1)
        time.sleep(0.25)

        os.system("clear")
        print ("Loading: ", LOAD2)
        time.sleep(0.25)

        os.system("clear")
        print ("Loading: ", LOAD3)
        time.sleep(0.25)

def LOAD_FANCY():
    spm = 16
    while (spm): 
        spm = spm - 8

        os.system("clear")
        print ("Loading: ", LOADF1)
        time.sleep(0.30)

        os.system("clear")
        print ("Loading: ", LOADF2)
        time.sleep(0.30)

        os.system("clear")
        print ("Loading: ", LOADF3)
        time.sleep(0.30)

        os.system("clear")
        print ("Loading: ", LOADF4)
        time.sleep(0.30)

def LEGACYTXT():
    print ("Welcome To CaMau On Shell")
    print ("Or ( MauSh ) is a simple python shell.")
    print ("By Dv5N")

#####################################################################################################################################################################
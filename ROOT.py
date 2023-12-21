import subprocess
import os

os.chdir("ROOT/SusSys/system/CaMauTerm")

print ("Starting Up...\n\n\n")

subprocess.call(["python", "precamau.py"])

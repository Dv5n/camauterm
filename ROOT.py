import subprocess
import os

print ("Starting Up...\n\n\n")

os.chdir("ROOT/SusSys/system/CaMauTerm")

subprocess.call(["python", "precamau.py"])

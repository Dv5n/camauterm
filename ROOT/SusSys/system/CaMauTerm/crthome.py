import os

os.chdir("..")
os.chdir("..")
os.chdir("..")
os.chdir("Home")

## This creates the user folder
sname = input("Enter a Cool Name:  ")
print("Ok, Created User: " + sname)
os.mkdir(sname)


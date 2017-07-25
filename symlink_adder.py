import os,sys
dirs = ""
sr_file = open("sr.conf","a")
while dirs != "exit":
    dirs = input("Path: ")
    if os.path.isdir(dirs):
        sr_file.write(dirs+"\n")
    elif dirs != "exit":
        print("No such directory exists. Is it a directory?")
sr_file.close();

sr_read = open("sr.conf","r")
symlinks = sr_read.read().split("\n")[4:] #The last element in the list is an empty string because of the \n character
for sym in symlinks:
    if os.path.isdir(sym):
        os.system("ln -s "+sym+" "+os.getcwd())
    else:
        break;
#print(symlinks)

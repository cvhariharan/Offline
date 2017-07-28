import os,sys
dirs = ""
sr_read = open("sr.conf","r")
symlinks = sr_read.read().split("\n")[4:] #The last element in the list is an empty string because of the \n character
sr_read.close()
sr_file = open("sr.conf","a")
already_added = []
while dirs != "exit":
    dirs = input("Path: ")
    if os.path.isdir(dirs):
        if not (dirs in already_added) and not (dirs in symlinks): #Check if the directory was already added
            sr_file.write(dirs+"\n")
            already_added.append(dirs)
        else:
            print("Directory already exists.")
    elif dirs != "exit":
        print("No such directory exists. Is it a directory?")
sr_file.close();

sr_read = open("sr.conf","r")
symlinks = sr_read.read().split("\n")[4:] #The last element in the list is an empty string because of the \n character
for sym in symlinks:
    dir_name = sym.split("/")[(len(sym.split("/"))-1)]
    #print(dir_name)
    if os.path.isdir(sym) and not os.path.islink(dir_name): #Check if it is a dir and whether already a symlink exists
            os.system("ln -s "+sym)
    else:
        break;
#print(symlinks)

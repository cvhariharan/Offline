import os,sys
def sym_remover():
    sr = open("sr.conf","r")
    links = sr.readlines()
    sr.close()
    #print(links)
    i = 4
    while i < len(links):
        link_name = links[i].split(":")[1]
        link_name = link_name.replace("\n","")
        if not os.path.islink(os.getcwd()+"/"+link_name):
            print(link_name)
            links[i] = ""
        i += 1
    #print(links)
    sr = open("sr.conf","w")
    sr.writelines(links)
    sr.close()

dirs = ""
sr_read = open("sr.conf","r")
symlinks = sr_read.read().split("\n")[4:] #The last element in the list is an empty string because of the \n character
sr_read.close()
sym_remover()
sr_file = open("sr.conf","a")
already_added = []
while dirs != "exit":
    dirs = input("Path: ")
    if os.path.isdir(dirs):
        if not (dirs in already_added) and not (dirs in symlinks) and not os.path.islink(dirs): #Check if the directory was already added
            name = input("Name of the link: ")
            os.system("ln -s "+dirs+" "+os.getcwd()+"/"+name)
            sr_file.write(dirs+":"+name+"\n")
            already_added.append(dirs)
        else:
            print("Directory already exists.")
    elif dirs != "exit":
        print("No such directory exists. Is it a directory?")
sr_file.close();

"""sr_read = open("sr.conf","r")
symlinks = sr_read.read().split("\n")[4:] #The last element in the list is an empty string because of the \n character
for sym in symlinks:
    dir_name = sym.split("/")[(len(sym.split("/"))-1)]
    #print(dir_name)
    if os.path.isdir(sym) and not os.path.islink(dir_name): #Check if it is a dir and whether already a symlink exists

    else:
        break;
#print(symlinks)"""

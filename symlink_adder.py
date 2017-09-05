import os,sys,easygui
from easygui import *
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
    try:
        dirs = easygui.diropenbox()
        #dirs = "\""+dirs+"\"" #Add quotes
        if os.path.isdir(dirs):
            if not (dirs in already_added) and not (dirs in symlinks) and not os.path.islink(dirs): #Check if the directory was already added
                name_field = ["name"]
                name_list = multenterbox("Name this Directory. (This won't change the original name of the folder.)","Offline",name_field)
                name = ''.join(name_list)
                name = name.replace(" ","")
                os.system("mklink /D "+os.getcwd()+"\\"+name+" "+"\""+dirs+"\"") #Has to be changed to work with linux
                sr_file.write(dirs+":"+name+"\n")
                already_added.append(dirs)
            else:
                print("Directory already exists.")
        elif dirs != "exit":
            print("No such directory exists. Is it a directory?")
    except TypeError:
        break

sr_file.close();

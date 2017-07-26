import os,hashlib,glob,_thread,xxhash,json
def lister(dir_name): #Lists all the files and folders in the current working directory
    for root, dirs, files in os.walk(dir_name, topdown=False):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for name in files:
            #dir_str = dir_str + os.path.join(root, name)
            f.write("file:"+name)
        for name in dirs:
            #dir_str = dir_str + os.path.join(root, name)
            #last_modified = os.path.getmtime(os.path.join(root, name))
            #f.write(name+":"+str(last_modified)+",")
            #Check if the directory is list and if true, traverse it
            if os.path.islink(name):
                #print(os.readlink(dir_name))
                lister(os.readlink(name)) #Returns the real path of name to lister
            f.write("dir:"+name)
f = open("filelist.txt","w")
lister(os.getcwd())
f.close()

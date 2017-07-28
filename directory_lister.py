#Deprecated version. Now switched to new_lister.py

#Just kept for reference purposes.
import os,hashlib,glob,_thread,xxhash,json
#from datetime import datetime
#The following function does not generate md5 hash. It uses xxhash. The entire file is not hashed. Only 18 chunks of 8k from the middle is hashed.
def md5sum(filename):
    try:
         with open(filename, mode='rb') as f:
           d = xxhash.xxh64()
           i=0;
           mid = int((os.path.getsize(filename))/2)
           f.seek(mid)
           while i < 18:
               buf = f.read(8192)
               if not buf:
                   break
               d.update(buf)
               i+=1
           return str(d.hexdigest()).strip("b").strip("\'")
    except FileNotFoundError:
        blank = ""
        return blank

f = open("files.dat","w")
def file_hash(dir_name):
    f.write(dir_name+":"+md5sum(dir_name)+'\r\n')
def dir_hash(dir_name):
    hashes = ""
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            hashes = hashes+md5sum(os.path.join(root,name))
    hashes = str(xxhash.xxh64(hashes).hexdigest()).strip("b").strip("\'")
    last_modified = os.path.getmtime(dir_name)
    f.write(dir_name+":"+hashes+'\r\n')
def lister(): #Lists all the files and folders in the current working directory
    for root, dirs, files in os.walk(".", topdown=True, followlinks=True): #Follw symlinks. Topdown set to true allows removing hidden dirs by the following code snippet
        #Check and remove hidden directories
        for each_dir in dirs:
            #print(each_dir)
            if each_dir.startswith("."):
                dirs.remove(each_dir)

        for name in files:
            #dir_str = dir_str + os.path.join(root, name)
            _thread.start_new_thread(file_hash,(os.path.join(root,name),))
        for name in dirs:
            #dir_str = dir_str + os.path.join(root, name)
            #last_modified = os.path.getmtime(os.path.join(root, name))
            #f.write(name+":"+str(last_modified)+",")
            #Check if the directory is list and if true, traverse it
            #if os.path.islink(name):
                #print(os.readlink(dir_name))
                #lister(os.readlink(name)) #Returns the real path of name to lister
            dir_hash(os.path.join(root,name))

lister()
f.close()

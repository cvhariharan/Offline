import os,hashlib,checksumdir,glob,_thread,xxhash,json
#from datetime import datetime
#The following function does not generate md5 hash. It uses xxhash. The entire file is not hashed. Only 25 chunks of 8k from the middle is hashed.
def md5sum(filename):
  with open(filename, mode='rb') as f:
    d = xxhash.xxh64()
    i=0;
    mid = int((os.path.getsize(filename))/2)
    f.seek(mid)
    while i < 25:
        buf = f.read(8192) # 128 is smaller than the typical filesystem block
        if not buf:
            break
        d.update(buf)
        i+=1
    return str(d.hexdigest()).strip("b").strip("\'")
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
def lister(dir_name):
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            #dir_str = dir_str + os.path.join(root, name)
            _thread.start_new_thread(file_hash,(os.path.join(root,name),))
        for name in dirs:
            #dir_str = dir_str + os.path.join(root, name)
            #last_modified = os.path.getmtime(os.path.join(root, name))
            #f.write(name+":"+str(last_modified)+",")
            dir_hash(os.path.join(root,name))
    f.close()
lister(os.getcwd())

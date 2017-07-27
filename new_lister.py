import fnmatch
import os,glob
import hashlib,glob,_thread,xxhash,json
#from datetime import datetime
#The following function does not generate md5 hash. It uses xxhash. The entire file is not hashed. Only 18 chunks of 8k from the middle is hashed.
"""def md5sum(filename):
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
    """
formats = [".jpg",".png",".avi",".mp4",".mp3",".mkv",".zip",".rar"]
for dirs in glob.iglob("./**/",recursive=True): #Only directories
    print(dirs)
for extension in formats: #Only the files with give formats
    for filename in glob.iglob("./**/*"+extension,recursive=True):
        #fhash = file_hash(os.path.join(os.getcwd(),filename))
        print(filename)#)":"+str(fhash))

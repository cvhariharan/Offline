#Test to see recursive directory lister
import os,hashlib,checksumdir,glob,_thread,xxhash
def md5sum(filename):
  with open(filename, mode='rb') as f:
    d = xxhash.xxh64()
    while True:
      buf = f.read(8192) # 128 is smaller than the typical filesystem block
      if not buf:
        break
      d.update(buf)
    return str(d.hexdigest()).strip("b").strip("\'")
    dir_str = " "
def dir_hash(file):
    print(checksumdir.dirhash(file))
def file_hash(file):
    print(file)
    print(md5sum(file))

dir_str = " "
def lister(dir_name):
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            #dir_str = dir_str + os.path.join(root, name)
            _thread.start_new_thread(file_hash,(os.path.join(root,name),))
        for name in dirs:
            #dir_str = dir_str + os.path.join(root, name)
            print(os.path.join(root, name))

all_files = []
#dir_name = input("Directory: ")
lister('/run/media/hariharan/OS/Series')
print(dir_str)
#print(all_files)

import hashlib,os,checksumdir

def md5sum(filename):
  with open(filename, mode='rb') as f:
    d = hashlib.md5()
    while True:
      buf = f.read(4096)
      if not buf:
        break
      d.update(buf)
    return d.hexdigest()
dir_list = os.listdir(os.getcwd())
dir_str = ""
for file in dir_list:
    if not os.path.isdir(file):
        print(file+":"+md5sum(file))
        dir_str = dir_str+","+str(file)+":"+md5sum(file)
    else:
        print(file+":"+checksumdir.dirhash(file))
        dir_str = dir_str+","+str(file)+":"+checksumdir.dirhash(file)
print(dir_str)

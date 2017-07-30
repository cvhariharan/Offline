import os,glob
import hashlib,_thread,json
#from datetime import datetime
#The following function does not generate md5 hash. It uses xxhash. The entire file is not hashed. Only 18 chunks of 8k from the middle is hashed.
def md5sum(filename):
    try:
         with open(filename, mode='rb') as f:
           d = hashlib.sha1()
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

def file_hash(dir_name):
    #print(dir_name)
    mtime = os.path.getmtime(dir_name)
    fname = dir_name.split("/")[(len(dir_name.split("/"))-1)]
    hashed = md5sum(dir_name)
    block = {}
    block['name'] = fname
    block['mtime'] = mtime
    block['hash'] = hashed
    block['dir'] = "False"
    test_block[dir_name] = block
    #print(fname+"-->"+str(mtime))
    #f.write(dir_name+":"+hashed+'\r\n')
def dir_hash(dir_name):
    #print(dir_name)
    hashes = ""
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            hashes = hashes+md5sum(os.path.join(root,name))
    hashes = str(hashlib.sha1(hashes.encode('UTF-8')).hexdigest()).strip("b").strip("\'")
    last_modified = os.path.getmtime(dir_name)
    mtime = os.path.getmtime(dir_name)
    fname = dir_name.split("/")[(len(dir_name.split("/"))-2)] #For directories the format is /path/to/dir_name/
    block = {}
    block['name'] = fname
    block['mtime'] = mtime
    block['hash'] = hashes
    block['dir'] = "True"
    test_block[dir_name] = block
    #print(test_block[dir_name])
    #print(fname+"-->"+str(mtime))
    #f.write(dir_name+":"+hashes+'\r\n')

formats = [".jpg",".png",".avi",".mp4",".mp3",".mkv",".zip",".rar"]
test_block = {}
if os.path.isfile("files.json"):
    #print("File Found.")
    fr = open("files.json","r")
    all_files = fr.read()
    test_block = json.loads(all_files)
    fr.close()
    #print(test_block)
    for dirs in glob.iglob("./**/",recursive=True): #Only directories
        try:
            #print(test_block[dirs])
            now_mtime = os.path.getmtime(dirs)
            pre_mtime = test_block[dirs]['mtime']
            if now_mtime != pre_mtime:
                dir_hash(dirs)
        except KeyError:
            dir_hash(dirs)

    for extension in formats: #Only the files with give formats
        for filename in glob.iglob("./**/*"+extension,recursive=True):
            try:
                #print(test_block[filename])
                now_mtime = os.path.getmtime(filename)
                pre_mtime = test_block[filename]['mtime']
                if now_mtime != pre_mtime:
                    file_hash(filename)
            except KeyError:
                file_hash(filename)
    indexed = test_block.keys()
    to_remove = []
    for each_indexed in indexed: #Checks for deleted files and removes them from the index
        if not os.path.exists(each_indexed):
            to_remove.append(each_indexed)
            #print("Each_Indexed: "+each_indexed)

    for each_remove in to_remove:
        #print("Each_Remove: "+each_remove)
        test_block.pop(each_remove,None)


else:
    for dirs in glob.iglob("./**/",recursive=True): #Only directories
        dir_hash(dirs)
    for extension in formats: #Only the files with give formats
        for filename in glob.iglob("./**/*"+extension,recursive=True):
            file_hash(filename)
json_h = json.dumps(test_block,separators=(',',':')) #Remove whitespaces
#print(json_h)
f = open("files.json","w")
#print(master_block)
f.write(str(json_h))
f.close()

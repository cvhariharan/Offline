import os,urllib3
import base64,requests
from Crypto.Cipher import AES
server_conf = open("sr.conf","r")
data = server_conf.readlines()
server_user = data[0].strip('Username:').strip('\n')
server_pass = data[1].strip('Password:').strip('\n')
port = int(data[2].strip('Port:').strip('\n'))
localhost = data[3].strip('Localhost:').strip('\n')
def dns(name):
    http = urllib3.PoolManager()
    r = http.request('POST','http://'+localhost+'dns_server.php',fields={'name':name})
    return r.data
def decodeAnddownload(fname):
    if os.path.exists(os.getcwd()+"/"+fname):
        f = open(fname,"r")
        to_read = f.read()
        IV = 16 * '\x00'

        def decrypt(enc, key):
            decobj = AES.new(key, AES.MODE_CBC, IV)
            data = decobj.decrypt(base64.b64decode(enc))
            return str(data.decode())

        key = to_read[23:55]
        to_read = to_read[0:23]+to_read[55:]
        #print(key)
        to_read.replace(key,"")
        data = decrypt(to_read, key)
        lines = data.split('\r\n')
        name = (lines[0].split(':'))[1].strip()
        location = (lines[1].split(':'))[1].strip()
        #server = (lines[2].split(':'))[1].strip()
        port = (lines[3].split(':'))[1].strip()
        server_user = (lines[4].split(':'))[1].strip()
        server_pass = (lines[5].split(':'))[1].strip()
        md5hash = (lines[6].split(':'))[1].strip()
        servername = (lines[7].split(':'))[1].strip()
        name = urllib.quote(name)
        server = dns(servername)
        print(server)
        download_com = "wget http://"+server_user+":"+server_pass+"@"+server+":"+port+"/"+name
        #print(download_com)
        os.system(download_com)
        #print(name)
        #print(location)
        #print(server+":"+port)
        #print(server_user+":"+server_pass)
        #print(md5hash)
    elif fname != "exit":
        print("No such file found!")
fname = ""
while fname != "exit":
    fname = raw_input("Name of the file (Type exit to exit): ")
    decodeAnddownload(fname)

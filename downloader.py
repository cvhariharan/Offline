import os,urllib,requests
import base64,sys
from Crypto.Cipher import AES
server_conf = open("sr.conf","r")
data = server_conf.readlines()
server_user = data[0].strip('Username:').strip('\n')
server_pass = data[1].strip('Password:').strip('\n')
port = int(data[2].strip('Port:').strip('\n'))
localhost = data[3].strip('Localhost:').strip('\n')
def dns(name):
    #http = urllib3.PoolManager()
    r = requests.post('http://'+localhost+'/dns_server.php',data={'name':name})
    return r.text
def decodeAnddownload(fname):
    if os.path.exists(os.getcwd()+"/"+fname):
        f = open(fname,"r")
        to_read = f.read()
        to_read = to_read[40:] #I can't find from where the initial 40 characters come from.
        #IV = 16 * '\x00'

        def decrypt(enc):
            return base64.b64decode(base64.b64decode(enc))


        #print(key)
        data = decrypt(to_read)
        lines = data.split('\r\n')
        #print(lines)
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
        #print(server)
        download_com = "wget -nH --no-parent -nc -c -r "+name+" http://"+server_user+":"+server_pass+"@"+server+":"+port+location
        #print(download_com)
        os.system(download_com)
        #os.remove("index.html")
        #print(name)
        #print(location)
        #print(server+":"+port)
        #print(server_user+":"+server_pass)
        #print(md5hash)
    elif fname != "exit":
        print("No such file found!")
        sys.exit(0)

fname = sys.argv[1] #raw_input("Name of the file (Type exit to exit): ")
decodeAnddownload(fname)

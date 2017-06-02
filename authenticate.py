import requests, time, threading,_thread,xxhash
import hashlib,checksumdir
import os, sys, socket, json, random, string
server_conf = open("sr.conf","r")
data = server_conf.readlines()
server_user = data[0].strip('Username:').strip('\n')
server_pass = data[1].strip('Password:').strip('\n')
port = int(data[2].strip('Port:').strip('\n'))
localhost = data[3].strip('Localhost:').strip('\n')
status = 0 #Server is Offline
def my_ip():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('192.0.0.2',1027))
    return s.getsockname()[0]

def basichttpserver(port,username,password):
    server_command = "./Server --username "+server_user+" --password "+server_pass+" -p "+str(port)
    output = os.system(server_command)

def downloader():
    com = "python downloader.py"
    os.system(com)

def server_status():
    try:
        r = requests.get("http://"+server_user+":"+server_pass+"@localhost:"+str(port))
        if r.status_code == 200:
            status = 1
    except requests.exceptions.RequestException as e:
        status = 0
    return status
headers = {'content-type': 'application/json'}
if server_status() == 0:
    server_thread = threading.Thread(target=basichttpserver,args=(port,server_user,server_pass,))
    server_thread.setDaemon(True)
    #download_thread.start()

    server_thread.start()
    server_thread.join(15)

auth = 0
attempts = 5
while auth != 1 and attempts != 0:
    username = input("Username: ")
    password = input("Password: ")
    ipaddr = my_ip()
    #print("http://"+localhost+"/auth.php")
    r = requests.post("http://"+localhost+"/auth.php", data = {'username':username, 'passw':password, 'ipaddr':ipaddr})
    if r.text == '1':
        print ("Authentication Successful!")
        auth = 1
        dir_str = " "
        os.system("python3 directory_lister.py")
        file_dat = open("files.dat","r")
        all_files = file_dat.readlines()
        for files in all_files:
            dir_str = dir_str + "," + (files.replace(str(os.getcwd()),""))
        response = requests.post("http://"+localhost+"/direcctorylist.php", data = {'list':dir_str,'username':username,'ipaddr':ipaddr,'location':os.getcwd(),'server_user':server_user,'server_pass':server_pass,'port':port})
        os.remove("files.dat")
        #downloader()
        #print(dir_str)
        downloader()
    elif attempts != 0:
        if attempts != 1:
            print("Authentication Failed! Try Again.")
        attempts-=1
        print("Attemps remaining "+str(attempts))
sys.exit(0)

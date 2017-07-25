import requests, time, threading,_thread,xxhash
import hashlib
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
    server_command = "./Server --username "+server_user+" --password "+server_pass+" -p "+str(port)+" > server.log"
    output = os.system(server_command)

def downloader():
    hv_file = input("Name of the hv file: ")
    com = "python downloader.py "+ hv_file
    os.system(com)

def server_status():
    try:
        r = requests.get("http://"+server_user+":"+server_pass+"@localhost:"+str(port))
        if r.status_code == 200:
            status = 1
    except requests.exceptions.RequestException as e:
        status = 0
    return status

def select_choice():
    while True:
        if auth == 1:
            print("1.Download\n2.Add Directory\n")
            choice = str(input("Enter 1 or 2 and exit to exit: "))
            if choice == "1":
                downloader()
            if choice == "2":
                os.system("python3 symlink_adder.py")
            if choice == "exit":
                break;
            else:
                print("Invalid selection!")
        else:
            sys.exit(0)


headers = {'content-type': 'application/json'}
if server_status() == 0:
    server_thread = threading.Thread(target=basichttpserver,args=(port,server_user,server_pass,))
    server_thread.setDaemon(True)
    server_thread.start()
    server_thread.join(2)
auth = 0
attempts = 5
#Authentication
while auth != 1 and attempts != 0:
    username = input("Username: ")
    password = input("Password: ")
    ipaddr = my_ip()
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
        break;

    elif attempts != 0:
        if attempts != 1:
            print("Authentication Failed! Try Again.")
        attempts-=1
        print("Attemps remaining "+str(attempts))
    break;

select_choice()

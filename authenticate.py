import requests, time, threading,_thread
import hashlib
import os, sys, socket, json, random, string, getpass

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

def check_symlinks():
        sr = open("sr.conf","r")
        links = sr.readlines()
        sr.close()
        #print(links)
        i = 4
        while i < len(links):
            link_name = links[i].split(":")[1]
            link_name = link_name.replace("\n","")
            if not os.path.islink(os.getcwd()+"/"+link_name):
                #print(link_name)
                links[i] = ""
            i += 1
        #print(links)
        sr = open("sr.conf","w")
        sr.writelines(links)
        sr.close()


def select_choice():
    while True:
        if auth == 1:
            print("1.Download\n2.Add Directory\n")
            choice = str(input("Enter 1 or 2 and exit to exit: "))
            if choice == "1":
                downloader()
                continue;
            if choice == "2":
                os.system("python3 symlink_adder.py")
                send_directory()
                continue
            if choice == "exit":
                break;
            else:
                print("Invalid selection!")
        else:
            sys.exit(0)

def send_directory():
    os.system("python3 new_lister.py")
    file_dat = open("files.json","r")
    all_files = file_dat.read()
    dir_block = json.loads(all_files)
    block = {}
    block['username'] = username
    block['ipaddr'] = ipaddr
    block['server_user'] = server_user
    block['server_pass'] = server_pass
    block['port'] = port
    dir_block["me"] = block
    json_dirs = json.dumps(dir_block,separators=(',',':')) #Remove whitespaces
    response = requests.post("http://"+localhost+"/Offline/direcctorylist.php", data = json_dirs)

try:
	server_conf = open("sr.conf","r")
	data = server_conf.readlines()
	server_user = data[0].strip('Username:').strip('\n')
	server_pass = data[1].strip('Password:').strip('\n')
	port = int(data[2].strip('Port:').strip('\n'))
	localhost = data[3].strip('Localhost:').strip('\n')
	server_conf.close()
	status = 0 #Server is Offline

	check_symlinks()

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
		password = getpass.getpass(prompt="Password: ", stream=None)
		ipaddr = my_ip()
		r = requests.post("http://"+localhost+"/auth.php", data = {'username':username, 'passw':password, 'ipaddr':ipaddr})
		if r.text == '1':
			print ("Authentication Successful!")
			notification = requests.get("http://"+localhost+"/notification.php")
			print(notification.text)
			auth = 1
			send_directory()
			break;

		elif attempts != 0:
			if attempts != 1:
				print("Authentication Failed! Try Again.")
			attempts-=1
			print("Attemps remaining "+str(attempts))


	select_choice()
except FileNotFoundError:
	print("Sr.conf file not found. Make sure you download it and place it in the current directory.")

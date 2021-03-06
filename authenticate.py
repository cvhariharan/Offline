import requests, time, threading,_thread
import hashlib
from easygui import *
import easygui
import os, sys, socket, json, random, string, getpass

def my_ip():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(('192.0.0.2',1027))
	return s.getsockname()[0]

def basichttpserver(port,username,password):
	server_command = "./Server "+server_user+" "+server_pass+" "+str(port)+" > server.log\""
	output = os.system(server_command)


def downloader():
	try:
		hv_file = easygui.fileopenbox() #Does not return the full path
		command = "python downloader.py "+ "\""+hv_file+"\""
		os.system(command)
	except TypeError as e:
		return


def server_status():
	try:
		r = requests.get("http://"+server_user+":"+server_pass+"@localhost:"+str(port))
		if r.status_code == 200:
			status = 1
	except requests.exceptions.RequestException as e:
		status = 0
	return status

def check_symlinks():
	no_of_links = len(data)
	i = 4
	while i < no_of_links:
		path_breakdown = data[i].strip("/")
		symlink = path_breakdown[(len(path_breakdown)-1)]
		if not os.path.islink(os.getcwd()+"/"+symlink):
			#print(os.getcwd()+"/"+symlink)
			data[i] = ""
		i += 1
	server_conf = open("sr.conf","w")
	server_conf.writelines(data)


def select_choice():
	while True:
		if auth == 1:
			if server_status() == 1:
				print("1.Download\n2.Add Directory\n")
				#choice = str(input("Enter 1 or 2 and exit to exit: "))
				all_choices = ["Download", "Add Directory","Exit"]
				choice = choicebox("You want to download or add a directory to be shared?","Choose",all_choices)
				if choice == "Download":
					downloader()
					continue;
				if choice == "Add Directory":
					os.system("python3 symlink_adder.py")
					send_directory()
					continue
				if choice == "Exit":
					break;
				else:
					print("Invalid selection!")
			else:
				print("You seem to have exit the client server cmd prompt. Restarting the Server ...")
				start_server()

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
	response = requests.post("http://"+localhost+"/direcctorylist.php", data = json_dirs)

def start_server():
	server_thread = threading.Thread(target=basichttpserver,args=(port,server_user,server_pass,))
	server_thread.setDaemon(True)
	server_thread.start()
	server_thread.join(5)

try:
	server_conf = open("sr.conf","r")
	data = server_conf.readlines()
	server_user = data[0].strip('Username:').strip('\n')
	server_pass = data[1].strip('Password:').strip('\n')
	port = int(data[2].strip('Port:').strip('\n'))
	localhost = data[3].strip('Localhost:').strip('\n')
	server_conf.close()
	status = 0 #Server is Offline
	version = "1.0.0"
	title = "Offline-Authentication"
	msg = "Enter your Username and Password"
	fields = ["Username","Password"]
	check_symlinks()
	try:
		headers = {'content-type': 'application/json'}
		if server_status() == 0:
			start_server()
		auth = 0
		attempts = 5
		#Authentication
		while auth != 1 and attempts != 0:
			username,password = multpasswordbox(msg,title,fields) #GUI
			#password = getpass.getpass(prompt="Password: ", stream=None)
			ipaddr = my_ip()
			r = requests.post("http://"+localhost+"/auth.php", data = {'username':username, 'passw':password, 'ipaddr':ipaddr})
			if r.text == '1':
				print ("Authentication Successful!")
				payload = {'username':username,'version':version}
				notification = requests.get("http://"+localhost+"/notification.php",params = payload)
				message = notification.text.split(":")
				print(message[0])
				stop = 0
				if message[1] == "stop":
					stop = 1

				auth = 1
				if stop == 0:
					send_directory()
				break;

			elif attempts != 0:
				if attempts != 1:
					print("Authentication Failed! Try Again.")
				attempts-=1
				print("Attemps remaining "+str(attempts))
		if stop == 1:
			print("This client software will not work.")
			sys.exit(0)

		select_choice()
	except requests.exceptions.RequestException as e:
		print("Server is not live. Please try again later!")

except FileNotFoundError:
	print("Sr.conf file not found. Make sure to download it and place it in the current directory.")

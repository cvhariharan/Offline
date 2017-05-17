import requests
import os, sys, socket, json
headers = {'content-type': 'application/json'}
username = input("Username: ")
password = input("Password: ")
ipaddr = socket.gethostbyname(socket.gethostname())
r = requests.post('http://localhost/Offline/auth.php', data = {'username':username, 'passw':password, 'ipaddr':ipaddr})
if r.text == '1':
    print ("Authentication Successful!")
    #path = "/var/www/html/"
    dirs = os.listdir(os.curdir)
str_dir = str(dirs)
response = requests.post('http://localhost/Offline/direcctorylist.php', data = {'list':str_dir,'username':username,'ipaddr':ipaddr,'location':os.getcwd()})
print("Response: \n")
print(response.text)
#for file in dirs:
#    print (file)

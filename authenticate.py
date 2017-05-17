import requests
import os, sys, socket
username = input("Username: ")
password = input("Password: ")
ipaddr = socket.gethostbyname(socket.gethostname())
r = requests.post('http://localhost/Offline/auth.php', data = {'username':username, 'passw':password, 'ipaddr':ipaddr})
if r.text == '1':
    print ("Authentication Successful!")
    #path = "/var/www/html/"
    #dirs = os.listdir(path)

#for file in dirs:
    #print (file)

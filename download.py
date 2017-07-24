import os,sys
from pySmartDL import SmartDL

url = str(sys.argv[1]) #The first argument is the name of the python script
#url = input("URL: ")
#print(url)
dest = os.getcwd()

obj = SmartDL(url,dest)
obj.start()

path = obj.get_dest()

import os
from pySmartDL import SmartDL
url = input("URL: ")
dest = os.getcwd()

obj = SmartDL(url,dest)
obj.start()

path = obj.get_dest()


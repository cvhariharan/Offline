#Test to see recursive directory lister
import os
def lister(dir_name):
    os.chdir(dir_name)
    dirs = os.listdir(os.getcwd())
    for file in dirs:
        if not os.path.isdir(file):
            print(file + "Location: "+os.getcwd())
        else:
            lister(file)
all_files = []
dir_name = input("Directory: ")
lister(dir_name)

print(all_files)

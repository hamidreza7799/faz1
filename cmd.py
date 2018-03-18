import socket
from os import listdir
from os.path import isfile, join
mypath = 'C://Users/ASUS/Desktop/Project'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
print(onlyfiles)
from os import walk
f=[]
for(dirpath,dirnames,filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)

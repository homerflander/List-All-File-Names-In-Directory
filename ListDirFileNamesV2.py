import os
import sys
import io

def search(scriptparam,depth):
    dirList = os.listdir("./")
    for filename in dirList:
        x=0
        holder=""
        for x in range (0,depth):
            holder=holder+"\t"
        if(depth>0):
            holder = holder + "->" + filename
        else:
            holder=holder+filename
        #print(depth) #was used for troubleshooting depth of subfiles/folders
        if (filename != scriptparam):
            #print(holder)
            FILEOUT.write(holder + "\n")
            if os.path.isdir(filename):
                #print(filename + " is a folder") #was used from troubleshooting if file was a folder or file
                os.chdir(filename)
                depth=depth+1
                search(scriptparam, depth)
                depth=depth-1
                os.chdir("..")

FILEOUT=io.open("output.txt", "w", encoding='utf-8')
location=input("Enter in the location of the directory you wish to search. \n")
os.chdir(location)

#copen output.txt file to write the list, excluding the python script name
search(location,0)
FILEOUT.close()
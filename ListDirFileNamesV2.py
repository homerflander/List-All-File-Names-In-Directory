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
            print(holder)
            FILEOUT.write(holder + "\n")
            if os.path.isdir(filename):
                #print(filename + " is a folder") #was used from troubleshooting if file was a folder or file
                os.chdir(filename)
                depth=depth+1
                search(scriptparam, depth)
                depth=depth-1
                os.chdir("..")

if len(sys.argv) is not 2:#takes in one argument for output textfile.
    sys.exit("Error, script needs one command-line argument. (output.txt File)")

start=0#start of python script location string
end=len(sys.argv[0])#end of python script location string
directorylist=""  # set up output name directorylist
#print(start) used for troubleshooting
#print(end) used for troubleshooting

#find python script name, not entire location
while(sys.argv[0].find("/",start,end)!=-1):
    #print(sys.argv[0].find("/",start,end))
    start=sys.argv[0].find("/",start,end)+1

pscript=sys.argv[0][start:end]

#copen output.txt file to write the list, excluding the python script name
FILEOUT=io.open(sys.argv[1], "w", encoding='utf-8')
search(pscript,0)
FILEOUT.close()



import os
import sys

def search(scriptparam,depth):
    templist=""
    dirList = os.listdir("./")
    for filename in dirList:
        x=0
        holder=""
        for x in range (0,depth):
            holder=holder+"    "
        if(depth>0):
            holder = holder + "->" + filename
        else:
            holder=holder+filename
        print(holder)
        #print(depth) #was used for troubleshooting depth of subfiles/folders
        if (filename != scriptparam):
            templist = templist + holder + "\n"
            if os.path.isdir(filename):
                #print(filename + " is a folder") #was used from troubleshooting if file was a folder or file
                os.chdir(filename)
                depth=depth+1
                templist=templist+search(scriptparam,depth)
                depth=depth-1
                os.chdir("..")
    return templist

if len(sys.argv) is not 2:#takes in one argument for output textfile.
    sys.exit("Error, script needs one command-line argument. (output.txt File)")

start=0#start of python script location string
end=len(sys.argv[0])#end of python script location string
list=""  # set up output name list
#print(start)
#print(end)

#find python script name
while(sys.argv[0].find("/",start,end)!=-1):
    #print(sys.argv[0].find("/",start,end))
    start=sys.argv[0].find("/",start,end)+1

pscript=sys.argv[0][start:end]
#create file name list excluding python script name
list=search(pscript,0)

print("\n")
print("Now writing the following list of file names to %s" %sys.argv[1])
print(list)

#open output text file and write the file name list. Then close output file.
FILEOUT = open(sys.argv[1], 'w')
FILEOUT.write(list)
FILEOUT.close()

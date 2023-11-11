#File Automation
#input mhanun folder ch naav 
#Accept folder name from user and display all the files and sub folders in it
#SUb folder n chya aatlya files pn display krt
#Kiti vel lagla te pn display karel

from sys import *
import os
import time

def DirectoryTravel(DirName):
    print("We are going to scan the directory : ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        print("Current Directory Name : ",foldername)

        for subname in subfoldername:
            print("Subfolder name is  : ",subname)

        for fname in filename: 
            print(fname)
            print("Filesize is : ",os.path.getsize(fname))

        #We can use this syntax also
        # for fname in filename: 
            #print(fname, " : ",os.path.getsize(foldername+"/"+fname), " bytes")

def main():
    print("----------Automation Script----------")

    print("Automation script Name : ",argv[0])

    if(len(argv) != 2):     
        print("Invalid number of arguments")
        exit()
    if(argv[1] == "-h" or argv[1] == "-H"):       #-h flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):        #-u flah ==g for displaying usage of script
        print("Usage : Name_Of_Script First_Argument")
        print("Example : Demo.py Marvellous")
        exit()
        
    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if  __name__ == "__main__":
    main()
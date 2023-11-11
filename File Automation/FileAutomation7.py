#File search
from sys import *
import os
import time

def DirectoryTravel(DirName,Name):  
    print("We are going to Scan the Directory : ",DirName)

    flag = os.path.isabs(DirName)       #jr dilela path absolute asel tr true 

    if flag == False:
        DirName = os.path.abspath(DirName)      #jr path absolute nasel tr path la absolute path madhe convert kara

    exist = os.path.isdir(DirName)      #path directory cha ahe ki nahi te check krnya sathi

    if exist:        #if exist ==True   
        #       1           2               3
        for foldername, subfoldername, filename in os.walk(DirName):    #3 return values ahet                
            for fname in filename:
                if(fname == Name):
                    print("File is present in directory with name : ",fname)
            
        
    else:
        print("Invalid path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument Second_Argument")
        print("Example : Demo.py Marvellous Demo.txt")
        exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1],argv[2])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name File_Name
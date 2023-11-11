#File search and display the file name of largest size
from sys import *
import os
import time

def DirectoryTravel(DirName):  
    print("We are going to Scan the Directory : ",DirName)
    MaxSize = 0
    MaxSizeFileName = " "

    flag = os.path.isabs(DirName)       #jr dilela path absolute asel tr true 

    if flag == False:
        DirName = os.path.abspath(DirName)      #jr path absolute nasel tr path la absolute path madhe convert kara

    exist = os.path.isdir(DirName)      #path directory cha ahe ki nahi te check krnya sathi

    if exist:        #if exist ==True   
        #       1           2               3
        for foldername, subfoldername, filename in os.walk(DirName):    #3 return values ahet                
            for fname in filename:
                filepath = os.path.join(foldername,fname)
                if(MaxSize < os.path.getsize(filepath)): 
                    MaxSize = os.path.getsize(filepath)
                    MaxSizeFileName = filepath
        print("Maximum Sized file name is : ",MaxSizeFileName," with size : ",MaxSize)          
        
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
        print("Example : Demo.py Marvellous")
        exit()

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name File_Name
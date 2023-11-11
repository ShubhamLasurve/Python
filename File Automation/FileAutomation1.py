#File Automation
#input mhanun folder ch naav 
#Accept folder name from user and display all the files and sub folders in it

from sys import *
import os

def DirectoryTravel(DirName):
    print("We are going to scan the directory : ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        for fname in filename: 
            print(fname)

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
        DirectoryTravel(argv[1])

if  __name__ == "__main__":
    main()
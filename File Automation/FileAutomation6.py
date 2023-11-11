from sys import *
import os
import time

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)

    flag = os.path.isabs(DirName)       #jr dilela path absolute asel tr true 

    if flag == False:
        DirName = os.path.abspath(DirName)      #jr path absolute nasel tr path la absolute path madhe convert kara

    exist = os.path.isdir(DirName)      #path directory cha ahe ki nahi te check krnya sathi

    if exist:        #if exist ==True   
        #       1           2               3
        for foldername, subfoldername, filename in os.walk(DirName):    #3 return values ahet                
            for fname in filename:
                print(fname, " : ", os.path.getsize(os.path.join(foldername,fname)), " bytes")  #join method 2 paths la join karun dete
                #join method chya parameter chya folder name madhe file parant cha path yeil ani fname madhe file names yetil
        
    else:
        print("Invalid path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument")
        print("Example : Demo.py Marvellous")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()


#for foldername, subfoldername, filename in os.walk(DirName,FileName):
#   for fname in filename:
#       if(fname == FileName):
#           print("File found")
#       else:
#           print("File not found")
# python FileAutomation.py Directory_Name
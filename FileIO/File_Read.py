#Read the data in existing file

import os

def main():
    print("Enter the name of file that you want to open for reading  purpose : ")
    File_name = input()

    if os.path.exists(File_name):       #hi method file ahe ki nahi check krte
        fobj = open(File_name, "r")     #r mhanje file read mode madhe open (data baghayla)
        if fobj:              #if(fobj == true)
            print("File successfully opened in append mode") 

            Data = fobj.read()      #data read chi method
            print("Data from file is : ",Data)

            fobj.close()  
        else:
            print("Unable to open file")        
    else:
        print("There is no such file")     

if __name__ == "__main__":
    main()
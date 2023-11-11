#Write the data in existing file

import os

def main():
    print("Enter the name of file that you want to open for writing  purpose : ")
    File_name = input()

    if os.path.exists(File_name):       #hi method file ahe ki nahi check krte
        fobj = open(File_name, "w")     #w mhanje write mode(data override krto...unsafe ahe)
        if fobj:              #if(fobj == true)
            print("File successfully opened in write mode") 

            print("Enter the data that you want to write in the file")
            Data=input()

            fobj.write(Data)        #Write the data into the file
            
            fobj.close()  
        else:
            print("Unable to open file")        
    else:
        print("There is no such file")     

if __name__ == "__main__":
    main()
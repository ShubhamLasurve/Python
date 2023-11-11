#Creating the new file 
#Check whether the file is in the folder or not
#Open method is used to create as well as open the file

import os

def main():
    print("Enter the name of file that you want to create")
    File_name = input()

    if os.path.exists(File_name):       #hi method file ahe ki nahi check krte
        print("Unable to create a file as file is already exists")
    else:
        fobj = open(File_name, "x")     

if __name__ == "__main__":
    main()
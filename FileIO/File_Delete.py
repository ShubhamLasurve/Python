#Delete the existing file

import os

def main():
    print("Enter the name of file that you want to delete")
    File_name = input()

    if os.path.exists(File_name):       #hi method file ahe ki nahi check krte
        os.remove(File_name)            #hi method file delete krte
    else:
        print("There is no such file")     

if __name__ == "__main__":
    main()
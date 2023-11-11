#Creating the new file 
#Open method is used to create as well as open the file
def main():
    print("Enter the name of file that you want to create")
    File_name = input()

    fobj = open(File_name, "x")     
    #1st parameter : Name of file that you want to create
    #2nd parameter cha meaning file cha use kasha sathi karaycha ahe tya sathi(check notes)


if __name__ == "__main__":
    main()
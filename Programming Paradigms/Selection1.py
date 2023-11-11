#Even Odd

def main():
    print("Enter Number : ")
    No = int(input())

    Result = No % 2 

    if(Result == 0):
        print("Given number is even")
    else:
        print("Given number is odd")
    
if __name__ == "__main__":
    main()
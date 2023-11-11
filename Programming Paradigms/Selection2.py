#Even Odd


def CheckEven(Value):
    Result = Value % 2 

    if(Result == 0):
        print("Given number is even")
    else:
        print("Given number is odd")

def main():

    No = 0
    print("Enter Number : ")
    No = int(input())

    CheckEven(No)
    
if __name__ == "__main__":
    main()
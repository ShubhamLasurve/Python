#Demonstration of advanced functions

#Function Accepts parameter as another function

def Add(A,B):
    return A+B

def Marvellous(FPTR):
    print(type(FPTR))
    Ans = FPTR(11,7)
    print("Addition is : ",Ans)

def main():
    Marvellous(Add)

if __name__ == "__main__":
    main()
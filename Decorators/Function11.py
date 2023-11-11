#Demonstration of advanced functions

#Function Accepts parameter as another function

def Add(A,B):       #0x00000218E76E3E20
    return A+B

def Marvellous(FPTR):
    print(type(FPTR))
    print(FPTR)
    Ans = FPTR(11,7)        #Ans = 0x00000218E76E3E20(11,7)
    print("Addition is : ",Ans)

def main():
    Marvellous(Add)     #Marvellous(0x00000218E76E3E20)

if __name__ == "__main__":
    main()
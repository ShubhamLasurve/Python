#Demonstration of advanced functions

#Function Accepts multiple parameters and returns multiple parameters
#Only in Python

def Marvellous(Value1,Value2):
    Addition = Value1 + Value2
    Substraction = Value1 - Value2
    Multiplication = Value1 * Value2

    return Addition,Substraction,Multiplication

def main():
    Ret = Marvellous(11,6)
    print(type(Ret))
    print("Addition is : ",Ret[0])
    print("Substraction is : ",Ret[1])
    print("Multiplication is : ",Ret[2])
    
if __name__ == "__main__":
    main()
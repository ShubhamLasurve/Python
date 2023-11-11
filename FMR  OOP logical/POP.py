# Procedure Oriented Programming

def Addition(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Substraction(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def main():
    Value1 = int(input("Enter first number : "))
    Value2 =int(input("Enter second number : "))

    Ret = Addition(Value1,Value2)
    print("Addition is : ",Ret)

    Ret = Substraction(Value1,Value2)
    print("Substraction is : ",Ret)
    
if __name__ == "__main__":
    main()
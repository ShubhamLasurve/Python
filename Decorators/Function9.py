#Demonstration of advanced functions

#Function Accepts parameters and call another function from it and return multiple values

Add = lambda A,B : A+B

Sub = lambda A,B:A-B

def Marvellous(Value1,Value2):
    Ans1 = Add(Value1,Value2)
    Ans2 = Sub(Value1,Value2)

    return Ans1,Ans2

def main():
    Arr = Marvellous(11,7)
    print("Addition is : ",Arr[0])
    print("Substraction is :",Arr[1])

if __name__ == "__main__":
    main()
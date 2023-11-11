
import Marvellous #module import kel

def main():
    Value1 = int(input("Enter First number : "))
    Value2 = int(input("Enter Second number : "))

    Result = 0
    Result = Marvellous.Addition(Value1,Value2)     #module madhl specific function call kel
    print("Addition is : ",Result)

    Result = 0
    Result = Marvellous.Substraction(Value1,Value2)
    print("Substraction is : ",Result)


    Result = 0
    Result = Marvellous.Multiplication(Value1,Value2)
    print("Multiplication is : ",Result)


if __name__ == "__main__":
    main()
#FMR: Filter Map Reduce

from functools import reduce        #module for reduce function

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def Increase(No):
    return No + 2

def Add(A,B):
    return A+B

def main():
    print("Demonstration of Filter Map Reduce")
    Data = []

    print("Enter number of elements")
    Size = int(input())

    print("Enter the elements")
    for i in range(Size):
        value = int(input())
        Data.append(value)

    print(Data)

    output = list(filter(CheckEven,Data))
    print(output)

    moutput = list(map(Increase,output))
    print(moutput)

    result = reduce(Add,moutput)
    print(result)

if __name__ == "__main__":
    main()
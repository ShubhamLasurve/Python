#FMR: Filter Map Reduce
#using lambda 
from functools import reduce        #module for reduce function

CheckEven = lambda No : (No % 2 == 0)

Increase = lambda No: (No + 2)
    
Add= lambda A,B:( A+B)

def main():
    print("Demonstration of Filter Map Reduce")
    Data = []

    print("Enter number of elements")
    Size = int(input())

    print("Enter the elements")
    for i in range(Size):
        value = int(input())
        Data.append(value)

    print("Input Data : ",Data)

    output = list(filter(CheckEven,Data))
    print("Output after Filter : ",output)

    moutput = list(map(Increase,output))
    print("Output After Map : ",moutput)

    result = reduce(Add,moutput)
    print("Output after Reduce : ",result)

if __name__ == "__main__":
    main()
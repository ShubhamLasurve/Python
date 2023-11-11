#FMR: Filter Map Reduce
#Using lambda 

import functools         #module for reduce function

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

    output = list(filter(lambda No : (No % 2 == 0),Data))
    print("Output after Filter : ",output)

    moutput = list(map(lambda No: (No + 2),output))
    print("Output After Map : ",moutput)

    result = functools.reduce(lambda A,B:(A+B),moutput)
    print("Output after Reduce : ",result)

if __name__ == "__main__":
    main()
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
    Data = [5,4,9,8,13,17,12,18]
    print(Data)

    output = list(filter(CheckEven,Data))
    print(output)

    moutput = list(map(Increase,output))
    print(moutput)

    result = reduce(Add,moutput)
    print(result)

if __name__ == "__main__":
    main()
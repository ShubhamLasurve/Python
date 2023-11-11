#FMR: Filter Map Reduce
#using lamda
#Using swatach logic
# #Swatach module tayar karun 

import MarvellousFMR

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

    output = list(MarvellousFMR.filterX(CheckEven,Data))
    print("Output after Filter : ",output)

    moutput = list(MarvellousFMR.mapX(Increase,output))
    print("Output After Map : ",moutput)

    result = MarvellousFMR.reduceX(Add,moutput)
    print("Output after Reduce : ",result)

if __name__ == "__main__":
    main()
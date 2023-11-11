#FMR: Filter Map Reduce
#using lamda
#Using swatach logic 

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No: (No + 2)    
Add= lambda A,B:( A+B)

#Task : Name of Function 
#Elements : List of Data elements

def filterX(Task, Elements):
    Result = []
    for no  in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

#Task : Name of Function 
#Elements : List of Data elements

def mapX(Task,Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

#Task : Name of Function 
#Elements : List of Data elements

def reduceX(Task,Elements):
    Sum=0
    for no in Elements:
        Sum = Task(Sum,no)
    return Sum

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

    output = list(filterX(CheckEven,Data))
    print("Output after Filter : ",output)

    moutput = list(mapX(Increase,output))
    print("Output After Map : ",moutput)

    result = reduceX(Add,moutput)
    print("Output after Reduce : ",result)

if __name__ == "__main__":
    main()
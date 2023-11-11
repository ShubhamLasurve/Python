#Modle for FMR11





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
#Demonstration of advanced functions

#Function defines another function inside it(Inner Function) and return as its return value
#Only in Python

def Marvellous(Value1,Value2):     
    def Add(A,B):      
        return A+B
    return Add(Value1,Value2)       

def main():             
    Ret = Marvellous(10,7)    
    
    print("Addition is : ",Ret)   

if __name__ == "__main__":
    main()              
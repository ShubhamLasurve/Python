#Demonstration of advanced functions

#Function defines another function inside it(Inner Function) and return as its return value
#Only in Python

def Marvellous():      #0X200
    def Add(A,B):      #0X100
        return A+B
    return Add          #return 0X100

def main():             #0X300
    Ret = Marvellous()  #0X200()
    Ans = Ret(10,7)     #0X100(10,7)
    
    print("Addition is : ",Ans)   

if __name__ == "__main__":
    main()              #0X300()
#Demonstration of Decorator

#Suppose Sub() is an inbuilt function
#We canot modify the inbuilt function
def Sub(A,B):               #0X100
    return A-B

#Decorator
def SmartSub(FPTR):         #0X200
    def Inner(A,B):         #0X300
        if(A<B):
            A,B = B,A
        return FPTR(A,B)            #return 0X100
    return Inner                    #retuen 0X300

def main():                                 
    SubX = SmartSub(Sub)        #0X200(0X100)
    #SubX = 0X300 
    Ret = SubX(10,7)               #0X300(10,7)
    print("Substraction is : ",Ret)

    Ret = SubX(7,10)                #0X300(7,10)
    print("Substraction is : ",Ret)

if __name__ == "__main__":
    main()
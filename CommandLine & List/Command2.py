#Demonstration of Command line argument
#Addition of two numbers using command line argument

import sys      #for use of command line arguments

def main():
    print("Demonstration of Command Line Arguments")

    Value1 = int(sys.argv[1])
    Value2 = int(sys.argv[2])
    Ans = Value1 + Value2

    print("Addition is : ",Ans)


if __name__ == "__main__":
    main() 

#python Command1.py Marvellous 11
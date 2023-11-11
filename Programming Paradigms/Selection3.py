#Even Odd
import Infosystems      #imported user defined module named Infosystems

def main():

    No = 0
    print("Enter Number : ")
    No = int(input())

    Infosystems.CheckEven(No)
    
if __name__ == "__main__":
    main()
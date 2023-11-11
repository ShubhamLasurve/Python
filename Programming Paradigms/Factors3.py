# Code to display Factors of number


def Factor(Value):
    for i in range(1,Value,1):
        if(Value % i == 0):
            print(i)

def main():
    print("Enter Number")
    No = int(input())
    Factor(No)

if __name__ == "__main__":
    main()
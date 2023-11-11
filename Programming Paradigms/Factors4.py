# Code to display Factors of number


def Factor(Value):
    i = 1
    while(i < Value):
        if(Value % i == 0):
            print(i)
        i = i + 1

def main():
    print("Enter Number")
    No = int(input())
    Factor(No)

if __name__ == "__main__":
    main()
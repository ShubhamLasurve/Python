# Code to display Factors of number

No = int(input("Enter the number"))

for i in range(1,No,1):
    if(No % i == 0):
        print(i)
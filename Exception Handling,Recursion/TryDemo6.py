
def main():
    try:
        print("Enter first number")
        No1 = int(input())

        print("Enter Second number ")
        No2 = int(input())
        
        Ans = 0
        Ans = No1/No2

    except ZeroDivisionError as zobj1:
        print("Divide by Zero is not allowed",zobj1)
        return

    except ValueError as zobj3:
        print("Invalid input ",zobj3)
        return

    except Exception as zobj2:
        print("Excepption Occured as",zobj2)
        return

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()
#Demonstration of advanced functions

#Function Accepts one parameter and returns Nothing
def Marvellous(Name):
    print("Inside Marvellous Function")
    print("Welcome ",Name)
    print(type(Name))

def main():
    Marvellous("Amit")
    Marvellous(90.90)

if __name__ == "__main__":
    main()
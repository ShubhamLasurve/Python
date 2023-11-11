#class variable
#class method

class HDFC:
    ROI = 9.5           #class Variable
    def __init__(self,Name,Amount):
        self.AccountHolder = Name
        self.Balance = Amount       #Instance variable
        print("Welcome ",self.AccountHolder)
        print("Your Account gets successfully created with initial balance : ",self.Balance)

    def DisplayBalance(self):       #instance method
        print("Hello ",self.AccountHolder)
        print("Your account Balance is : ",self.Balance)

    def Withdraw(self,Amount):      #instance method
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance = self.Balance - Amount
            print("Amount withdrawal successfully...")

    def Deposit(self,Amount):       #instance method
        self.Balance = self.Balance + Amount
        print("Amount deposited successfully...")

    @classmethod                        #bracket madhe cls lihaych
    def DisplayBankInfo(cls):           #class method       decorator lihava lagto
        print("welcome to HDFC bank portal")
        print("Our Bank is Private Limited Bank")
        print("We Provide the Rate Of Interest on Saving Account is : ",cls.ROI)        #Accessing class variable in class 

    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI, you should provide below documents for KYC ")
        print("Your Adhar Card")
        print("Your PAN Card")
        print("Your Passport Sized photo")

def main():
    print("ROI of HDFC bank is : ",HDFC.ROI)

    HDFC.DisplayBankInfo()

    HDFC.DisplayKYCInfo()

    print("Creating new Account...")
    Amit = HDFC("Amit",5000)           #__init__(100,"Amit",5000)
    
    print("Creating new Account...")
    Sagar = HDFC("Sagar",3000)           #__init__(200,"Sagar",3000)

    print("Performing operations on OBJ1")
    Amit.Deposit(2000)
    Amit.DisplayBalance()

    Amit.Withdraw(1000)
    Amit.DisplayBalance()

    print("Performing operations on Sagar's account")

    Sagar.Deposit(4000)
    Sagar.DisplayBalance()

    Sagar.Withdraw(500)
    Sagar.DisplayBalance()

if __name__ == "__main__":
    main()
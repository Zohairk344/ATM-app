class ATM: 
    def __init__(self) -> None:
        self.Pin = 1234
        self.Balance = 5000
    
    def Check_Pin(self, Input_Pin):
        try :
            if self.Pin == Input_Pin :
                print("Pin Matches, Access Granted")
                return True
            else :
                print("Incorrect Pin, Access Denied")
                return False
        except ValueError:
            print("Please enter a valid number")
            return False
        
    def Check_Balance(self) :
        print(f"You Have {self.Balance} left in you account")
    
    def Deposit(self, Amount):
        if Amount > 0 :
            self.Balance += Amount
            print(f"Money Deposited. You now have {self.Balance} rupees")
        else :
            print("Incorrect Value")
    
    def Withdraw(self, Amount):
        if Amount > 0 and Amount <= self.Balance :
            self.Balance -= Amount
            print(f"{Amount} withdrawn. {self.Balance} rupees left in the account.")
        elif Amount > self.Balance :
            print("Insufficient Balance in Account")
        else :
            print("Incorrect Amount")
    
    def Exit(self):
        print("Thank you for using our ATM. Goodbye!")
        

def Main():    
    atm = ATM()
    Input_Pin = int(input("Enter PIN: "))
    while not atm.Check_Pin(Input_Pin):
        Input_Pin = int(input("Enter PIN: "))

    while True:
        Choice = int(input("""                
=== ATM MENU ===
1: Check Balance
2: Deposit Money
3: Withdraw Money
4: Exit ATM
          
Enter Choice(1-4) : """))

        if Choice == 1:
            atm.Check_Balance()  
            
        elif Choice == 2:
            Amount = int(input("Input Amount of money you want to deposit: "))
            Input_Pin = int(input("Re-enter PIN for verification: "))
            while not atm.Check_Pin(Input_Pin):
                Input_Pin = int(input("Re-enter PIN for verification: "))
            atm.Deposit(Amount)
        
        elif Choice == 3:
            Amount = int(input("Input Amount of money you want to withdraw: "))
            Input_Pin = int(input("Re-enter PIN for verification: "))
            while not atm.Check_Pin(Input_Pin):
                Input_Pin = int(input("Re-enter PIN for verification: "))
            atm.Withdraw(Amount)

        elif Choice == 4:
            atm.Exit()
            break

        else :
            print("Incorrect Option. please choose between 1 and 4")

if __name__ == "__main__" :
    Main()
print("Welcome to the bank")
print("Here you can deposit and withdrawal")

class ATM:
    def __init__(self):
        self.balance=0
        
    def deposit(self):
        amount=float(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print("Amount Deposited: ",amount)

    def withdraw(self):
        amount = float(input("Enter the amount you wish to withdrawal: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Net Available Balance=", self.balance)

s = ATM()

s.deposit()
s.withdraw()
s.display()


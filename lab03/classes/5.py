class Account:
    pass
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, month, percent):
        for i in range(month):
            self.balance += percent*self.balance
        print(f"And your balance after {month} is {self.balance}")
    def withdraw(self, get):
        if get<0:
            print("You can't take negative amount of money!")
        elif get > self.balance:
            print("Not enough money!")
        else:
            print(f"You are taking {get} and {self.balance - get} have left!")
            self.balance -= get
            
account = Account(input("Your name? "), int(input("Write your balance: ")))
account.withdraw(int(input("How much do you want to get? ")))
account.deposit(int(input("For how many months do you want to put the money for? ")), 15)
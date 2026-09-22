class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def interest(self):
		interest=self.balance *0.02
		return interest
	




class SavingsAccount(BankAccount):

	def __init__(self,name,balance=0):
		super()._init_(name,balance)

	def __privateaccount(self):
            print("acount created")
              

def interest(self):
		interest=self.balance *0.03
		return interest

obj1=BankAccount('sahal',1000)
print(obj1.deposit(5000))
print(obj1.withdraw(20000))
obj1.calculate_interest()

obj2=SavingsAccount('sabu',7000,27)
print(obj2.deposit(5000))
print(obj2.withdraw(20000))
print(obj2.calculate_interest())
obj2._SavingsAccount__privateaccount()









      
      



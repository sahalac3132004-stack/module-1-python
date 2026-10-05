#Create an abstract class Payment with abstract methods make_payment() and payment_status(). Implement two concrete classes CreditCardPayment and UPIPayment. Write a program where the user chooses the payment method and the respective class handles the process.
from abc import ABC, abstractmethod


# Abstract class
class Payment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass

    @abstractmethod
    def payment_status(self):
        pass


# Credit Card Payment
class CreditCardPayment(Payment):

    def make_payment(self, amount):
        print(f"Credit Card payment of ₹{amount} completed.")

    def payment_status(self):
        print("Payment Status: Successful")


# UPI Payment
class UPIPayment(Payment):

    def make_payment(self, amount):
        print(f"UPI payment of ₹{amount} completed.")

    def payment_status(self):
        print("Payment Status: Successful")


# User chooses payment method
print("Choose Payment Method")
print("1. Credit Card")
print("2. UPI")

choice = input("Enter your choice: ")
amount = float(input("Enter amount: ₹"))

if choice == "1":
    payment = CreditCardPayment()

elif choice == "2":
    payment = UPIPayment()

else:
    print("Invalid payment method")
    exit()

# Process payment
payment.make_payment(amount)
payment.payment_status()
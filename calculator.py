x=int(input("enter the first value:"))
y=int(input("enter the second value"))
opr=input("enter the operator:")

def addition(x,y):
        result=x+y
        print(result)

def substraction(x,y):
        result=x-y
        print(result)

def multiplication(x,y):
        result=x*y
        print(result)

def division(x,y):
        result=x/y
        print(result)

def modulus(x,y):
        result=x%y
        print(result)

if opr=="+":
        addition(x,y)

elif opr=="-":
        substraction(x,y)

elif opr=="*":
        multiplication(x,y)

else :
        division(x,y)


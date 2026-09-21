n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
opr=input("enter the operator")

def addition(n1,n2):
    return n1+n2

def substraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    try:
     return n1/n2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.") 
    finally:
      print("execution completed")

if opr=="+":
    print(addition(n1,n2))
elif opr=="-":
    print(substraction(n1,n2))
elif opr=="*":
    print(multiplication(n1,n2))
elif opr=="/":
    print(division(n1,n2))
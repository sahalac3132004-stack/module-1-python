n=int(input("enter the number:"))

try :
     result=10/n
     print(result)

except ZeroDivisionError:
        print("cannot divide by zero")

finally :
        print("exeption is completed")


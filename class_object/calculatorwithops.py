n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
opr=input("enter the operator")

class calculator:

	def addition(self,n1,n2):
		return n1+n2
      

	def substraction(self,n1,n2):
		return n1-n2
		
	def multiplication(self,n1,n2):
			return n1*n2
      

	def division(self,n1,n2):
		try:
			return n1/n2
		except ZeroDivisionError:
			print("Error: Division by zero is not allowed.") 
		finally:
			print("execution completed")


obj=calculator()
if opr=="+":
    print(obj.addition(n1,n2))
elif opr=="-":
    print(obj.substraction(n1,n2))
elif opr=="*":
    print( obj.multiplication(n1,n2))
elif opr=="/":
    print(obj.division(n1,n2))



obj.addition(n1,n2)
obj.substraction(n1,n2)
obj.multiplication(n1,n2)
obj.division(n1,n2)


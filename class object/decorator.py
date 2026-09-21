def my_decorator(func):
	def wrapper():
		func()
		print("this is decorator function")

	return wrapper


@my_decorator

def greet():
	pass

greet()


#decorator is essentially a function that takes another function as an argument,and returns a new function with enhanced functionaliti
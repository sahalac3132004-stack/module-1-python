def my_decorator(func):
	def wrapper(a, b):
		result=func(a,b)
		return abs(result)
	return wrapper
		
		
		
@my_decorator	
def addition(a,b):
	result =a-b
	return result

print(addition(2,5))
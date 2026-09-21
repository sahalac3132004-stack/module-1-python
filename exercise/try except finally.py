try:
	print(10/0)
except ZeroDivisionError:
	print("zero")
else:
	print("else")
finally:
	print("finally")
	
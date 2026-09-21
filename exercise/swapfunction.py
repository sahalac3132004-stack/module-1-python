class A:
	x=10

class B(A):
	pass



a=A()
b=B()
print(a.x,b.x)
A.x=30
print(a.x,b.x)
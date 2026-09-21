def f():
	print("A")
	yield 1
	print("B")
	yield 2

g=f()
print(next(g))
print(next(g))

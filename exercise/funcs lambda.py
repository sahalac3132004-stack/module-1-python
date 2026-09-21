funcs= []
for i in range(5):
	funcs.append(lambda i=i: i)
print([f() for f in funcs])
class parent:

	x =10


	def parent_method(self):
		print("this is parent method")


class child(parent):

   x=20	
   def child_method(self):
       print("this is child method")

   def parent_method(self):
       print("this is parent method from child class")


obj=parent()
obj.parent_method()
obj1=child()
obj1.child_method()
obj1.parent_method()
print(obj1.x)
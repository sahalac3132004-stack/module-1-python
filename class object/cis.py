class Student():

	count=0

	def __init__(self,name):
		self.name=name
		Student.count += 1

	#instance method
	def detail(self):
		print(f'My name is {self.name}')

	#class method
	@classmethod
	def class_method(cls):
		print(f'student count:{cls.count}')

	#static method
	@staticmethod
	def static_method(a,b):
		return a+b


obj=Student('sahal')
obj.detail()

obj1 =Student('samil')
obj1.detail()
Student.class_method()
print(Student.static_method(10,2))



	



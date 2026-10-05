class person():

	def __init__(self,name,age):
		self.__name=name #private variable
		self.__age=age

    #getter
	
	def get_name(self):
		print(self.__name)
		

	def get_age(self):
		print(self.__age)


    #setter
	
	def set_name(self,name):
		self.__name=name

	def set_age(self,age):
		self.__age=age


obj=person('sahal','22')
obj.get_name()
obj.get_age()

obj.set_name('john')
obj.set_name
obj.set_age






		
	
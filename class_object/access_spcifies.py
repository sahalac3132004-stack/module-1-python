#access specifies
class detail():

	def __init__(self,name,age,password):
		self.name=name
		self._age=age
		self._password=password

	def show_password(self):
		return f'show password {self._password}'
	

obj=detail('sahal','22','1234')
print(obj.name)
print(obj._age)
print(obj.show_password())











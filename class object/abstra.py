from abc import ABC, abstractmethod

#Abstract class
class vehicle(ABC):
	@abstractmethod

	def start(self):
		pass

#concrete class
class car(vehicle):
	def start(self):
		print("car engine started with a key")

#concrete class 2
class bike(vehicle):
	def start(self):
		print("bike engine started with a kickstart")


#usage
v1=car()
v1.start()


v2=bike()
v2.start()
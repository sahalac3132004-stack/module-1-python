class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

employee = Employee("Sahal", 22, 50000)

print("name:",employee.name)
print("age:",employee.age)
print("salary:",employee.salary)

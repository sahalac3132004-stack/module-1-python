class Employee():
	company_name = "TechNova Solutions"

	def __init__(self, emp_name, emp_id, salary):
			self.emp_name = emp_name
			self.emp_id = emp_id
			self.salary = salary

	def display_details(self):
			print(f"Employee Name : {self.emp_name}")
			print(f"Employee ID   : {self.emp_id}")
			print(f"Salary        : {self.salary}")
			print(f"Company Name  : {Employee.company_name}")

	@classmethod
	def change_company_name(cls, new_name):
		cls.company_name = new_name





class Developer(Employee):
    def __init__(self, emp_name, emp_id, salary, programming_language):
        super().__init__(emp_name, emp_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()  
        print(f"Programming Language : {self.programming_language}")


class Manager(Employee):
    def __init__(self, emp_name, emp_id, salary, team_size):
        super().__init__(emp_name, emp_id, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size : {self.team_size}")

developer1 = Developer("sahal", "s108", 35000, "Python")
manager1 = Manager("arjun", "s201", 55000, 4)


print("\n Developer Details")
developer1.display_details()

print("\n Manager Details")
manager1.display_details()


Employee.change_company_name("Zyvion Technologies")
print("\n After Company Name Update")

print("\n Developer Details")
developer1.display_details()

print("\n Manager Details")
manager1.display_details()





	
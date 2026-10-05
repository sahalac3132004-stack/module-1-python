class Employee():
    def __init__(self, name):
        self.name = name


class FullTimeEmployee(Employee):
    
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Freelancer(Employee):
    
		def __init__(self, name, pay_per_project, projects_completed):
			super().__init__(name)
			self.pay_per_project = pay_per_project
			self.projects_completed = projects_completed

		def calculate_salary(self):
			return self.pay_per_project * self.projects_completed




employee1=FullTimeEmployee("sahal", 5000)
employee2=PartTimeEmployee("sabu", 25, 80)
employee3=Freelancer("john",30000,2)

employees = [employee1,employee2,employee3]


for employee in employees:
    print("employee",employee.name)
    print("salary",employee.calculate_salary())
    








    


        
	


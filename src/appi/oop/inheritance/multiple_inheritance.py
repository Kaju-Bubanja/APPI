# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)


# Child class
class Employee(Person, Company):
    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.employee_info(12000, 'Machine Learning')


class Employee2(Person):

    def __init__(self):
        self.company = Company()

    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp2 = Employee2()

# access data
emp2.person_info('Lisa', 26)
emp2.company.company_info('Facebook', 'San Francisco')
emp2.employee_info(11000, 'Machine Learning')

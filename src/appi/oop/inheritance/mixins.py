# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


# Parent class 2
class HealthInsuranceMixin:
    def __init__(self, type="standard"):
        if type == "extra":
            self.benefits = ["Dental", "Optometrist", "General", "Rega", "Private doctor"]
        else:
            self.benefits = ["Dental", "Optometrist", "General"]

    def show_benefits(self):
        print(f'Employee has health insurance benefits: {self.benefits}')


# Child class
class EmployeeInsured(Person, HealthInsuranceMixin):
    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)
        self.show_benefits()


class EmployeeNotInsured(Person):
    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


emp = EmployeeInsured()
emp.person_info('Lisa', 26)
emp.employee_info(11000, 'Machine Learning')

emp.person_info('Ralph', 28)
emp = EmployeeNotInsured()
emp.employee_info(12000, 'Machine Learning')


class HealthInsurance:
    def __init__(self, type="standard"):
        if type == "extra":
            self.benefits = ["Dental", "Optometrist", "General", "Rega", "Private doctor"]
        else:
            self.benefits = ["Dental", "Optometrist", "General"]

    def show_benefits(self):
        print(f'Employee has health insurance benefits: {self.benefits}')


class Employee(Person):
    def __init__(self):
        self.insurance = HealthInsurance("standard")

    def set_insurance(self, name):
        self.insurance = HealthInsurance(name)

    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)
        self.insurance.show_benefits()


emp.person_info('Simon', 30)
emp = Employee()
emp.employee_info(13000, 'Sys admin')
emp.set_insurance("extra")
emp.employee_info(13000, 'Sys admin')


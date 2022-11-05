# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def show2(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, self.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name

    def modify_school_name2(self, new_name):
        # create instance attribute
        self.school_name = new_name


s1 = Student("Harry", 12)

# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
s1.show()
s1.show2()
s1.modify_school_name2('UVW School')
# call instance methods
s1.show()
s1.show2()

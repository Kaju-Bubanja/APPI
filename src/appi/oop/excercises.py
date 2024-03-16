# 1: Create a Vehicle class with max_speed and mileage instance attributes, create an object and print their attributes

# 2: Create a Vehicle class without any variables and methods


# 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Implement __str__ to print all attributes of the vehicle
# Given
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Expected Output:
# Vehicle Name: School Volvo Speed: 180 Mileage: 12


# 4: Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# You need to use method overriding.
# Given
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Expected Output:
# The seating capacity of a bus is 50 passengers


# 4.1 Make the seating capacity a child specific instance attribute and modify the child seating_capacity method
# to take no argument, but to take the instance attribute


# 5: Define property that should have the same value for every class instance
# Define a class attribute ”color” with a default value white. I.e., Every Vehicle and every Car should be white.
# Given
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18


# 6: Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
# Given
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

# Expected Output
# Total Bus fare is: 5500.0

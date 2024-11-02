class Car:
    # Class attribute to keep track of the number of cars created
    total_cars = 0
    tires = 4

    def __init__(self, make, color):
        self.make = make
        self.color = color
        Car.total_cars += 1

    @classmethod
    def reset_counter(cls):
        cls.total_cars = 0

    @staticmethod
    def miles_to_km(miles):
        return miles * 1.60934

# Creating instances
car1 = Car("Toyota", "blue")
car2 = Car("Honda", "yellow")
car3 = Car("Ford", "white")

# Accessing the class attribute
print(f"Total cars created: {Car.total_cars}")


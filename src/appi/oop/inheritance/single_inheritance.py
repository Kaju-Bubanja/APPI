# Base class
class Vehicle:
    def vehicle_info(self):
        print('Inside Vehicle class')


# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


# Create object of Car
car = Car()

# access Vehicle's info using car object
car.vehicle_info()
car.car_info()
print(type(car))

v = Vehicle()
print(type(v))

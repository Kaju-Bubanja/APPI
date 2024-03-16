class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Bus(Vehicle):
    def __init__(self, name, color, seats):
        super().__init__(name, color)
        self.seats = seats


b = Bus("Kirby", "blue", 50)
print(b.name, b.color, b.seats)

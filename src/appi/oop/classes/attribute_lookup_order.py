class Warehouse:
    purpose = 'storage'
    region = 'west'

    def __init__(self):
        self.region = "east"

w1 = Warehouse()
print(w1.region)
# prints "east"
print(Warehouse.region)
# prints "west"


# Reframing previously used syntax (constructors) and object methods
x = []
x = list()
x.append(5)
print(x)

y = dict()
y = {"2": "abc"}
print(y.items())

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

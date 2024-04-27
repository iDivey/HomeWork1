class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


house = House()
print(house.numberOfFloors)
house.setNewNumberOfFloors(150)
print(house.numberOfFloors)
class House:
    numberOfFloors = 10


house = House()
while house.numberOfFloors < 100:
    print(f"Текущий этаж равен {house.numberOfFloors}")
    house.numberOfFloors += 10
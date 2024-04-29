class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


hrushevka = Building(5, 'Хрущевка')
neboskreb = Building(1000, 'Небоскреб')
if hrushevka == neboskreb:
    print('Допустим')
else:
    print('Поверим')

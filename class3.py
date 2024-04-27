class Building:
    def __init__(self):
        self.numberOfFloors = 5
        self.buildingType = 'Хрущёвка'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


hrushevka = Building()
neboskreb = Building()
if hrushevka == neboskreb:
    print('Допустим')
else:
    print('Поверим')
neboskreb.numberOfFloors = 1000
neboskreb.buildingType = 'Небоскреб'
if hrushevka == neboskreb:
    print('Допустим')
else:
    print('Поверим')

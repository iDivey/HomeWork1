class Car:
    price = 1000000

    power = 100

    def horse_powers(self):
        print(self.power)


car = Car()
car.horse_powers()


class Nissan(Car):
    price = Car.price + 255555

    def horse_powers(self):
        print(Car.power + 50)


nissan = Nissan()
nissan.horse_powers()


class Kia(Car):
    price = Car.price - 100000

    def horse_powers(self):
        print(Car.power - 10)


kia = Kia()
kia.horse_powers()
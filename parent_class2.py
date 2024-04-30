class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    power = 100

    def horse_powers(self):
        return self.power


class Nissan(Vehicle, Car):
    vehicle_type = "легковушка - езди сам"
    price = Car.price + 255555

    def horse_powers(self):
        return Car.power + 50


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)

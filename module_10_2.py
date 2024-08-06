from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        varvar = 100
        print(f'{self.name}, на нас напали!')
        day = 0
        while varvar != 0:
            sleep(1)
            day += 1
            varvar = varvar - self.power
            print(f'{self.name} сражается {day} день(дня)..., осталось {varvar}')
        print(f'{self.name},одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')

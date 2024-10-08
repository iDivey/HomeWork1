from threading import Thread
from time import sleep
import queue
from random import randint


class Table:
    def __init__(self, n, for_guest=False):
        self.n = n
        self.for_guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        s = randint(3, 10)
        sleep(s)


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table_for_guest = False
            for table in self.tables:
                if table.for_guest is None:
                    table.for_guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.n}')
                    table_for_guest = True
                    break
            if not table_for_guest:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.for_guest is not None for table in self.tables):
            for table in self.tables:
                if table.for_guest is not None:
                    if not table.for_guest.is_alive():
                        print(f"{table.for_guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.n} свободен")
                        table.for_guest = None

                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.for_guest = next_guest
                            next_guest.start()
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.n}")

            sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

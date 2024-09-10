import unittest as ut
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(ut.TestCase):
    def test_walk(self):
        try:
            forest = Runner('Forest', -5)
            for i in range(20):
                forest.walk()
            logging.info(f'"test_walk" выполнен успешно')
            self.assertEqual(forest.distance, 100)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            print('Упс')

    def test_run(self):
        try:
            gump = Runner(True, 5)
            for i in range(15):
                gump.run()
            self.assertEqual(gump.distance, 150)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            print('Упс')

    def test_challenge(self):
        r1 = Runner('Usain')
        r2 = Runner('Bolt')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    ut.main()

import unittest as ut


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(ut.TestCase):
    is_frozen = False

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        forest = Runner('Forest')
        for i in range(20):
            forest.walk()
        self.assertEqual(forest.distance, 100)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        gump = Runner('Gump')
        for i in range(15):
            gump.run()
        self.assertEqual(gump.distance, 150)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Usain')
        r2 = Runner('Bolt')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(ut.TestCase):
    is_frozen = True
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        t = Tournament(90, self.r1, self.r3)
        t1 = t.start()
        self.all_results.append(t1)
        i = len(t1)
        g = t1.get(i)
        name = 'Ник'
        a = g is name
        self.assertTrue(a)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        t = Tournament(90, self.r2, self.r3)
        t1 = t.start()
        self.all_results.append(t1)
        i = len(t1)
        g = t1.get(i)
        name = 'Ник'
        a = g is name
        self.assertTrue(a)

    @ut.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        t = Tournament(90, self.r1, self.r2, self.r3)
        t1 = t.start()
        self.all_results.append(t1)
        i = len(t1)
        g = t1.get(i)
        name = 'Ник'
        a = g is name
        self.assertTrue(a)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)


if __name__ == '__main__':
    ut.main()
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


class TournamentTest(ut.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    def test_run1(self):
        t = Tournament(90, self.r1, self.r3)
        t1 = t.start()
        self.all_results.append(t1)

    def test_run2(self):
        t = Tournament(90, self.r2, self.r3)
        t1 = t.start()
        self.all_results.append(t1)

    def test_run3(self):
        t = Tournament(90, self.r1, self.r2, self.r3)
        t1 = t.start()
        self.all_results.append(t1)

    def test(self):
        print(self.all_results)
        '''result = len(self.all_results) - 1
        r = self.all_results[result]
        i = len(r)
        g = r.get(i)
        name = 'Ник'
        a = g is name
        self.assertTrue(a)
        for result in self.all_results:
            i = len(result)
            g = result.get(i)
            name = 'Ник'
            a = g is name
            self.assertTrue(a)'''
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

if __name__ == '__main__':
    ut.main()



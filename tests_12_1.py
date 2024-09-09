import unittest as ut


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(ut.TestCase):
    def test_walk(self):
        forest = Runner('Forest')
        for i in range(20):
            forest.walk()
        self.assertEqual(forest.distance, 100)

    def test_run(self):
        gump = Runner('Gump')
        for i in range(15):
            gump.run()
        self.assertEqual(gump.distance, 150)

    def test_challenge(self):
        r1 = Runner('Usain')
        r2 = Runner('Bolt')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    ut.main()


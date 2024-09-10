import unittest as ut
import tests_12_3


testST = ut.TestSuite()
testST.addTest(ut.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(ut.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = ut.TextTestRunner(verbosity=2)
runner.run(testST)
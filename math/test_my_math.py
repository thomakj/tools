import unittest
from my_math import modulo3
from my_math import modulo5
from my_math import fibonacci
from my_math import sumOfEvenNumbers

class TestMyMathPy(unittest.TestCase):
    def testModulo3(self):
        self.assertTrue(modulo3(9))
        self.assertTrue(modulo3(30))
        self.assertFalse(modulo3(2))
        self.assertFalse(modulo3(20))

    def testModulo5(self):
        self.assertTrue(modulo5(5))
        self.assertTrue(modulo5(100))
        self.assertTrue(modulo5(1005))
        self.assertFalse(modulo5(111))
        self.assertFalse(modulo5(4))

    def testFibonacci(self):
        self.assertEqual(
            fibonacci(100),
            [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def testSumOfEvenNumbers(self):
        self.assertEqual(
            sumOfEvenNumbers([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
            44)

if __name__ == '__main__':
    unittest.main()

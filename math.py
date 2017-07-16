import math
import unittest

def modulo3(n):
    if n % 3: return False
    else: return True

def modulo5(n):
    if n % 5: return False
    else: return True

def sumOfEvenNumbers(list):
    sumOfEvenNumbers = 0
    for n in list:
        if not n % 2:
            sumOfEvenNumbers = sumOfEvenNumbers + n
    return sumOfEvenNumbers

def fibonacci(highestFibonacciNumber):
    i = 1
    j = 2
    fibNumbers = [i]
    while j < highestFibonacciNumber:
        fibNumbers.append(j)
        k = i + j
        i = j
        j = k
    return fibNumbers

class Test(unittest.TestCase):
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
        self.assertEqual(fibonacci(100),[1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def testSumOfEvenNumbers(self):
        self.assertEqual(sumOfEvenNumbers([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]), 44)

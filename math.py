import math
import unittest

def modulo3(n):
    if n % 3: return False
    else: return True

def modulo5(n):
    if n % 5: return False
    else: return True


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

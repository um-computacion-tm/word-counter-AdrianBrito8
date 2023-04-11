import unittest

def fibonacci(number):
    if number == 1:
        return 1
    a0 = 0
    a1 = 1
    for index in range(number):
        total += index
        return total
    

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, fibonacci(1))

    def testa_2(self):
        self.assertEqual(1, fibonacci(2))


if __name__ == '__main__':

    unittest.main()


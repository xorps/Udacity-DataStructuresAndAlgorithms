import unittest

def sqrt(number):
    if not isinstance(number, int): raise TypeError('expecting an integer')
    if number < 0: raise ValueError('number out of range')
    if number == 0: return 0
    def average(S, x):
        return ((S / x) + x) / 2
    guess = number / 2
    revised = average(number, guess)
    while int(guess) != int(revised):
        guess = revised
        revised = average(number, guess)
    return int(guess)

class SqrtTests(unittest.TestCase):
    def test_validation(self):
        with self.assertRaises(TypeError):
            sqrt('a')
        with self.assertRaises(ValueError):
            sqrt(-1)
    def test_zero(self):
        self.assertEqual(0, sqrt(0))
    def test_one(self):
        self.assertEqual(1, sqrt(1))
    def test_four(self):
        self.assertEqual(2, sqrt(4))
    def test_nine(self):
        self.assertEqual(3, sqrt(9))
    def test_sixteen(self):
        self.assertEqual(4, sqrt(16))
    def test_twentyseven(self):
        self.assertEqual(5, sqrt(27))

if __name__ == '__main__':
    unittest.main()
import unittest
import random

def get_min_max(ints):
    if not isinstance(ints, list): raise TypeError('expecting list')
    if len(ints) < 1: raise ValueError('ints must be 1 or greater')
    min = max = ints[0]
    for i in range(1, len(ints)):
        if ints[i] > max:
            max = ints[i]
        elif ints[i] < min:
            min = ints[i]
    return min, max

class MinMaxTests(unittest.TestCase):
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            get_min_max([])
        with self.assertRaises(TypeError):
            get_min_max(3)
    def test_case_one(self):
        ints = [3, -6, 9, 2, 8, 12, 32, 83, 24, 4, 7]
        result = get_min_max(ints)
        self.assertEqual(result, (min(ints), max(ints)))
    def test_case_random(self):
        ints = [i for i in range(0, 10)]
        random.shuffle(ints)
        self.assertEqual((0, 9), get_min_max(ints))
    def test_case_single(self):
        self.assertEqual((1, 1), get_min_max([1]))

if __name__ == '__main__':
    unittest.main()
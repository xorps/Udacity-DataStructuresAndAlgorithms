import unittest

def sort_012(input_list):
    if not isinstance(input_list, list): raise TypeError('expecting list')
    if len(input_list) < 1: raise ValueError('expecting a non-empty list')
    acc = [list(), list(), list()]
    for n in input_list:
        acc[n].append(n)
    return acc[0] + acc[1] + acc[2]

class Sort_012_Tests(unittest.TestCase):
    def test_inputs(self):
        with self.assertRaises(TypeError):
            sort_012(3)
        with self.assertRaises(ValueError):
            sort_012([])
    def test_case_one(self):
        input = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        self.assertEqual(sorted(input), sort_012(input))
    def test_case_two(self):
        input = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        self.assertEqual(sorted(input), sort_012(input))
    def test_case_three(self):
        input = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(sorted(input), sort_012(input))

if __name__ == '__main__':
    unittest.main()
import unittest

def add_remainder(result, array, index):
    while index < len(array):
        result.append(array[index])
        index += 1

def mergesort(array):
    if len(array) <= 1: return array
    mid = len(array) // 2
    left = mergesort(array[0:mid])
    right = mergesort(array[mid:])
    result = []
    left_index = 0
    right_index = 0
    # add greatest numbers first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    add_remainder(result, left, left_index)
    add_remainder(result, right, right_index)
    return result

def rearrange_digits(input_list):
    if not isinstance(input_list, list): raise TypeError('expecting a list')
    if len(input_list) < 2: raise ValueError('expecting list of at least 2 elements')
    # sort from greatest to lowest
    # then we can pick numbers in descending order for most significant digit
    input_list = mergesort(input_list)
    # these are our two numbers
    a = 0
    b = 0
    for n in input_list:
        # add `n` to the end
        a *= 10
        a += n
        # this alternates which number gets the next highest number
        a, b = b, a
    return [a, b] if a > b else [b, a]

class RearrangeTests(unittest.TestCase):
    def test_mergesort_empty(self):
        self.assertEqual(mergesort([]), [])
    def test_mergesort_single(self):
        self.assertEqual(mergesort([1]), [1])
    def test_mergesort(self):
        self.assertEqual(mergesort([1,2,3,4,5,6,7]), [7,6,5,4,3,2,1])
    def test_mergesort_even(self):
        self.assertEqual(mergesort([5,3,7,1]), [7,5,3,1])
    def test_type(self):
        with self.assertRaises(TypeError):
            rearrange_digits(1)
    def test_empty(self):
        with self.assertRaises(ValueError):
            rearrange_digits([])
    def test_single(self):
        with self.assertRaises(ValueError):
            rearrange_digits([1])
    def test_two(self):
        self.assertEqual(rearrange_digits([1, 2]), [2, 1])
    def test_case_one(self):
        self.assertEqual(rearrange_digits([1,2,3,4,5]), [531, 42])
    def test_case_two(self):
        self.assertEqual(rearrange_digits([4,6,2,5,9,8]), [964, 852])

if __name__ == '__main__':
    unittest.main()
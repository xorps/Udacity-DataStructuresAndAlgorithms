import unittest

def binary_search(array, lower_bound, upper_bound, number):
    while lower_bound <= upper_bound:
        if array[lower_bound] == number: return lower_bound
        if array[upper_bound] == number: return upper_bound
        middle = (lower_bound + upper_bound) // 2
        if array[middle] == number: return middle
        if array[middle] > number: upper_bound = middle - 1
        else: lower_bound = middle + 1
    return -1

def rotated_array_search(input_list, number):
    if not isinstance(input_list, list): raise TypeError('expecting a list')
    lower_bound = 0
    upper_bound = len(input_list) - 1
    while lower_bound <= upper_bound:
        if input_list[lower_bound] == number: return lower_bound
        if input_list[upper_bound] == number: return upper_bound
        middle = (lower_bound + upper_bound) // 2
        if input_list[middle] == number: return middle
        # if right half is sorted
        if middle + 1 < upper_bound and input_list[middle + 1] < input_list[upper_bound]:
            if input_list[middle + 1] <= number < input_list[upper_bound]: return binary_search(input_list, middle + 1, upper_bound - 1, number)
            else: upper_bound = middle
        # if left half is sorted
        if middle - 1 > lower_bound and input_list[lower_bound] < input_list[middle - 1]:
            if input_list[lower_bound] < number <= input_list[middle - 1]: return binary_search(input_list, lower_bound + 1, middle - 1, number)
            else: lower_bound = middle
        lower_bound += 1
        upper_bound -= 1
    return -1

class BinarySearchTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(0, binary_search([3], 0, 0, 3))
    def test_neg(self):
        self.assertEqual(-1, binary_search([4], 1, 0, 3))
    def test_simple(self):
        self.assertEqual(2, binary_search([1,2,3,4,5,6,7], 0, 4, 3))

class RotatedTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(-1, rotated_array_search([], 1))
    def test_single(self):
        self.assertEqual(0, rotated_array_search([5], 5))
        self.assertEqual(-1, rotated_array_search([5], 9))
    def test_case_1(self):
        self.assertEqual(0, rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
    def test_case_2(self):
        self.assertEqual(5, rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
    def test_case_3(self):
        self.assertEqual(2, rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
    def test_case_4(self):
        self.assertEqual(3, rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))
    def test_case_5(self):
        self.assertEqual(-1, rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))

if __name__ == '__main__':
    unittest.main()
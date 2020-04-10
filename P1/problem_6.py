import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        cur_head = self.head
        out_string = ''
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    def member(self, value):
        node = self.head
        while node:
            if node.value == value: return True
            node = node.next
        return False
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

def union(llist_1, llist_2):
    new_list = LinkedList()
    for element in llist_1:
        new_list.append(element)
    for element in llist_2:
        new_list.append(element)
    return new_list

def intersection(llist_1, llist_2):
    new_list = LinkedList()
    for element in llist_1:
        if  llist_2.member(element):
            new_list.append(element)
    return new_list

class ListTests(unittest.TestCase):
    def test_member(self):
        empty_list = LinkedList()
        self.assertFalse(empty_list.member(1))
        list_ = LinkedList()
        list_.append(1)
        self.assertTrue(list_.member(1))
    def test_case_1(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()
        element_1 = [3,2,4,35,6,65,6,4,3,21]
        element_2 = [6,32,4,9,6,1,11,21,1]
        for i in element_1:
            linked_list_1.append(i)
        for i in element_2:
            linked_list_2.append(i)
        expected = sorted(element_1 + element_2)
        actual = sorted(union(linked_list_1, linked_list_2))
        self.assertEqual(expected, actual)
        expected = sorted([4,6,6,4,21])
        actual = sorted(intersection(linked_list_1, linked_list_2))
        self.assertEqual(expected, actual)
    def test_case_2(self):
        linked_list_3 = LinkedList()
        linked_list_4 = LinkedList()
        element_1 = [3,2,4,35,6,65,6,4,3,23]
        element_2 = [1,7,8,9,11,21,1]
        for i in element_1:
            linked_list_3.append(i)
        for i in element_2:
            linked_list_4.append(i)
        expected = sorted(element_1 + element_2)
        actual = sorted(union(linked_list_3, linked_list_4))
        self.assertEqual(expected, actual)
        expected = []
        actual = sorted(intersection(linked_list_3, linked_list_4))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
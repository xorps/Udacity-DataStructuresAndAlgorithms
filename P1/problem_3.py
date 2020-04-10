from collections import defaultdict
from heapq import heappop, heappush
import unittest

class Node:
    def __init__(self, value=None, weight=None, left=None, right=None):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.weight < other.weight

def huffman_table(tree):
    table = {}
    def iter(node, acc):
        if node.left: iter(node.left, acc + '0')
        if node.right: iter(node.right, acc + '1')
        if node.value: # its a leaf node
            table[node.value] = acc
    iter(tree, '')
    return table

def huffman_freq(string):
    table = defaultdict(int)
    for char in string:
        table[char] += 1
    return table.items()

def huffman_code(table, string):
    binary_string = ''
    for char in string:
        binary_string += table[char]
    return binary_string

def huffman_encoding(data):
    if not data: return None, None
    freq_table = huffman_freq(data)
    queue = []
    for (value, weight) in freq_table:
        heappush(queue, Node(value=value, weight=weight))
    while len(queue) > 1:
        left = queue.pop()
        right = queue.pop()
        weight = left.weight + right.weight
        heappush(queue, Node(left=left, right=right, weight=weight))
    tree = heappop(queue)
    table = huffman_table(tree)
    encoded = huffman_code(table, data)
    return encoded, tree

def huffman_decoding(data, tree):
    if not data or not tree: return None
    def iter(node, data, acc):
        if node.value:
            if data == '': return acc + node.value
            return iter(tree, data, acc + node.value)
        elif data[0] == '0':
            return iter(node.left, data[1:], acc)
        else:
            return iter(node.right, data[1:], acc)
    return iter(tree, data, '')

class HuffmanTests(unittest.TestCase):
    def test_huffman_freq(self):
        expected = {'a': 1, 'b': 3, 'c': 2, 'd': 5, 's': 6}.items()
        actual = huffman_freq('bcbadcbdsdsdsdsss')
        self.assertEqual(expected, actual)
    def test_coding(self):
        expected = 'sjfwjewlkjdfswjbmwnfkwerisddhh'
        encoded, tree = huffman_encoding(expected)
        actual = huffman_decoding(encoded, tree)
        self.assertEqual(expected, actual)
    def test_coding_empty(self):
        data, tree = huffman_encoding('')
        expected = None
        actual = huffman_decoding(data, tree)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
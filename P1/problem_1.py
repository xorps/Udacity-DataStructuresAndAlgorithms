from collections import OrderedDict
import unittest

class LRU_Cache(object):
    def __init__(self, capacity = 5):
        self.queue = OrderedDict()
        self.capacity = capacity
        self.size = 0
    def _check_capacity(self):
        if self.size < self.capacity: return
        lru = self.queue.popitem(last=False)
        self.size -= 1
    def get(self, key):
        if key not in self.queue: return -1
        value = self.queue[key]
        del self.queue[key]
        self.queue[key] = value
        return value
    def set(self, key, value):
        self._check_capacity()
        if key in self.queue: del self.queue[key]
        self.queue[key] = value
        self.size += 1
    def __repr__(self):
        return self.queue.__repr__()

class LRUTest(unittest.TestCase):
    def test_basics(self):
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(9), -1)
        cache.set(5, 5)
        cache.set(6, 6)
        self.assertEqual(cache.get(3), -1)
    def test_empty(self):
        cache = LRU_Cache(5)
        self.assertEqual(cache.get(0), -1)
    def test_maxsize(self):
        cache = LRU_Cache(3)
        cache.set(1, 3)
        cache.set(3, 5)
        cache.set(9, 2)
        cache.set(12, 4)
        self.assertEqual(cache.get(1), -1)

if __name__ == '__main__':
    unittest.main()
import hashlib
import datetime
import unittest

def timestamp_now():
    now = datetime.datetime.now(datetime.timezone.utc)
    return now.strftime('%X %x')

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.timestamp.encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        sha.update(self.previous_hash.encode('utf-8'))
        return sha.hexdigest()
    def __repr__(self):
        return 'Block(Timestamp: {}, Data: {}, PrevHash: {}, Hash: {})'.format(self.timestamp, self.data, self.prev_hash, self.hash)

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        if self.tail is None:
            self.tail = Node(Block(timestamp_now(), data, '0'))
            self.head = self.tail
        else:
            prev_hash = self.tail.value.previous_hash
            self.tail.next = Node(Block(timestamp_now(), data, prev_hash))
            self.tail = self.tail.next
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

class BlockTests(unittest.TestCase):
    def test_hash(self):
        block_a = Block('one', 'my data', '0')
        block_b = Block('two', 'my data', '0')
        self.assertNotEqual(block_a.hash, block_b.hash)
        block_a = Block('one', 'my data', '0')
        block_b = Block('one', 'my data', '0')
        self.assertEqual(block_a.hash, block_b.hash)
    def test_chain(self):
        chain = BlockChain()
        chain.insert('Block One')
        chain.insert('Block Two')
        chain.insert('Block Three')
        self.assertEqual([block.data for block in chain], ['Block One', 'Block Two', 'Block Three'])
    def test_empty_chain(self):
        self.assertEqual(list(BlockChain()), [])

if __name__ == '__main__':
    unittest.main()
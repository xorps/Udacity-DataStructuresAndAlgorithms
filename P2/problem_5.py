from collections import defaultdict
import unittest

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False
    def insert(self, char):
        return self.children[char]
    def suffixes(self):
        result = []
        for (prefix, child) in self.children.items():
            if child.word: result.append(prefix)
            result.extend(prefix + suffix for suffix in child.suffixes())
        return result

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for character in word:
            node = node.insert(character)
        node.word = True
    def find(self, prefix):
        node = self.root
        for character in prefix:
            if character not in node.children: return None
            node = node.children[character]
        return node

class TrieTests(unittest.TestCase):
    def test_case_1(self):
        trie = Trie()
        for word in ['fun', 'function', 'factory']:
            trie.insert(word)
        self.assertEqual(trie.find('f').suffixes(), ['un', 'unction', 'actory'])

if __name__ == '__main__':
    unittest.main()
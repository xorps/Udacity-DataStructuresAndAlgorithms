# Trie Analysis
### Time Complexity
Trie insert and find are `O(n)` where `n` is the length of the word or prefix or input.
TrieNode insert is `O(1)` as it uses hashmap insertion.
TrieNode suffixes visits every node so its complexity is `O(k)` where `k` is the number of nodes.
### `TrieNode.suffixes()` Space Complexity
We will need `O(k)` stack frames where `k` is the total number of nodes in the trie.
We will also need a `result` of size `O(c)` where `c` is the number of children in trienode for each stack frame.
In total we would need `O(k*c)` for auxiliary space. The input space is remained constant `O(1)`.
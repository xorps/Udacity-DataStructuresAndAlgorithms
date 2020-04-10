# Huffman Analysis
## Introduction
I chose to approach this using a Priority Queue or (min heap). 
Nodes with lowest frequency would be extracted first via `Extract-Min` and combined together with a new weight and reinserted. One node would be left, and using `peak` this would be our huffman tree.
## Time Analysis
### `huffman_table`
This performs a post-order traversal of a tree and performs an `O(1)` insertion into a hash table. This function is `O(n)` as time spent grows linearly with the number of nodes.
### `huffman_freq`
This iterates over a string and performs `O(1)` insertion and lookup on a hashtable. Then calls `O(n)` `dict.items()`. This function is `O(n)`.
### `huffman_code`
This iterates over a string and performs `O(1)` lookups on a table.
This function is `O(n)`.
### `huffman_encoding`
* calls `huffman_freq` - `O(n)`.
* calls `heappush` - `O(log(n))` over a loop, yielding `O(nlog(n))`.
* in a loop, calls `O(log(n))` `heappop` x2, and `O(log(n))` `heappush`
* over time this loop will be converge to `O(nlog(n))`
* another call to `heappop` which is `O(log(n))`
* calls `huffman_table` which is `O(n)`
* calls `huffman_code` which is `O(n)`
* this boils down to `O(n + nlog(n) + nlog(n) + log(n) + n + n) = O(3n + 2nlog(n) + log(n)) = O(n + nlog(n) + log(n)) = O(n(1 + log(n)) + log(n)) = O(nlog(n) + log(n)) = O(log(n)(n + 1)) = O(nlog(n))`
### `huffman_decoding`
This performs a binary search on a complete binary tree `O(log(n))`. This avoids worst case scenario of `O(n)` time.
## Space Analysis
### `huffman_table`
Increases in size linearly with input: `O(n)`
### `huffman_freq`
Increases in size linearly with input (albeit doubled): `O(2n) = O(n)`
### `huffman_code`
Increases linearly with size of input: `O(n)`
### `huffman_encoding`
Increases and returns 2 objects that grow linearly with respect to input: `O(n)`
### `huffman_decoding`
Builds a string that increases linearly with respect to input: `O(n)`
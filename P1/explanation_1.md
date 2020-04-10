# LRU Analysis
## Introduction
I decided to use a FIFO Queue to keep track of what values were used in order.
I would have to remove items that were used and re-insert them back in as they were used to prevent duplicates and to prevent recently used items from being truncated by capacity.
This would also mean the LRU or least recently used items would trend to the front of the queue.
I chose a doubly linked list for the data structure of the FIFO Queue.
Doubly linked lists provide constant insertion time and constant removal time.
Unfortunately, Doubly linked lists do not provide constant search time, but linear search time.
I decided to add another data structure, the hash table to provide constant search time.
The hash table would maintain a reference to the node associated by the key.

## Time Complexity
### `LRU_Cache.get`
This method uses `OrderedDict` which has `O(1)` insertion and removal.
### `LRU_Cache.set`
THis method uses `OrderedDict` which has `O(1)` insertion and removal.
## Space Complexity
### `LRU_Cache.get`
The space size does not change. `O(1)`.
### `LRU_Cache.set`
This can cause an insertion of a new item if the key does not exist, and we are below max capacity, so worst case `O(n)`.
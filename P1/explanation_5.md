# Block Chain Analysis
## Introduction
Using a double ended singly linked list to represent a block chain.
## Time Complexity
### `BlockChain.insert`
This has `O(1)` insertion, ignoring the cost of hashing and timestamps.
### `BlockChain.__iter__`
This runs in `O(n)` where `n` is the number of blocks.
## Space Complexity
### `BlockChain.append`
Space grows linearly with size of input: `O(n)`.
### `BlockChain.__iter__`
This uses a generator, and the space does not grow, we could say `O(1)`.
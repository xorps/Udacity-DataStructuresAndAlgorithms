# `find_files` Analysis
## Introduction
I initially thought about using a recursive approach but [Python does not support tail call optimization][1], which means deep directory hierarchies would cause a stack overflow. I chose a python list to hold the next paths to search and another list to hold files that were discovered. If order matters we could also use a FIFO queue with a bread first search approach or depth first search as needed.
## Time Complexity
The best case is `O(n)` where there are no subdirectories to search.
If we let `n` be the number of files, and `m` be the number of directories, we could say approximately the time complexity would be `O(n*m)` since for each subdirectory we need to perform a linear search.
## Space Complexity
If we let `n` be the number of paths that fit our criteria, we could say our space complexity is `O(n)` as the space grows linearly to the number of files that match our criteria.

[1]: http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
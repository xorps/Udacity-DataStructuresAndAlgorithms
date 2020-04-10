# `rotated_array_search` Analysis
I wasn't quite sure how to approach this so I looked at this in sub problems. If there was a sorted slice in the list, I could just use a binary search if the number was in range, otherwise I could remove this slice from the input space, and continue the problem with the rest of the input space.
### Time Complexity
As the input is continuously divided in half, I'd expect the performance to be `O(log(n))`.
Where `n` is the length of `input_list`.
|   n   | iterations |
| ----- | ---------- |
| 100   | 1          |
| 500   | 6          |
| 1000  | 7          |
| 10000 | 9          |
| 100000| 14         |
### Space Complexity
The space used for the input is `O(n + 1)` where `n` is the length or size of `input_list`.
There are three local variables of total size `O(3)`. Their size never change.
Total space required: `O(n + 4)` or `O(n)`.
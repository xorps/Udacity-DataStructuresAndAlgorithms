# `rearrange_digits` Analysis
### Time Complexity
As we already know [`mergesort` has `O(nlog(n))`][1] sorting complexity which is why I chose it for this problem.
After `input_list` is sorted, I do a `O(n)` traversal to make the two numbers.
In total we have `O(nlog(n) + n) = O(n(log(n) + 1)) = O(nlog(n))`.
### Space Complexity
[Merge sort has `O(n)` space complexity][1] in addition to the three more local variables that we need that do not change in size: `O(3)`.
We have `O(n + 3)` or simply `O(n)`.

[1]: https://en.wikipedia.org/wiki/Merge_sort
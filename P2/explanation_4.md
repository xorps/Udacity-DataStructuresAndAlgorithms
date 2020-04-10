# `sort_021` Analysis
### Time Complexity
This function iterates over each element in `input_list` and appends it to another one -- list.append is `O(1)`.
At the end the lists are combined in `O(n)` time.
The time complexity is `O(n)` where `n` is the number of elements in `input_list`.
### Space Complexity
The input is of space `O(n)` where `n` is the number of elements in `input_list`.
We have a local variable `acc` that grows to the maximum space of `O(n)` -- the space of `input_list`.
We have another local variable `n` where the space is `O(1)` and does not grow.
At the end we require `O(n)` space to combine `acc`.
Note that `O(acc[0]) + O(acc[1]) + O(acc[2]) <= O(input_list)` holds true for the duration of the function.
The space complexity is `O(n + n + 1 + n)` or simply `O(n)`.
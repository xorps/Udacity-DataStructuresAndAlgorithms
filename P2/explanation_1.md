# `sqrt` Analysis
To solve this problem I decided to use the [Babylonian method][1] to approximate the square root.
### Time Complexity
I made a table and graphed its inputs to see that it had `O(log(n))` behaviour.
| number | iterations |
| ------ | ---------- |
| 0      | 1          |
| 1      | 2          |
| 2      | 1          |
| 3      | 1          |
| 4      | 1          |
| 6      | 2          |
| 7      | 2          |
| 12     | 3          |
| 20     | 3          |
| 30     | 4          |
| 61     | 5          |
| 143    | 6          |
| 499    | 6          |
### Space Complexity
This function requires 1 variable for input and 2 local variables to keep track of state. The local variables do not change in size. `O(1)`.

[1]: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
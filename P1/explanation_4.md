# Active Directory Analysis
## Introduction
I chose python's deque which provides a FIFO queue, so I can search groups in a breadth first search manner.
## Time Complexity
### `is_user_in_group`
In worst case every group and its users will be explored.
Time to search will increase as the numbers of groups and users increase.
We could say `O(u + g)` where `u` is the number of users and `g` is the number of groups. 
## Space Complexity
### `is_user_in_group`
The function keeps state in a queue that holds a *frontier* of groups to explore. We could say the space increases as the number of groups increases where `g` is the number of groups. `O(g)`.
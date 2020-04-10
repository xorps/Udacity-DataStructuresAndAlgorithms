# Lists Analysis
Using singly linked list.
## Time Analysis
### `member`
Performs a linear search, runs in `O(n)` time.
### `union`
Constructs a new list, iterating over list and appending each element.
Runs in `O(n^2)` time as append is linear.
### `intersection`
Constructs a new list, iterating over the first let and only adding elements if its a member of the second list.
Runs in `O(n^2)` time as member is linear and append is linear.
## Space Analysis
### `member`
This does not change in space. `O(1)`.
### `union`
Creates a new list of the size of both inputs. `O(n)`.
### `intersection`
Creates a new list of members from the first list if they are members of the second. The space grows linearly in respect. `O(n)`.
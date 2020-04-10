# `Router` Analysis
## Time Complexity
### `Router.add_handler`
* calls `split_path` which is `O(n)` where `n` is the number of paths to create, `k` is omitted since `k` is constant -- `/`.
* calls `RouteTrie.insert` which has `O(n)` insertion where `n`n is the number of paths.
* Conclusion: `O(n)`.
### `Router.lookup`
* calls `split_path` which is `O(n)` where `n` is the number of paths
* calls `RouteTrie.insert` which is `O(n)` where `n` is the number of paths.
* Conclusion: `O(n)`.
## Space Complexity
### `Router.split_path`
* calls `str.split` where new space is allocated of `O(n)` where `n` is the number of paths.
* creates a new array of `O(k)` where `k` is the number of paths that are not empty.
* Note: `k <= n`.
* At the end of the function we will be left with `O(k)` auxiliary space for worst case.
* Input space is `O(c)` where `c` is the length of path.
* Total space is `O(c + k + n)`.
### `Router.add_handler`
* calls `split_path` which will take `O(p)` auxiliary space where `p` is the number of paths.
* calls `RouteTrie.insert` which will at worst case add a new node for each `p`, so `O(p)`.
* Total space is `O(1 + 2p)` where `O(1)` is the input space and `O(2p)` is the auxiliary space.
* Conclusion: `O(p)`.
### `Router.lookup`
* This is the same as `Router.add_handler` only we are not allocating any new nodes.
* So we have `O(1 + p) = O(p)` for total space complexity.

Binary Search Tree
==================
A balanced complete binary tree used to support searching.


Overview
--------
Maintains the invariant that for every node, the value is > all left children and <= all right children.


Operations
----------
insert(val)
remove(val)
find(val)



Traversal
---------
Refers to strategies for iteratively visiting nodes.

# In-order
For each node, left child is printed first, then current node, then right child.

# Pre-order
For each node, it is printed first, then the left child, then the right child.

Post-order
# For each node, left child is printed first, then right child, then current node

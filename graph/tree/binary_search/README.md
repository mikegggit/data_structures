Binary Search Tree
==================
A binary tree used to support searching.


Overview
--------
Each node has a key and a value.

Maintains the invariant that for every node, the key is > all left children keys and <= all right children keys.

Nodes are organized according to their keys.


Operations
----------
insert(val)
remove(val)
removeMin()
removeMax()
find(val)
max()
min()


Traversal
---------
Refers to strategies for iteratively visiting nodes.

# In-order
For each node, left child is printed first, then current node, then right child.

# Pre-order
For each node, it is printed first, then the left child, then the right child.

Post-order
# For each node, left child is printed first, then right child, then current node


Analysis
--------
The performance of certain operations is O(h), where h is the height of the BST.

Not necessarily balanced.  

An unbalanced tree leads to worst case performance of some operations approaching O(n).

For improved performance and a more balanced tree, at the expense of a more complex implementation, use AVL and Red / Black trees.
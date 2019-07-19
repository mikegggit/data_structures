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
contains(val)
max()
min()
findNextLargest(val)
findNextSmallest(val)

Traversal
---------
Refers to strategies for iteratively visiting nodes.

# In-order
For each node, left child is printed first, then current node, then right child.

# Pre-order
For each node, it is printed first, then the left child, then the right child.

Post-order
# For each node, left child is printed first, then right child, then current node


Removal
-------
Removing nodes in a BST is non-trivial.



Implementation
--------------
Handling root deletion seems to require use of a wrapper class to store reference to the root node.

Clients need to see changes to the root, hence a wrapper class.


Analysis
--------
The performance of certain operations is O(h), where h is the height of the BST.

Not necessarily balanced.  

An unbalanced tree leads to worst case performance of some operations approaching O(n).

A BST is most unbalanced when nodes are almost sorted.

For improved performance and a more balanced tree, at the expense of a more complex implementation, use AVL and Red / Black trees.

BST is most efficient when the tree is balanced.

insert(val) -> O(N)
	Worst case, nodes are inserted in sorted order, leading to a high tree.  
remove(val) -> O(N)
	Worst case scenario, nodes were stored in sorted order, leading to a high tree.  
	To delete, need to first find the node to delete, then...
		
		If...
		...no children, remove node
		...one child, replace node to be removed w/ the child
		...two children, replace node to remove w/ next successor (??? or predecessor???)

find(val) -> O(N)
	See insert.


Red Black tree
==============
A balanced binary search tree.

A node and it's parent are considered adjacent, as are a node and it's direct children.

All leafs are Null nodes.

All Null nodes are black.

Every node is either Red or Black.

Invariants
----------
* Root property
  Root is always black.

* Red property
  If a node is Red, than both its children are black    
  No two adjacent nodes can both be red.    

* Black property
  The number of black nodes along any path from one node to a descendant Null node is the same.

The path from root to the leaf farthest from the root is not more than twice as long as the path from root the the leaf nearest the root.



Black height
------------
The invariant number of black nodes along all paths from root to any leaf.


ADT
---
insert node
find value
delete node
print in order


Implementation
--------------
Each node carries an extra bit of information denoting its color.

Leaf nodes contain no data

Inserts and deletes break the RB tree invariants, requiring an associated fixup step.

Insert
Insertion node is always red.

If the parent of the inserted node is black, we're done.

Otherwise:

	You have to either color switch, or rotate.

	Determine the action by evaluating the uncle of the insertion node, or in other words, the parent's sibling.

	If red, color flip, otherwise rotate.

	Null nodes are considered when determining the uncle (parent's sibling).  For example...

	    3

	  /    \

	1        5
	        
	           \

	             7

	           /

	         6

	The uncle of 6 is a black Null        


### Color flipping
Flip the parent (and uncle if not not Null).

Flip grandparent if not root.

Recursively check for invariant validation starting @ grandparent

### Rotations
Do colors change as a part of rotating?

Left

Left -> Right
Refers to a left rotation followed by a right rotation

Right

Right -> Left
Refers to a right rotation followed by a left rotation

Analysis
--------
Balancing is good enough, meaning it isn't perfect, but good enough to maintain O(Log(n)) complexity of insert / delete operations.

Comparison to AVL trees
-----------------------
AVL trees are more strictly balanced than RB trees.

To maintain the more restrictive balancing invariants, more rotations are required.

As a result, RB trees are often preferred where lots of insertions / deletions occur.


Usage
-----

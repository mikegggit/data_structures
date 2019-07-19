B tree
======
Self balancing tree structure that maintains sorted data and supports logarithmic operations.

Summary
-------
Generalization of a BST in that nodes can have more than two children. 

Each node has a set of keys establishing the ranges of it's children.

A node having two children will have a single key.
 - All nodes in the left subtree will have values less than the key, those in the right greater than the key.

 

A node having three children will have two keys, etc.



Invariants
----------
Internal nodes are defined as able to have children of data with a pre-defined range.


Data associated w/ children of any particular node must 

Why useful?
-----------
Supports use cases where data is read / written in blocks.

Requires less work to maintain invariants by virtue of the fact that a node may have more than two children within a range of values.

May require more memory by virtue of the fact that nodes pre-allocate memory for not yet established data.


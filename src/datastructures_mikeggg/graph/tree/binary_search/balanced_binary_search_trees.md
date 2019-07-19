Balanced Binary Search Trees
============================
Binary search trees ensure O(log(n)) performance and avoid O(n) worst-case performance that can happen with an unbalanced tree.

Types
-----
* AVL
* Red-Black tree

Why balanced?
-------------
To minimize the height of the tree.  

Most BST operations have complexity proportional to the tree height.

To illustrate the problem, consider a simple BST whose nodes are sourced from a sorted list.  The resulting tree will be a linked list of size N, and height N.


Self balancing
--------------
Property of a BST where the height is minimized as a function of node insertion / deletion.


Rotation
--------
A node restructuring operation whereby in-order node traversal before the rotation is maintained afterwards.  

Usage
-----
Use a red-black tree when insert / delete operations outweigh search operations, otherwise AVL.

Implementation
-------------


Red-black tree
--------------
Less performant insert / delete operations than an AVL tree.  May involve more rotations on insert / delete than in the case of an AVL tree.


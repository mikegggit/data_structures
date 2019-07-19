Heap
====
An almost complete balanced binary tree that satisfies the heap invariant.


Heap invariant
--------------
Depending on whether the heap is a min / max heap, for each node with children, the value of the node is greater then or equal to the value of each child.


Operations
----------
insert(val)
min()
removeMin()
size()
height()

Internal operations include: 
 - heapify - Processes structure to establish heap invariant
 - heapifyUp(node) - 
 - heapifyDown(node)
 - getParent
 - getChildren


Uses
----
A heap can be used to implement a priority queue, in which the highest priority item is to be repeatedly removed from a collection.



Implementation
--------------
Data is typically stored in an array instead of a structure using pointers.

The use of an array yields a space efficient solution.

Values in the array are stored in order of in-order traverssal.

For a given node at array index i, it's child nodes can be found at 2i and 2i + 1.  

Given it is implemented as a complete binary tree, it's max height is log(n)


Analysis
--------
Not a sorted structure.

Being a balanced tree, it supports log(n) operations.

Always has h of log(n).

Suffers from no worst-case quadratic issues sorting like quicksort.

The typical implementation using a binary tree implemented using an array has max height log(n).

There is no implied ordering for in-order traversal.


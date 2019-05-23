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


Uses
----
A heap can be used to implement a priority queue, in which the highest priority item is to be repeatedly removed from a collection.



Implementation
--------------
Data is typically stored in an array instead of a structure using pointers.

The use of an array yields a space efficient solution.



Analysis
--------
Not a sorted structure.

Being a balanced tree, it supports log(n) operations.

Always has h of log(n).




Stack
=====
A data structure that supports orderly insertion and removal in O(1) time.

Overview
--------
Similar to a queue but different:
 - supports LIFO insertion / removal
 - insertion / deletion occurs at one end of the structure

Like a queue, a linear structure.


Operations
----------
push(el)
pop()
size()
peek()
isFull()


Analysis
--------
Insertions and deletions are O(1)
Search is O(n)


Implementation
--------------
Like queues, are commonly implemented with either an array or linked list.


Use cases
---------
Items are popped in the reverse order they were inserted.

Used to support LIFO insertion / removal.

Maintains original entry order.
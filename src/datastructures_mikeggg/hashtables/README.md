Slot
----
Also called a key.

The goal of a hash function is to map an item into a slot, or key.


Number of slots
---------------
The more slots you have, the more memory you need.



Hash function
-------------
The function that assigns an item to a slot.

Good hash function
------------------
Easy to compute.

Distributes values evenly amongst slots.

Minimizes collisions.


Load factor
-----------
The percent of slots in a hashtable containing at least one item.

Collision
---------
More than one item are assigned the same slot by a hash function.

The more collisions there are, the worse the performance.

Minimizing collisions requires a combination of more slots and a good hash function.



Common hash functions
---------------------

### Remainder method
Divide an item's hash value by the number of slots.

### Perfect
Assigns each item to a unique hash value.

Difficult to create without knowing beforehand the items to be hashed.

One way to achieve is to have as many slots as the largest possible value -> requires
  a large amount of memory.

### Folding method
Divide the item into equal size pieces (last piece may not be equal).

Add the pieces together and mod by number of slots.

Some impl's perform additional modification of the pieces, or every other piece, before adding.

1234567 -> 12 34 56 7 -> 12 43 56 7 -> 118 -> 118 % 11 slots -> 8

### Mid square
Square each item.  If the resulting value is even, take middle 2 digits, else 1 digit, and mod by # slots.


Common hash function problems
-----------------------------
### Anagrams
Function that doesn't treat items containing same components arranged differently.

A bad hash function would assign cat and act to the same slot -> add ordinals of each letter and mod by # slots -> BAD

A better function would consider the position of each character, for example, by multiplying the ordinal by the char
  position.

### Complex
A hash function that is too complex will end up dominating the complexity and make the process of calculating the
  slot more work than simply performing a sequential / binary search for the item.


Collision Resolution
--------------------
Handing case where a hash function assigns an item to an already occupied slot.

### Open Addressing
Given a collision, sequentially check adjacent slots until an open one is found.

May introduce clustering given a hash function and data set that results in certain slots being assigned more often.

To reduce clustering, can check non-sequentially, for example, every third slot for an empty one.

The process of finding an empty slot in the event of a collision is called rehashing.  


### Chaining
Support storing more than one item in each slot.

When a collision is found, just add the item to the end of the slot array.



Discussion
----------
Hashtables provide indexed access to data based on a numeric representation of its data.

The benefits of storing data in a hashtable are:
 - search performance approaching O(1) time.

A good implementation has these properties:
 - takes into account the data to be stored
 - minimizes collisions



To minimize the number of collisions, determine a hash function that generates a good 
distribution of values across slots.

Values are assigned a slot by applying an indexing function to a hash value.  A simple indexing 
function mods the hash value by the number of slots.

A hashtable has a certain number of slots.  To minimize the number of collisions, choose a 
hashtable size that is a prime number.

A good hash function requires some knowledge of the data being hashed.



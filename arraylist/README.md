ArrayList
=========
A resizable list.

Operations
----------
add(el)
addAt(i, el)
remove()
removeAt(i)
size()
contains(el)

Analysis
--------
add(el)
  Adds to the end of the list in O(1).  
  Doesn't require shifting elements to the right

addAt(i, el)
  Worst case O(n) if el if i is in beginning of array.
  Requires shifting el's to the right.
  Doesn't replace

remove()
  O(1) since element being removed is at end of array
  No shifting of el's is required

removeAt(i)
  O(n) worst case if element to remove is at beginning of the array

contains(el)
  O(n) since we may have to scan all el's of the array
 
Amortized across all resizing, the cost of resizing is O(1).  


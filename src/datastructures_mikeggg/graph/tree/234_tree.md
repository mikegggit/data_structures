2-3-4 Tree
==========
A self balancing tree data structure.


ADT
---
Insert

Delete

Search


Invariants
----------
Every node is either a 2, 3 or 4 node.

All external nodes are at the same depth.

All data is in stored in sorted order

	

Structure
---------
### Internal node
Internal nodes are nodes that have children.

Every internal node has either 2, 3, or 4 child nodes.

### External node
Nodes without children

All external nodes are at the same depth

2 node - has one data element, and if internal, two children
3 node - has two data elements, and if internal, three children
4 node - has two data elements, and if internal, four children


Relationship to B-trees
-----------------------
2-3-4 trees are B-trees with order 4.


Relationship to RB trees
------------------------
May be more difficult to implement than rb trees due to the number of special cases needed to be handled.

Rb trees are simpler to implement


Analysis
--------
All of insertion, delete and search operations are O(log(n))
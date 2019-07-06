Graphs
======
Reference-based non-linear structure that defines relationships between vertexes.

Background
----------

### Vertex 
A node which may or may not be associated with other vertex(es).  

In a connected graph, every vertex is associated with at least one other vertex.

The degree of a vertex is the number of adjacent vertices associated with the vertex.  A loop is counted twice towards degree.  Degree can be considered the number of lines touching the vertex.


### Edge
An association between two vertices, or in the case of a loop, just one.  

May be either ordered (directed) or unordered (undirected).

Arc - Directed edge

Directed edges are considered ordered, as a -> b means something else from b -> a.

### Path
A sequence of vertices connected by edges with no duplicate edges.

### Cycle
A path in a directed graph starting and ending at the same node.

An acyclical graph is one in which it is impossible to arrive back at the starting node while navigating along edge between vertices.

### Tree
An acyclic connected graph.

### Connected graph
There is at least one path from every vertex to every other vertex.

### Subgraph
A subset of a graph's edges (and related vertices) representing a graph.

### Root
Relevant to trees, which are a type of acyclical undirected graph.

### Spanning tree
Relevant to a connected graph.

A subgraph of a connected graph.

Contains all the vertices of a given subgraph.

Is a tree.

### Leaf
Relevant to trees


Operations
----------
The Graph ADT has these operations:

* addVertex(a)
* removeVertex(a)
* addEdge(a, b)
* removeEdge(a, b)
* adjacent(a, b)
* neighbors(a)
* getVertexValue(a)
* getEdgeValue(a, b) <- if edges hold values


Classification
--------------
### Directed / Undirected

### Cyclical / Acyclical

### Connected / Unconnected

### Weighted / Unweighted edges

### Allowing parallel edges
Parallel edges refers to multiple edges incident on the same two vertices.
Can be allowed for both directed and undirected graphs.
A graph with parallel edges is called a multigraph.

Parallel edges require using storing adjacent nodes in a structure that supports duplicates.  

### Allowing loops
A loop is an edge incident on a single vertex.

### Sparse / Dense
A sparse graph contains few edges relative to the number of vertices.

A dense graph can be considered one having edges >= V^2.



Representations
---------------
The ordering of vertices in either representation is unimportant aside from possibly printing.

A concern is how a vertex is represented in the structure.

One possibility is to use an index representation of the vertex, thus associating each vertex with a unique numeric index.  It is an implementation detail how vertices with non-numeric labels are mapped to a numeric index.

Another possibility is to maintain the vertex label as the identifier, treating the label as a hash key.  Using a python dictionary to store vertexes as keys is an example.

Storing the vertex as a indexed manner (whether a hashtable or indexed array) is important to avoid having to search for vertices / edges.


### Adjacency list

Space complexity is O(V + E)
Generally preferred over matrix.  Most graphs are sparse.

Refers to an array of lists, with the vertex stored in the array index of the same id, and adjacent nodes (edge targets) stored in the list under that index.

Using a list to store adjacent vertexes allows parallel edges.

#### Pros
Avoids storage penalty for sparse graphs.
Allows storing vertex / edge info internally.
Fast retrieval of all edges incident on a given vertex.
Easier to add vertexes

#### Cons
Requires more time than a matrix representation to determine whether a specific edge from vertex A to B exists.



### Matrix
Space complexity of O(V^2).

Traditionally implemented as a 2D array.

Presence of an edge between two vertices is represented by a non-zero or non-false value in the 2d entry.

Undirected matrixes are symetric.

Adding vertices where an array is being used to store vertices as opposed to a hashtable or similar requires either growing the component array's or pre-allocating larger arrays. 

#### Pros
Preferred to adjacency list impl when it's important to quickly determine whether a certain edge exists.

#### Cons
* Storage
If using an array structure, Wasted storage for sparse graphs (few edges).

Using a hashtable to map src / dest vertices can avoid the need to allocate memory for unused slots.

* Doesn't allow parallel edges.





Analysis
--------
In many cases, complexity depends on how the graph is represented.


* __addVertex(a)__

    Adjacency list: O(1).  Simply adds an empty adjacency list to a new array index.  

    Matrix: Adding vertices to a matrix may be expensive depending on whether or not the matrix needs to grow and a new matrix is being created and copying done.

    If the matrix requires resizing, O(V^2).  Create new arrays of twice the size, For each vertex in each source array, copy the entry from the original matrix. Finally add the new entry.

# removeVertex(a)
    Adjacency list: O(V + E).  For each Vertex, you need to traverse its adjacency list to see whether any edges from that vertex to vertex being removed exists.  

    Matrix: O(E)

Matrix:

* addEdge(a, b)
    Adjacency list: O(1)

    Matrix: O(1)

* removeEdge(a, b)
    Adjacency list: O(V + E).  Visits each vertex, then traverses each adjacency list searching for edges to remove.

    Matrix: O(1). Remove the entry in (a, b), and (b, a) if undirected.

* adjacent(a, b)
    Adjacency list: O(V).  Visit the source list and search the adjacency list for b.  O(V) since there are at most V-1 edges to search through

    Matrix: O(1). Return value of (a, b)

* neighbors(a)
    Adjacency list: O(1).  returns all entries in adjacency list for a.  O(1) since this is just returning the adjacenty list stored for a.

    Matrix:  O(V) For entry a, need to travers all possible adjacents (vertices) to find those having a value of 1.  O(V) since there at most V-1 possible vertices to search.

* getVertexValue(a)
	Adjacency list: O(1)

	Matrix: O(1)

Matrix:
* getEdgeValue(a, b) <- if edges hold values
	Adjacency list: O(E). Need to find vertex a, then visit each adjacent vertex.

	Matrix: O(1)

### Storage
Matrixes are space inefficient for sparse graphs (graphs where a relatively large percent of vertex pairs have no association).


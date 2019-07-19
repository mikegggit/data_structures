#!/usr/bin/python

class GraphM:
  """Undirected graph represented by an 2d dictionary, allowing vertex labels to be
  treated like array indexes.  Being an undirected graph, the graphical representation
  ends up being symmetric.

  As written, doesn't support parallel edges or loops.
  """

  # The 2d matrix, implemented as a 2d dictionary
  m = {}
  
  def addEdge(this, a, b):
    """
    Complexity O(1).
    """
    if not a in this.m:
      this.m[a]={b:1}
    else:
      this.m[a][b] = 1

    if not b in this.m:
      this.m[b] = {a:1}
    else :
      this.m[b][a] = 1

  def removeEdge(this, a, b):
    """
    O(1).
    """
    if a in this.m and b in this.m[a]:
      this.m[a][b] = 0

    if b in this.m and a in this.m[b]:
      this.m[b][a] = 0

  def addVertex(this, v):
    """
    We're essentially using a hashtable, so depending on how implemented, any of these
    operations might trigger resizing.   

    On an amortized basis, the complexity is O(1), although any one add could trigger a resize of O(V). 
    """
    if v in this.m:
      return

    this.m[v] = {}

  def removeVertex(this, v):
    """
    O(V + E).  
    """
    if v in this.m:
      this.m.pop(v)

    for r in this.m:
      if v in this.m[r]:
        this.m[r].pop(v)
    
  def vertices(this):
    return [k for k in this.m.keys()]

  def adjacent(this, a, b):
    """Tests whether or not there is an edge between a and b.

    Returns False if a and b refer to the same node (loop).

    O(1).  Faster than an adjacency list impl.
    """
    return a in this.m and b in this.m[a] and this.m[a][b] == 1

  def neighbors(this, a):
    """Returns all neighbors of a.  In other words returns vertices on other end of edges associated w/ a.
   
    O(V).  Requires iterating over all members of a's adjacency list.  More expensive than an adjacency list.
    """
    return [ n for n, v in this.m[a].items() ]

     
  def printGraph(this):
    """
      A B C D E F
    A 0 0 1 0 0 0
    B 0 0 1 0 1 0 
    C 1 1 0 1 1 0 
    D 0 0 1 0 0 0
    E 0 1 1 0 0 0 
    F 0 0 0 0 0 0
    """
    print(this.m["B"]["C"])    
    # print x axis
    print("  " + "".join(["{:2}".format(k) for k in this.m.keys()]))

    # print y axis and rows
    print("\n".join([v + " " + " ".join([str(this.m[v][w]) if w in this.m[v] else str(0) for w in this.m.keys()]) for v in this.m.keys()]))
      
if __name__ == "__main__":
  g = GraphM()

  """
  A     B
   \   /|
    \ / |
     C  |   F
    / \ |
   /   \|
  D     E
  """
  g.addEdge("A", "C")
  g.addEdge("D", "C")
  g.addEdge("C", "B")
  g.addEdge("C", "E")
  g.addEdge("B", "E")
  
  print(g.vertices())

  g.addVertex("F")

  print(g.vertices())
  g.printGraph()

  assert not g.adjacent("A", "F") 
  assert g.adjacent("A", "C") 
  assert g.adjacent("C", "A") 
  assert not g.adjacent("C", "C") 

  print(g.neighbors("C"))

  g.removeVertex("A")
  g.printGraph()

  assert g.adjacent("B", "C")
  g.removeEdge("B", "C")
  assert not g.adjacent("B", "C")
  g.printGraph()

  g.addVertex("A")
  g.printGraph()
  g.addVertex("G")
  g.printGraph()

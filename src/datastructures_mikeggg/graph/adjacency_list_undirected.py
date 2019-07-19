#!/usr/bin/python


class GraphAL():
  """An undirected graph.
  
  Models vertices as dictionary keys.

  Adjacent nodes (edges) are modeled as entries in an adjacency set.

  An adjacency set prevents having multiple edges between two nodes.

  Each edge is represented twice, in each vertex's adjacency set.
  """
  m=None

  def __init__(this):
    this.m = {}

  def addVertex(this, v):
    """
    O(1)
    """
    if not v in this.m:
      this.m[v] = set()

  def removeVertex(this, v):
    """ 
    O(V + N)
    Deletes the vertex and associated adjacency list.

    Since undirected, traverses each other vertex and removes edges incident to vertex being removed 
    """
    this.m.pop(v)
    for a in this.m.values():
      print(type(a))
      if v in a:
        a.remove(v)

  def addEdge(this, a, b):
    """
    O(1)
  
    Registers undirected edge with both vertex a and b
    """
    if not a in this.m:
      this.m[a]=set()
    this.m[a].add(b)
    if not b in this.m:
      this.m[b]=set()
    this.m[b].add(a)

  def adjacent(this, a, b):
    """
    O(V) since there are up to V-1 possible edges that will need to be looked through
    to determine whether or not b is incident to a.
    """ 
    if not a in this.m:
      return False
    return b in this.m[a]

  def vertices(this):
    return [k for k in this.m.keys()]

  def printEdges(this, n):
    for t in this.m[n]:
      print("Edge [v1={}, v2={}]".format(n, t))

  def print(this):
    for i, j in this.m.items():
      print("{} => {}".format(i, ("None" if len(j) == 0 else j)))

if __name__ == "__main__":
  g = GraphAL()

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
  g.addEdge("B", "C")
  g.addEdge("C", "E")
  g.addEdge("B", "E")

  g.print()
  print(g.vertices())
  g.printEdges("C")

  g.addVertex("F")
  print(g.vertices())
  g.print()

  assert g.adjacent("A", "C")
  assert not g.adjacent("A", "B")
  assert g.adjacent("C", "D")
  assert not g.adjacent("F", "E")
  assert g.adjacent("E", "B")

  g.removeVertex("C")

  g.print()
  assert not g.adjacent("A", "C")
  assert not g.adjacent("C", "D")

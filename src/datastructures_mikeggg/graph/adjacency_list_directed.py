#!/usr/bin/python


class GraphAL():
  """An directed graph.
  
  Models vertices as dictionary keys.

  Adjacent nodes (edges) are modeled as entries in an adjacency set.

  An adjacency set prevents having multiple edges between two nodes.
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
    O(V + E)

    V to iterate over every vertex.

    E to iterate over every adjacency list.

    Here, we're simply removing the vertes and hence leaving it to the runtime to free the memory.
    """
    this.m.pop(v)
    for a in this.m.values():
      if v in a:
        a.remove(v)

  def addEdge(this, a, b):
    """
    O(1)
  
    Registers directed edge with only a.
    """
    if not a in this.m:
      this.m[a]=set()
    this.m[a].add(b)

  def adjacent(this, a, b):
    """
    O(V) since there are up to V-1 possible edges that will need to be looked through
    to determine whether or not b is incident to a.
    """ 
    if not a in this.m:
      return False
    return b in this.m[a]

  def neighbors(this, a):
    """
    O(1)
    """
    if not a in this.m:
      return None
    return this.m[a]

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
 
  assert set(["C", "E"]) == g.neighbors("B")

  g.addVertex("F")
  print(g.vertices())
  g.print()

  
  assert g.adjacent("A", "C")
  assert not g.adjacent("A", "B")
  assert g.adjacent("D", "C")
  assert not g.adjacent("C", "D")
  assert not g.adjacent("F", "E")
  assert g.adjacent("B", "E")
  assert not g.adjacent("E", "B")

  g.removeVertex("C")

  assert set(["E"]) == g.neighbors("B")
  g.print()
  assert not g.adjacent("A", "C")
  assert not g.adjacent("C", "D")

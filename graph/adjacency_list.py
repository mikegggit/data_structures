#!/usr/bin/python


class GraphAL():
  """An undirected graph.
  
  Models vertices as dictionary keys.

  Adjacent nodes, and hence edges, are modeled as entries in an adjacency set.

  An adjacency set prevents having multiple edges between two nodes.

  Each edge is represented twice, in each vertex's adjacency set.
  """
  v=None

  def __init__(this):
    this.v = {}

  def addVertex(this, n):
    if not n in this.v:
      this.v[n] = set()

  def addEdge(this, a, b):
    """Registers undirected edge with both vertex a and b"""
    if not a in this.v:
      this.v[a]=set()
    this.v[a].add(b)
    if not b in this.v:
      this.v[b]=set()
    this.v[b].add(a)
 
  def vertices(this):
    return [k for k in this.v.keys()]

  def printEdges(this, n):
    for t in this.v[n]:
      print("Edge [v1={}, v2={}]".format(n, t))

  def print(this):
    for i, j in this.v.items():
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
  """
  g.addVertex("A")
  g.addVertex("B")
  g.addVertex("C")
  g.addVertex("D")
  g.addVertex("E")
  g.addVertex("F")
  """

  print(g.vertices())

  g.addEdge("A", "C")
  g.addEdge("D", "C")
  g.addEdge("B", "C")
  g.addEdge("C", "E")
  g.addEdge("B", "E")

  print(g.vertices())
  g.printEdges("C")

  g.addVertex("F")
  print(g.vertices())
  g.print()

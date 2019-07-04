#!/usr/bin/python

class GraphM:
  """Graph represented by an 2d dictionary, allowing vertex labels to be
  treated like array indexes.

  As written, doesn't support parallel edges
  """

  m = {}
  
  def addEdge(this, a, b):
    if not a in this.m:
      this.m[a]={b:1}
    else:
      this.m[a][b] = 1

    if not b in this.m:
      this.m[b] = {a:1}
    else :
      this.m[b][a] = 1

  def addVertex(this, v):
    if v in this.m:
      return

    this.m[v] = {}

  def vertices(this):
    return [k for k in this.m.keys()]

  def printGraph(this):
    """
     ABCDEF
    A001000
    B001010
    C110110
    D001000
    E011000
    F000000
    """
    # print x axis
    print(" ", end="")
    for i in this.m.keys():
      print(i, end="")
    print("")

    # print y axis and rows
    for v in this.m.keys():
      print(v, end="")
      al = this.m[v]
      for w in this.m.keys():
        print(1 if w in al else 0, end="")
      print("")
 
      
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


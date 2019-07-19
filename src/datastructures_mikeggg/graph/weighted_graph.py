#!/usr/bin/python

class Graph:
  """ Implementation of a weighted undirected graph """
  m = None

  def __init__(this):
    this.m = {}

  def addEdge(this, a, b, w):
    if not a in this.m:
      this.m[a] = set()
    this.m[a].add((b, w))
    if not b in this.m:
      this.m[b] = set()
    this.m[b].add((a, w))


  def print(this):
    print("\n".join([str(i[0]) + " -> " + ", ".join(str(j) for j in i[1]) for i in this.m.items()]))

def shortestPath(g, a, b):
  n = a
  visited = []
  visited.append(a)
  notVisited = [v for v in g.m.keys()]
  distance = 0

  done = False
  while not done:  
    adj = g.m[n]
    short = None
    for e in adj:
      #print(e)
      if e[0] in visited:
        continue

      if e[0] == b:
        done = True
        short = e
        break

      elif not short or e[1] < short[1]:
        short = e

    visited.append(short[0])
    distance += short[1]
    n = short[0]

  print(visited) 
  print(distance)
 

if __name__ == "__main__":
  g = Graph()

  g.addEdge(0, 1, 4)
  g.addEdge(0, 2, 3)
  g.addEdge(1, 2, 5)
  g.addEdge(1, 3, 2)
  g.addEdge(1, 4, 4)
  g.addEdge(0, 4, 4)
  g.addEdge(3, 4, 2)
  g.addEdge(4, 5, 6)
 
  shortestPath(g, 0, 5)
 

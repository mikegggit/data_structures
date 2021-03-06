#!/usr/bin/python

import math

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

  def neighbors(this, n):
    return this.m[n]

  def print(this):
    print("\n".join([str(i[0]) + " -> " + ", ".join(str(j) for j in i[1]) for i in this.m.items()]))

def dijkstra(g, a, b):
  
  notVisited = [v for v in g.m.keys()]
  distances = {v:math.inf for v in g.m.keys()}
  distances[a] = 0

  print(distances)
  cur = a
  while len(notVisited) > 0:
    
    # choose vertex from notVisited having lowest estimated distance

    
    if cur is None:                 # starting vertex
      print("Visiting starting vertex...")
      cur = a
      notVisited.remove(a)
    else:                           # choose unvisited neighbor having lowest estimated distance
      next = None
      minTentDist = 0
      for adj in g.neighbors(cur):
        if adj[0] in notVisited:
          print("neighbor={}".format(adj))
          tmp = distances[adj[0]] + adj[1]
          if not minTentDist or tmp < minTentDist:
            lowestTentDist = tmp
            next = adj

      cur = next[0]
      distances[cur] = minTentDist
      print("Visiting vertex [v={}]".format(cur))
      print(notVisited)
      notVisited.remove(cur)
    
"""
    for a in distances.items():
      if a.
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
""" 

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
 
  dijkstra(g, 0, 5)
 

#!/usr/bin/python

import copy

class MinHeap:
  """ MinHeap impl that stores multivariate node data, including id and weight """  
  nodes=[]

  def __init__(this):
    this.nodes = []

  def numNodes(this):
    return len(this.nodes)

  def isEmpty(this):
    return this.numNodes() == 0

  def heapifyUp(this, i):
    if this.numNodes() == 1:
      return

    pi = this.parent(i)
    if this.nodes[i][1] < this.nodes[pi][1]:
      this.swap(i, pi)
      this.heapifyUp(pi)

  def hasLeft(this, i):
    return this.leftIdx(i) <= this.numNodes() - 1

  def hasRight(this, i):
    return this.rightIdx(i) <= this.numNodes() - 1

  def isLeaf(this, i):
    return not this.hasLeft(i)

  def getWeight(this, i):
    return this.nodes[i][1]
 
  def heapifyDown(this, i):
    if not this.isLeaf(i):
      weightLeft = this.getWeight(this.leftIdx(i))
      weight = this.getWeight(i)
      if this.hasRight(i):
        weightRight = this.getWeight(this.rightIdx(i))
        if weightLeft < weight or weightRight < weight:
          if weightLeft < weightRight:
            this.swap(i, this.leftIdx(i))
            this.heapifyDown(this.leftIdx(i))
          else:
            this.swap(i, this.rightIdx(i))
            this.heapifyDown(this.rightIdx(i))
      elif weightLeft < weight:
        this.swap(i, this.leftIdx(i))
          
  def swap(this, i, j):
    tmp = this.nodes[i]
    this.nodes[i] = this.nodes[j]
    this.nodes[j] = tmp

  def add(this, data):
    this.nodes.append(data)
    this.heapifyUp(this.numNodes()-1)    

  def pop(this):
    this.swap(0, this.numNodes() - 1)
    min = this.nodes[this.numNodes() - 1]
    this.nodes.remove(min)
    this.heapifyDown(0)
    return min
 
  def left(this, i):
    return this.nodes[this.leftIdx(i)]

  def right(this, i):
    return this.nodes[this.rightIdx(i)]

  def leftIdx(this, i):
    return 2 * i + 1

  def rightIdx(this, i):
    return 2 * i + 2

  def parent(this, i):
    return int((i - 1) / 2)

  def peek(this):
    if this.isEmpty():
      return None
    return copy.deepcopy(this.nodes[0]) if not this.isEmpty() else None

if __name__ == "__main__":
  h = MinHeap()

  h.add(('D',3))
  h.add(('E',4))
  h.add(('B',5))
  h.add(('A',1))

  assert h.peek() == ('A',1)
  print(h.peek())

  assert h.pop() == ('A', 1)

  assert h.peek() == ('D',3)
  print(h.peek())

  assert h.pop() == ('D', 3)

  assert h.peek() == ('E',4)
  print(h.peek())

  assert h.pop() == ('E', 4)

  assert h.peek() == ('B',5)
  print(h.peek())

  assert h.pop() == ('B', 5)
  assert h.isEmpty()

#!/usr/bin/python

import math

class Heap:

  root = None
  numEntries = 0
  
  def __init__(this, capacity):
    this.ar = [None] * capacity

  def heapify(this):
    pass

  def min(this):
    return this.root()

  def isEmpty(this):
    return this.numEntries == 0

  def root(this):
    if this.isEmpty():
      return None
  
    return this.ar[0]

  def height(this):
    return math.ceil(math.log(this.numEntries +1, 2)) - 1

  def removeMin(this):
    if this.numEntries == 0:
      raise Exception("No entries.")

    val = this.min()
    this.ar[0] = this.ar[this.numEntries - 1]
    
    this.ar[this.numEntries - 1] = None
    this.numEntries -= 1
    this.heapifyDown(0)
    return val

  def size(this):
    return this.numEntries

  def insert(this, data):
    if this.numEntries == len(this.ar):
      raise Exception("Heap is full.")

    root = this.root()
   
    if root is None:
      this.ar[0] = data
      this.numEntries += 1
    else:
      this.numEntries += 1
      this.ar[this.numEntries - 1] = data
      this.heapifyUp(this.numEntries - 1)

  def getParentIdx(this, idx):
    if idx == 0:
      return None

    return int(idx / 2)

  def minChildIdx(this, idx):
    li = 2 * idx + 1
    lr = 2 * idx + 2

    if li > this.numEntries - 1:
      return   
 
  
  def heapifyDown(this, idx):

    hasLeft = this.numEntries - 1 >= 2 * idx + 1
    
    if not hasLeft:
      return

    li = idx * 2 + 1
    ri = idx * 2 + 2

    if ri <= this.numEntries - 1:        # two children
      if this.ar[li] <= this.ar[ri]:     # left is <= right
        if this.ar[li] < this.ar[idx]:   # swap w/ lft child 
          temp = this.ar[idx]
          this.ar[idx] = this.ar[li]
          this.ar[li] = temp
          this.heapifyDown(li)
      else:                              # left > right
        if this.ar[ri] < this.ar[idx]:
          temp = this.ar[idx]
          this.ar[idx] = this.ar[ri]
          this.ar[ri] = temp
          this.heapifyDown(ri)
              
    else:                                # one (left) child
      if this.ar[li] < this.ar[idx]:     # swap w/ left child
        temp = this.ar[idx] 
        this.ar[idx] = this.ar[li]
        this.ar[li] = temp
        this.heapifyDown(li)


  def heapifyUp(this, idx):
    """ Reorg the last element in the heap until the heap invariant is established / verified."""
    parentIdx = this.getParentIdx(idx)

    if parentIdx is None:
      return

    if this.ar[parentIdx] > this.ar[idx]:
      # swap val of node @ idx w/ parent val
      temp = this.ar[parentIdx]
      this.ar[parentIdx]  = this.ar[idx]
      this.ar[idx] = temp
      this.heapifyUp(parentIdx)
 
if __name__ == "__main__":
  h = Heap(5)

  assert h.size() == 0
  assert h.min() is None
  h.insert(10)

  assert h.size() == 1
  assert h.min() == 10  
  
  h.insert(5)
  assert h.size() == 2
  assert h.min() == 5 
 
  h.insert(25)
  assert h.size() == 3
  assert h.min() == 5 

  h.insert(16)
  assert h.size() == 4
  assert h.min() == 5 

  h.insert(4)
  assert h.size() == 5
  assert h.min() == 4 

  try:
    h.insert(40)
  except Exception as e:
    print(e)

  m = h.removeMin()
  assert m == 4
  assert h.min() == 5
  assert h.size() == 4
  assert h.height() == 2

  m = h.removeMin()
  assert m == 5
  assert h.min() == 10
  assert h.size() == 3
  assert h.height() == 1

  m = h.removeMin()
  assert m == 10
  assert h.min() == 16
  assert h.size() == 2
  assert h.height() == 1

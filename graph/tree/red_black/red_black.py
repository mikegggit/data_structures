#!/usr/bin/python



class Node:
  l = None
  r = None
  color = 1 # 0 => red, 1 => black
  data = None

  def __init__(this, data, color=0):
    this.data = data

  def hasChildren(this):
    return this.l or this.r

class RedBlack:
  def __init__(this):
    this.root = None

  def insert(this, data):
    if data is None:
      return

    n = Node(data)
    if this.root is None:
      this.root = n
    else:
      n = this.root
      while n:
        if data < n.data:
          if n.l:
            n = n.l
          else:
            
            n.l = Node(data)  
        else:
          if n.r:
            n = n.r
          else:
            n.r = Node(data)
        

if __name__ == "__main__":
  t = RedBlack()
  t.insert(1)
  t.insert(2)
  t.insert(3)
  t.insert(4)

  print(t.

#!/usr/bin/python

from functools import total_ordering

@total_ordering
class Person:
  ssn    = None
  name   = None

  def __init__(this, ssn, name=None):
    this.ssn  = ssn
    this.name = name

  def __eq__(this, rhs):
    return this.ssn == rhs.ssn

  def __lt__(this, rhs):
    return this.ssn < rhs.ssn

  def __str__(this):
    return "ssn = {}, name = {}".format(this.ssn, this.name)
 
class Node:
  """A tree node.

  data - a comparable value
  """

  parent = None
  data   = None
  left   = None
  right  = None

  def __init__(this, data=None, parent=None):
    this.data = data
    this.parent = parent

  def insert(this, data, parent=None):

    if this.data is None:  
      this.data = data               # tree is empty   
      return this

    elif data < this.data:           # new < current
      if this.left is None:          
        this.left = Node(data, this)
        return this.left
      else:
        this.left.insert(data)   

    else:
      if this.right is None:         # new >= current
        this.right = Node(data, this)
        return this.right
      else:
        this.right.insert(data)
      
  def printInOrder(this):
    if this.data is None:
      print("Empty")
    else:
      if this.left:
	this.left.printInOrder()

      print(this.data)

      if this.right:
	this.right.printInOrder()

  def printPreOrder(this):
    if this.data is None:
      print("Empty")
    else:
      print(this.data)
 
      if (this.left):
        this.left.printPreOrder()
  
      if (this.right):
        this.right.printPreOrder()

  def printPostOrder(this):

    if this.data is None:
      print("Empty")
    else:
      if this.left:
	this.left.printPostOrder()

      if this.right:
	this.right.printPostOrder()

      print(this.data)

  def find(this, data):
    if this.data is None:           # tree is empty
      return None
    
    if data == this.data:           # found the node
      return this
    elif data < this.data:          # try searching left
      if this.left is None:
        return None
      else:
        return this.left.find(data)
    else:                           # tre searching right
      if this.right is None:
        return None
      else:
        return this.right.find(data)

  def min(this):
    if this.left is None:
      return this
    else:
      return this.left.min()

  def max(this):
    if this.right is None:
      return this
    else:
      return this.right.max()

  def height(this):
    """Recursive function"""
    hl, hr = -1, -1
  
    if this.left:
      hl = this.left.height() 
    if this.right:
      hr = this.right.height()

    if hl > hr:
      return hl + 1
    else:
      return hr + 1

  def remove(this, data):
    """Removes data from tree.

    Find node...
    Remove...
    """
    print("remove [data={}]".format(data))
    nodeDel = this.find(data)

    if nodeDel is None:
      return False

    if nodeDel.left and nodeDel.right:
     
      # if two children, find min right, copy value to current, and delete min
      nodeMinRight = nodeDel.right.min()
      nodeMinRightParent = nodeMinRight.parent
      nodeDel.data = nodeMinRight.data

      return nodeMinRight.remove(nodeMinRight.data)

    elif nodeDel.left:
      print("left")
      nodeDelParent = nodeDel.parent
      if nodeDelParent.left and nodeDelParent.left.data == nodeDel.data:
        nodeDelParent.left = nodeDel.left
        nodeDel.left.parent = nodeDelParent
        return True
      elif nodeDelParent.right and nodeDelParent.right.data == nodeDel.data:
        nodeDelParent.right = nodeDel.left
        nodeDel.left.parent = nodeDelParent
        return True

    elif nodeDel.right:
      print("right")
      nodeDelParent = nodeDel.parent
      if nodeDelParent.left and nodeDelParent.left.data == nodeDel.data:
        nodeDelParent.left = nodeDel.right
        nodeDel.right.parent = nodeDelParent
        return True
      elif nodeDelParent.right and nodeDelParent.right.data == nodeDel.data:
        nodeDelParent.right = nodeDel.right
        nodeDel.right.parent = nodeDelParent
        return True

    else:              # No children, just delete the node
      print("no children")
      print(nodeDel)
      nodeDelParent = nodeDel.parent
      if nodeDelParent.left and nodeDelParent.left.data == nodeDel.data:
        nodeDelParent.left = None
        return True
      elif nodeDelParent.right and nodeDelParent.right.data == nodeDel.data:
        nodeDelParent.right = None
        return True

  
  def __str__(this):
    result="Node [data='{}', parent='{}']"
    if this.data is None:
      return result.format("x")

    if this.parent is None:
      return result.format(this.data, "x")
    
    return result.format(this.data, this.parent.data)
if __name__ == "__main__":
  tree = Node()

  tree.insert(Person(10, "Mike"))
  tree.insert(Person(5, "Jane"))
  tree.insert(Person(7, "Fred"))
  tree.insert(Person(3, "Betsy"))
  print(tree.insert(Person(100, "Laura")))
  tree.insert(Person(200, "Steve"))
  tree.insert(Person(300, "Steve"))
  tree.insert(Person(150, "Mary"))
  tree.insert(Person(175, "Stewie"))

  tree.printInOrder()
  tree.printPreOrder()
  tree.printPostOrder()

  print(tree.min()) 
  print(tree.max()) 
  print(tree.height())

  print(tree.find(Person(200)))
  tree.remove(Person(10))
  tree.printInOrder()
  tree.remove(Person(150))
  tree.printInOrder()
  tree.remove(Person(100))
  tree.printInOrder()
  tree.remove(Person(300))
  tree.printInOrder()
  tree.remove(Person(175))
  tree.printInOrder()
  tree.remove(Person(5))
  tree.printInOrder()

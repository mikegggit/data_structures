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

    elif data < this.data:           # new < current
      if this.left is None:          
        this.left = Node(data, this)
      else:
        this.left.insert(data)   

    else:
      if this.right is None:         # new >= current
        this.right = Node(data, this)
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
      return this.data
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
      return this.data
    else:
      return this.left.min()

  def max(this):
    if this.right is None:
      return this.data
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
       
if __name__ == "__main__":
  tree = Node()

  tree.insert(Person(10, "Mike"))
  tree.insert(Person(5, "Jane"))
  tree.insert(Person(7, "Fred"))
  tree.insert(Person(3, "Betsy"))
  tree.insert(Person(100, "Laura"))
  tree.insert(Person(200, "Steve"))
  tree.insert(Person(300, "Steve"))
  tree.insert(Person(400, "Steve"))
  tree.insert(Person(500, "Steve"))
  tree.insert(Person(600, "Steve"))
  tree.insert(Person(700, "Steve"))
  tree.insert(Person(800, "Steve"))
  tree.insert(Person(900, "Steve"))
  tree.insert(Person(150, "Mary"))
  tree.insert(Person(175, "Stewie"))

  tree.printInOrder()
  tree.printPreOrder()
  tree.printPostOrder()

  print(tree.min()) 
  print(tree.max()) 
  print(tree.height())

  print(tree.find(Person(200)))

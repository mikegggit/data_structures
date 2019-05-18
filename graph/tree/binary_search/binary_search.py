#!/usr/bin/python

class Node:
  val        = None
  leftChild  = None
  rightChild = None

  def __init__(this, val = None):
    if val:
      this.val = val

  def insert(this, val):
    print("insert [this={}, val={}]".format(this, val))
    # if node has no current value, set the value to val
    if not this.val:
      this.val = val

    # If val is < the current node, go to the left child
    elif val < this.val:
      if not this.leftChild:
        this.leftChild = Node(val)
      else:
        this.leftChild.insert(val)
   
    # if val is >= the current node, go to the right child
    elif val >= this.val:
      if not this.rightChild:
        this.rightChild = Node(val)
      else:
        this.rightChild.insert(val)
 

  def find(this, val):
    pass

  def remove(this, val):
    pass

  def min(this):
    """Return left-most node"""
    if not this.leftChild:
      return this.val
   
    return this.leftChild.min() 

  def max(this):
    """Return right-most node"""
    if not this.rightChild:
      return this.val

    return this.rightChild.max()

  def __str__(this):
    return "val={}".format(this.val)
 
  def printInOrder(this):
    """Traverses the tree in order resulting in a sorted sequence of values"""
    if not this.val:
      print("Empty.")

    if this.leftChild:
      this.leftChild.printInOrder()

    print(this.val)

    if this.rightChild:
      this.rightChild.printInOrder()
 
  def printPreOrder(this):
    if not this.val:
      print("Empty.")
  
    print this.val

    if this.leftChild:
      this.leftChild.printPreOrder()   

    if this.rightChild:
      this.rightChild.printPreOrder()

  def printPostOrder(this):
    if not this.val:
      print("Empty.")

    if this.leftChild:
      this.leftChild.printPostOrder()

    if this.rightChild:
      this.rightChild.printPostOrder()
  
    print(this.val)
    
if __name__ == "__main__":
  tree = Node()

  tree.insert(5)
  tree.insert(50)
  tree.insert(20)

  tree.printInOrder()
  tree.printPreOrder()
  tree.printPostOrder()

  print("min()={}".format(tree.min()))
  print("max()={}".format(tree.max()))

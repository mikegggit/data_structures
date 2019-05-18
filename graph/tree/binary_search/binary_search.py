#!/usr/bin/python

class Node:
  key        = None
  val        = None
  leftChild  = None
  rightChild = None

  def __init__(this, key = None, val = None):
    if val and not key:
      raise Exception("val must have a key")

    this.key = key
    this.val = val

  def insert(this, key, val):
    print("insert [this={}, key={}, val={}]".format(this, key, val))
    # if node has no current key, set the value to val
    if not this.key:
      this.key = key
      this.val = val 

    # If key is < the current node, go to the left child
    elif key < this.key:
      if not this.leftChild:
        this.leftChild = Node(key, val)
      else:
        this.leftChild.insert(key, val)
   
    # if key is >= the current node, go to the right child
    elif key >= this.key:
      if not this.rightChild:
        this.rightChild = Node(key, val)
      else:
        this.rightChild.insert(key, val)

  def find(this, key):
    print("find [key={}, this.key={}]".format(key, this.key))
    if not key:
      return None

    if key == this.key:
      return this

    if key < this.key:
      if not this.leftChild:
        return None
      else:
        return this.leftChild.find(key)
    else:
      if not this.rightChild:
        return None
      else:
        return this.rightChild.find(key)
      
  def remove(this, key):
    if not key:
      return None

    if key == this.key:
      # no children
      
    
    pass

  def min(this):
    """Return left-most node"""
    if not this.leftChild:
      return this
   
    return this.leftChild.min() 

  def max(this):
    """Return right-most node"""
    if not this.rightChild:
      return this

    return this.rightChild.max()

  def __str__(this):
    return "key={}, val={}".format(this.key, this.val)
 
  def printInOrder(this):
    """Traverses the tree in order resulting in a sorted sequence of values"""
    if not this.key:
      print("Empty.")

    if this.leftChild:
      this.leftChild.printInOrder()

    print(this)

    if this.rightChild:
      this.rightChild.printInOrder()
 
  def printPreOrder(this):
    if not this.key:
      print("Empty.")
  
    print this

    if this.leftChild:
      this.leftChild.printPreOrder()   

    if this.rightChild:
      this.rightChild.printPreOrder()

  def printPostOrder(this):
    if not this.key:
      print("Empty.")

    if this.leftChild:
      this.leftChild.printPostOrder()

    if this.rightChild:
      this.rightChild.printPostOrder()
  
    print(this)
    
if __name__ == "__main__":
  tree = Node()

  tree.insert(100, "one hundred")
  tree.insert(50, "fifty")
  tree.insert(10, "ten")
  tree.insert(5, "five")
  tree.insert(75, "seventy five")

  tree.printInOrder()
  tree.printPreOrder()
  tree.printPostOrder()

  print("min()={}".format(tree.min()))
  print("max()={}".format(tree.max()))

  print("find(5)={}".format(tree.find(75)))

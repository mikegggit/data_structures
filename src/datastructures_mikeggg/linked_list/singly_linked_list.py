#!/usr/bin/python

class Node:

  val = None
  next = None

  def __init__(this, val=None, next=None):
    this.val = val
    this.next = next

  def __str__(this):
    return str(this.val)

  def hasNext(this):
    return this.next != None

class LinkedList:
  
  head = None
  tail = None

  def __init__(this):
    pass

  def add(this, val):

    node = Node(val)
    # check if empty
    if this.head == None:
      this.head = node
      this.tail = this.head
    else:
      # not empty 
      this.tail.next = node
      this.tail = node

  def deleteNode(this, v):
    """Deletes first occurrence of node having value v"""

    # check if empty
    if this.head is None:
      return
   
    # deleting head? 
    if this.head.val == v:
      this.head = this.head.next
      return
 
    node = this.head.next
    prev = this.head

    while True:
      if node.val == v:
        prev.next = node.next
        return
      
      # didn't fine the node to delete    
      if not node.next:
        return
     
      prev = node 
      node = node.next
 
  def __str__(this):
    node = this.head
    
    if node is None:
      return "EMPTY"

    s=""
  
    isFirst = True

    while True:
      if not isFirst:
        s += ","
      else:
        isFirst = False
      s += str(node.val)
      if not node.next:
        return s

      node = node.next

if __name__ == "__main__":
  ll = LinkedList()
  ll.add(9)
  ll.add(8)
  ll.add(7)
  ll.add(6)
  ll.add(5)

  print(ll)

  ll.deleteNode(7)

  print(ll)

#!/usr/bin/python

import math

"""Hashing w/ chaining.

Doesn't handle deletes.
"""

class Employee:
  phoneNumber = None
  fullName = None
  address = None

  def __init__(this, phoneNumber, fullName, address):
    this.phoneNumber = phoneNumber
    this.fullName = fullName
    this.address = address

  def __str__(this):
    return "Employee [ph#={}, name={}, address={}]".format(this.phoneNumber, this.fullName, this.address)

  def __eq__(this, other):
    if not isinstance(other, Employee):
      return False
    return this.phoneNumber == other.phoneNumber 

class HashNode:
  """Represents a chained entry at hashtable index.

     Each HashTable index points to the head of this linked-list impl.
  """
  key   = None # A number
  val   = None
  next  = None
 
  def __init__(this, key, val):
    this.key = key
    this.val = val

  def __str__(this):
    node = this

    result = "Entry [key={}, val={}]".format(node.key, node.val);

    while node.next:
      node = node.next
      result += " -> "
      result += "Entry [key={}, val={}]".format(node.key, node.val);
   
    return result

def employeeHashFunction(key):
  return key


class HashTable:
  """Simple implementation of a hashtable
    
     Data is represented by a key and a value.

     Data.key represents something unique about the data enabling it to be used as an identifier.

     Data.value is the data itself.  May be a complex type.

     
  """

  INITIAL_SLOTS = 37
  LOAD_FACTOR = .25 
  numSlots = INITIAL_SLOTS
  slots=None
  size=0
   
  def __init__(this, numSlots = INITIAL_SLOTS):
    print("Initializing HashTable...")
    this.slots = [None] * numSlots
    print("done...[numSlots={}]".format(len(this.slots)))
 
  def getHashIdx(this, key):
    return employeeHashFunction(key) % this.numSlots
      
  def add(this, key, val):
    slotIdx = this.getHashIdx(key)

    node = this.slots[slotIdx]

    if node is None:
      # No entries yet for this slot...
      print("Inserting new node chain [slotIdx={}, key={}, val={}]".format(slotIdx, key, val))
      node = HashNode(key, val)
      this.slots[slotIdx] = node
      this.size += 1
      newLoadFactor = this.size / this.numSlots
      print("New load factor -> {}".format(newLoadFactor))

      if (newLoadFactor > this.LOAD_FACTOR):
        
        print("Rehashing...")
        this.expand()

    else:
      # See if key already exists...
      while node:
        if node.key == key:
          print("Updating node [slotIdx={}, key={}, old={}, new={}]".format(slotIdx, key, node.val, val))
          node.val = val
          return
        else:
          node = node.next
     
      # no existing key, add to the chain...make it the new head of the chain...    
      print("Inserting new node [slotIdx={}, key={}, val={}]".format(slotIdx, key, val))
      newNode = HashNode(key, val)

      oldHead = this.slots[slotIdx]
    
      this.slots[slotIdx] = newNode
      newNode.next = oldHead
 
  def expand(this):
    # temporarily stash current slots
    tempSlots = this.slots

    newSize = nextPrime(2 * this.numSlots)
    print("Resizing hashtable [old={}, new={}]".format(this.numSlots, newSize))

    this.slots = [None] * newSize
    this.numSlots = newSize
    this.size = 0
 
    # rehash existing nodes
    for n in tempSlots:
      if not n:
        continue

      while n:
        this.add(n.key, n.val)
        n = n.next
     

  def get(this, key):
    idx = this.getHashIdx(key)
    node = this.slots[idx]

    while node:
      if node.key == key:
        return node.val
      else:
        node = node.next

    raise Exception("key not found in hashtable [key={}]".format(key))

def isPrime(n):
  i = 2
  while i <= math.sqrt(n):
    if n % i == 0:
      return False
    i += 1

  return True
    
def nextPrime(n):
  """returns next prime greater than n"""
  v = n + 1
  while True:
    if isPrime(v):
      return v
    v = v + 1
 
if __name__ == "__main__":
  ht = HashTable()

  ht.add(4124921456,Employee(4124921456, "Joe Shmoe", "123 Main Street"))
  ht.add(4122931112,Employee(4122931112, "Mike Smith", "999 Blue Road"))
  ht.add(3324924567,Employee(3324924567, "Lisa Lee", "555 Red Lane"))
  ht.add(9324725673,Employee(9324725673, "Mary Jones", "4 Clover Lane"))
  ht.add(9324221673,Employee(9324221673, "Tim Jones", "10 Main Street"))
  ht.add(9324725677,Employee(9324725677, "Jay Thomas", "98 Thompson Ave"))
  ht.add(9324725633,Employee(9324725633, "Dennis Plummer", "5 Park Place"))
  ht.add(1324125603,Employee(1324125603, "Mike Ives", "87 Baltic Ave"))
  ht.add(3324725663,Employee(3324725663, "Ian Holmes", "23 Pacific Ave"))
  ht.add(5324225673,Employee(5324225673, "Katy Perry", "455 Oriental Ave"))
  ht.add(2324325683,Employee(2324325683, "Mike Douglas", "7 Indiana Ave"))
  ht.add(7324725673,Employee(7324725673, "Doug Jones", "41 Palm St"))
  ht.add(9324725653,Employee(9324725653, "Amy Adams", "99 Robin Road"))
  ht.add(4324325673,Employee(4324325673, "Al Einstein", "8 Sherwood Drive"))
  ht.add(9324725603,Employee(9324725603, "Joe Cocker", "48 Commonwealth Avenue"))

  print(ht.get(9324725677))
  #print(ht.get(9324725603))


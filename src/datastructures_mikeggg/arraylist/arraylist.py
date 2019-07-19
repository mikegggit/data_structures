#!/usr/bin/python

"""Resizable list.

Protects against gaps in the list.
"""

class ArrayList:

  GROWTH_FACTOR = 2  
  array = None
  count = 0

  def __init__(this, initialCapacity):
    this.array = [None] * initialCapacity

  def add(this, el):
    """Append el to end of array"""
    print("add [el={}, count={}, arr-len={}]".format(el, this.count, len(this.array)))
    # check that array is big enough
    if this.count == len(this.array):
      this.grow()

    this.array[this.count] = el;
    this.count += 1
    print("...done [el={}, count={}, arr-len={}]".format(el, this.count, len(this.array)))

 
  def addAt(this, idx, el):

    # Check if there's room...
    if this.count == len(this.array):
      this.grow()

    # shift elements starting at idx right one slot...
    i = this.count 
    while i > idx:
      this.array[i] = this.array[i - 1]
      i -= 1

    this.array[idx] = el
    this.count += 1

  def remove(this):
    """removes item at end of backing array"""
    print("remove [el={}, count={}]".format(this.array[this.count - 1], this.count))
    this.array[this.count - 1] = None
    this.count -= 1
    print("...done [count={}]".format(this.count))

  def removeAt(this, idx):
    """removes item at given idx"""
    print("removeAt [el={}, count={}]".format(this.array[idx], this.count))
    
    i = idx
    while i < this.count:
      this.array[i] = this.array[i+1]
      i += 1
       
    this.array[this.count] = None
    this.count -= 1
    print("...done [count={}]".format(this.count))
    
  def grow(this):
    print("grow [size-old={}, new-size={}]".format(len(this.array), this.GROWTH_FACTOR * len(this.array)))
    # double the size of the underlying array...
    
    # stash current array
    temp = this.array

    # copy contents of original array into new larger one
    this.array = temp.copy() + [None] * len(temp)
    
  def __str__(this):
    return ", ".join([str(e) for e in this.array if e is not None])

    
if __name__ == "__main__":
  al = ArrayList(4)
  al.add(1)
  al.add(2)
  al.add(3)
  al.add(4)
  al.add(5)

  print(al)

  print(al.array)  

  al.addAt(0, 10)
  print(al.array)  
  al.addAt(0, 10)
  print(al.array)  
  al.addAt(0, 10)
  print(al.array)  
  al.addAt(0, 10)
  print(al.array)  
  al.add(10)
  print(al.array)  
  al.addAt(1, 20)
  print(al.array)  
  al.remove()
  print(al.array)
  al.removeAt(0)
  print(al.array)

#!/usr/bin/python

INITIAL_SLOTS = 37

slots = INITIAL_SLOTS

class Employee:
  phoneNumber = None
  fullName = None
  address = None

  def __init__(this, phoneNumber, fullName, address):
    this.phoneNumber = phoneNumber
    this.fullName = fullName
    this.address = address

  def hash(this):
    return this.phoneNumber % slots

  def __str__(this):
    return "Employee [ph#={}, name={}, address={}]".format(this.phoneNumber, this.fullName, this.address)

  def __eq__(this, other):
    print("__eq__")
    if not isinstance(other, Employee):
      return False
    print("111")
    return this.phoneNumber == other.phoneNumber 

"""Uses chaining.

Doesn't handle rehashing.
"""

def hash(v):
  return v % slots


class HashTable:
  """Simple implementation of a hashtable"""

  slots=None
  
  def __init__(this, numSlots = INITIAL_SLOTS):
    """establish hashtable w/ chaining"""
    this.slots = [None] * numSlots

  def add(this, value):
    slot = value.hash()

    print("add [value={}, slot={}]".format(value, slot))

    if this.slots[slot] is None:
      this.slots[slot] = [value]
    else:
      this.slots[slot].append(value)

  def get(this, v):
    hv = hash(v)
    chain = this.slots[hv]

    print("get [v={}, key={}, chain={}]".format(v, hv, chain))    

    for i in chain:
      if i.phoneNumber == v:
        return i

    raise Exception("v not found in hashtable [v={}]".format(v))
  
 
if __name__ == "__main__":
  ht = HashTable()

  ht.add(Employee(4124921456, "Joe Shmoe", "123 Main Street"))
  ht.add(Employee(4122931112, "Mike Smith", "999 Blue Road"))
  ht.add(Employee(3324924567, "Lisa Lee", "555 Red Lane"))
  ht.add(Employee(9324725673, "Mary Jones", "4 Clover Lane"))
  ht.add(Employee(9324221673, "Tim Jones", "10 Main Street"))
  ht.add(Employee(9324725677, "Jay Thomas", "98 Thompson Ave"))
  ht.add(Employee(9324725633, "Dennis Plummer", "5 Park Place"))
  ht.add(Employee(1324125603, "Mike Ives", "87 Baltic Ave"))
  ht.add(Employee(3324725663, "Ian Holmes", "23 Pacific Ave"))
  ht.add(Employee(5324225673, "Katy Perry", "455 Oriental Ave"))
  ht.add(Employee(2324325683, "Mike Douglas", "7 Indiana Ave"))
  ht.add(Employee(7324725673, "Doug Jones", "41 Palm St"))
  ht.add(Employee(9324725653, "Amy Adams", "99 Robin Road"))
  ht.add(Employee(4324325673, "Al Einstein", "8 Sherwood Drive"))
  ht.add(Employee(9324725603, "Joe Cocker", "48 Commonwealth Avenue"))

  print(ht.get(9324725677))
  #print(ht.get(9324725603))


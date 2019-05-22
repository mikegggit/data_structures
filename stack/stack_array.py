#!/usr/bin/python

class Stack:

  numElements= 0
  ar = None

  front = 0

  def __init__(self, capacity):
    self.ar = [None] * capacity

  def peek(self):
    if self.numElements == 0:
      return None

    return self.ar[self.front]
    
  def push(self, data):
    if self.numElements == len(self.ar):
      raise Exception("Stack is full.")
    
    if self.front == 0:
      self.front = len(self.ar) - 1
    else:
      self.front -= 1

    self.ar[self.front] = data
    self.numElements += 1

  def pop(self):
    if self.numElements == 0:
      return None

    val = self.ar[self.front]
    self.ar[self.front] = None
    if self.front == len(self.ar) - 1:
      self.front = 0
    else:
      self.front += 1
    self.numElements -= 1
    return val

  def size(self):
    return self.numElements

  def __str__(self):
    return ""

if __name__ == "__main__":
  s = Stack(5)
  assert s.size() == 0

  assert s.peek() is None

  s.push(10)

  assert s.size() == 1
  assert s.peek() == 10
  
  s.push(20)
  s.push(30)

  assert s.size() == 3
  assert s.peek() == 30
 
  s.push(40)
  s.push(50)

  assert s.size() == 5
  assert s.peek() == 50

  try:
    s.push(60)
  except Exception as e:
    print(e) 

  assert s.size() == 5
  assert s.peek() == 50

  assert s.pop() == 50
  assert s.size() == 4
  assert s.peek() == 40

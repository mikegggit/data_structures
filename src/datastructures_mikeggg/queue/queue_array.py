#!/usr/bin/python

"""Implemented using an array implementing a circular buffer.  """
class Queue:
    
  items = None
   
  """first item enqueued"""
  front = 0

  """last item enqueued"""
  back  = 0 

  """number of data points stored in items
  
  less than or equal to len(items)"""
  numFilled = 0

  def __init__(self, capacity):
    self.items = [None] * capacity 
    self.back = 0
    self.front = 0
    self.numFilled = 0

  def enqueue(self, data):
    if self.back == self.front and self.numFilled == len(self.items):
      raise Exception("Queue is full [capacity={}]".format(len(self.items)))

    self.numFilled += 1
    self.items[self.back] = data
    if self.back == len(self.items) - 1:
      self.back = 0
    else:
      self.back += 1
  
  def peek(self):
    if len(self.items) == 0:
      return None
  
    return self.items[self.front]

  def dequeue(self):
    popped = self.items[self.front]
    self.numFilled -= 1
    if self.front == len(self.items) - 1:
      self.front = 0
    else:
      self.front += 1
    return popped

  def size(self):
    return self.numFilled

  def isEmpty(self):
    return self.numFilled == 0

  def __str__(self):
    return "hello"

if __name__ == "__main__":
  q = Queue(5)
  assert q.size() == 0
  assert q.peek() is None
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.enqueue(4)
  q.enqueue(5)
  
  assert q.size() == 5
  assert q.peek() == 1
 
  try:
    q.enqueue(0)
  except Exception as e:
    print(e)
     
  popped = q.dequeue()
  assert popped == 1
  assert q.size() == 4
  assert q.peek() == 2
  q.dequeue()
  q.dequeue()
  assert q.size() == 2
  assert q.peek() == 4
  assert q.dequeue() == 4

  q.enqueue(100)
  assert q.size() == 2
  q.dequeue()
  assert q.peek() == 100
  assert q.dequeue() == 100
  assert q.size() == 0 
  assert q.isEmpty()

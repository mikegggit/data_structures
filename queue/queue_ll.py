#!/usr/bin/python

class Node:
 
  val = None
  next = None
  
  def __init__(self, val=None):
    self.val = val

  def next(self):
    return self.next if self.next else None
 
   
class Queue:

  """Pointer to front of queue"""
  front = None

  """Pointer to end of queue"""
  back = None

  """Number of elements currently enqueued"""
  numEnqueued = 0

  """Capacity of this queue"""
  capacity = -1

  def __init__(self, capacity):
    self.capacity = capacity

  def enqueue(self, val):
    if self.numEnqueued == self.capacity:
      raise Exception("Queue is full [capacity = {}]".format(self.capacity))

    if self.front is None:
      self.front = Node(val)
      self.back = self.front
    else:
      self.back.next = Node(val) 
      self.back = self.back.next

    self.numEnqueued += 1

  def size(self):
    return self.numEnqueued

  def peek(self):
    return self.front.val

  def dequeue(self):
    if self.front is None:
      return None
    else:
      dequeued = self.front.val
      if self.front.next:
        self.front = self.front.next
      else:
        self.front = None
      self.numEnqueued -= 1
      return dequeued 

if __name__ == "__main__":
  q = Queue(5)
  q.enqueue(1)

  assert q.size() == 1
  assert q.peek() == 1 

  q.enqueue(2)

  assert q.size() == 2
  assert q.peek() == 1 

  q.enqueue(3)
  q.enqueue(4)
  q.enqueue(5)

  try:
    q.enqueue(100)
    assert True == False
  except Exception as e:
    print(e)

  assert q.size() == 5
  assert q.peek() == 1 

  assert q.dequeue() == 1
  assert q.dequeue() == 2
  assert q.dequeue() == 3
 
  assert q.size() == 2
  assert q.peek() == 4

     

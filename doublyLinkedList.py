from node import Node

class DoublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
  
  def moveToHead(self, node):
    self.remove(node)
    self.addToHead(node)

  def remove(self, node):
    if self.head != node:
      node.prev.next = node.next
    else:
      self.head = node.next
    if self.tail != node:
      node.next.prev = node.prev
    else:
      self.tail = node.prev
    node.prev = None
    node.next = None

  def addToHead(self, node):
    if self.head:
      self.head.prev = node
      node.next = self.head
    else:
      self.tail = node
    self.head = node

  def removeTail(self):
    oldTail = self.tail
    self.tail = self.tail.prev
    self.tail.next = None
    return oldTail

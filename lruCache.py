from doublyLinkedList import DoublyLinkedList
from node import Node

class LruCache():
  def __init__(self, itemLimit):
    self.itemLimit = itemLimit
    self.itemCount = 0
    self.store = {}
    self.list = DoublyLinkedList()

  def set(self, key, val):
    if key not in self.store:
      self.store[key] = Node(key, val)
      self.itemCount += 1
    elif self.store.get(key) != val:
      self.store[key] = Node(key, val)
    self.list.addToHead(self.store.get(key))
    if self.itemCount > self.itemLimit: 
      tail = self.list.removeTail()
      del self.store[tail.key]

  def get(self, key):
    if key in self.store:
      node = self.store.get(key)
      self.list.moveToHead(node)
      return node.val

  def remove(self, key):
    if key in self.store:
      node = self.store.get(key)
      self.list.remove(node)
      del self.store[node.key]
      return node.val

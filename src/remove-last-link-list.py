#!/usr/bin/python2.7

import unittest
from test import test_support


class Node(object):
  def __init__(self, value):
    self.next = None
    self.value = value

class LinkedList(object):
  def __init__(self):
    self.tail = None
    self.head = None

  def add(self, value):
    node = Node(value)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def remove_last(self):
    if not self.tail or not self.head:
      return None
    if self.tail == self.head:
      val = self.tail.value
      self.tail = None
      self.head = None
      return val

    cur = self.head
    while cur.next:
      second_to_last = cur
      cur = cur.next

    value = self.tail.value
    self.tail = second_to_last
    self.tail.next = None
    return value

  def get_list(self):
    cur = self.head
    l = []
    if not cur:
      return l
    while cur:
      l.append(cur.value)
      cur = cur.next
    return l

  def get_last(self):
    cur = self.head
    while cur.next:
      cur = cur.next


class TestLinkedList(unittest.TestCase):
  def test_one(self):
    test_array = ['d', 'e', 'a', 'd', 'b', 'e', 'e', 'f']

    l = LinkedList()
    for i in test_array:
      l.add(i)

    self.assertEqual(test_array, l.get_list())

    new_list = []
    while True:
      cur = l.remove_last()
      if not cur:
        break

      new_list.append(cur)

    test_array.reverse()
    self.assertEqual(test_array, new_list)









if __name__ == '__main__':
   test_support.run_unittest(TestLinkedList)















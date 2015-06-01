#!/usr/local/bin/python3
"""
Unittest for linked_list.py
"""

from linked_list import *
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.mylist = UnorderedList()
        self.mylist.add(31)
        self.mylist.add(77)
        self.mylist.add(17)
        self.mylist.add(93)
        self.mylist.add(26)
        self.mylist.add(54)

    def test_size(self):
        self.assertEqual(self.mylist.size(), 6)

    def test_search(self):
        self.assertTrue(self.mylist.search(93))

    def test_search_item(self):
        self.assertFalse(self.mylist.search(100))

    def test_add(self):
        self.mylist.add(100)
        self.assertTrue(self.mylist.search(100))

    def test_remove(self):
        self.mylist.remove(54)
        self.assertFalse(self.mylist.search(54))


if __name__ == "__main__":
    unittest.main()

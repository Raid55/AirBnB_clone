#!/usr/bin/python3
import unittest
from models.state import State
"""test for amenity"""


class test_amenity(unittest.TestCase):
    """tests for amenity"""

    def setUp(self):
        """comment"""
        self.a = State()

    def tearDown(self):
        """comment"""
        del self.a

    def test_tests(self):
        """some tests for amenity"""
        # print('Hello')
        self.assertIsInstance(self.a, State)
        self.assertIsInstance(self.a.name, str)

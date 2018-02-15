#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""test for amenity"""


class test_amenity(unittest.TestCase):
    """tests for amenity"""

    def setUp(self):
        """comment"""
        self.a = Amenity()

    def tearDown(self):
        """comment"""
        del self.a

    def test_tests(self):
        """some tests for amenity"""
        # print('Hello')
        self.assertIsInstance(self.a, Amenity)
        self.assertIsInstance(self.a.name, str)

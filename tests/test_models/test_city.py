#!/usr/bin/python3
import unittest
from models.city import City
"""test for amenity"""


class test_city(unittest.TestCase):
    """tests for amenity"""

    def setUp(self):
        """comment"""
        self.a = City()

    def tearDown(self):
        """comment"""
        del self.a

    def test_tests(self):
        """some tests for amenity"""
        # print('Hello')
        self.assertIsInstance(self.a, City)
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.state_id, str)

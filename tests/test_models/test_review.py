#!/usr/bin/python3
import unittest
from models.review import Review
"""test for amenity"""


class test_amenity(unittest.TestCase):
    """tests for amenity"""

    def setUp(self):
        """comment"""
        self.a = Review()

    def tearDown(self):
        """comment"""
        del self.a

    def test_tests(self):
        """some tests for amenity"""
        # print('Hello')
        self.assertIsInstance(self.a, Review)
        self.assertIsInstance(self.a.place_id, str)
        self.assertIsInstance(self.a.user_id, str)
        self.assertIsInstance(self.a.text, str)

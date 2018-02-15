#!/usr/bin/python3
import unittest
from models.user import User
"""test for amenity"""


class test_user(unittest.TestCase):
    """tests for amenity"""

    def setUp(self):
        """comment"""
        self.a = User()

    def tearDown(self):
        """comment"""
        del self.a

    def test_tests(self):
        """some tests for amenity"""
        # print('Hello')
        self.assertIsInstance(self.a, User)
        self.assertIsInstance(self.a.email, str)
        self.assertIsInstance(self.a.password, str)
        self.assertIsInstance(self.a.first_name, str)
        self.assertIsInstance(self.a.last_name, str)

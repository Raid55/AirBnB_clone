#!/usr/bin/python3
import unittest
from models.place import Place
"""test for amenity"""


class test_place(unittest.TestCase):
    """tests for amenity"""

    def setUp(self):
        """comment"""
        self.a = Place()

    def tearDown(self):
        """comment"""
        del self.a

    def test_tests(self):
        """some tests for amenity"""
        # print('Hello')
        self.assertIsInstance(self.a, Place)
        self.assertIsInstance(self.a.city_id, str)
        self.assertIsInstance(self.a.user_id, str)
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.description, str)
        self.assertIsInstance(self.a.number_rooms, int)
        self.assertIsInstance(self.a.number_bathrooms, int)
        self.assertIsInstance(self.a.max_guest, int)
        self.assertIsInstance(self.a.price_by_night, int)
        self.assertIsInstance(self.a.latitude, float)
        self.assertIsInstance(self.a.longitude, float)
        self.assertIsInstance(self.a.amenity_ids, list)

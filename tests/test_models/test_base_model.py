#!/usr/bin/python3
"""testing the base"""
import unittest
from models.base_model import BaseModel
import re
import datetime


class test_BaseModel(unittest.TestCase):
    """tests for BaseModel class #3"""

    def setUp(self):
        self.a = BaseModel()
        self.b = BaseModel()

    def tearDown(self):
        del self.a
        del self.b

    def test_existance(self):
        """test for existance of variables"""
        # print("\nIn existance")
        m = ""
        for k in self.a.__dict__:
            m = m + " " + k
        i = re.search('id', m)
        k = re.search('created_at', m)
        j = re.search('updated_at', m)
        self.assertIsNotNone(i)
        self.assertIsNotNone(k)
        self.assertIsNotNone(j)

    def test_format(self):
        """test str format"""
        # print("\nIn format")
        """check format of str output"""
        self.assertRegex(self.a.__str__(), '\[.*\]\s+\(.*\)\s+\{.*\}')

    def test_id(self):
        """test id format"""
        # print("\nIn id")
        """check uuid format"""
        self.assertRegex(self.a.id, '\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
        """check id randomness, compare ids"""
        self.assertFalse(self.a.id == self.b.id)

    def test_instance(self):
        """test instance variables"""
        # print("\nIn instance")
        """check each if each variable isinstance str"""
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

    def test_time(self):
        """test time"""
        # print("\nIn time")
        """check ISO8601 format"""
        pattern = r'\d{4}-\d{2}-\d{2}[T]\d{2}:\d{2}.\d{2}.\d{6}'
        self.assertRegex(self.a.created_at.isoformat(), pattern)
        self.assertRegex(self.a.updated_at.isoformat(), pattern)
        """False: created >= update"""
        self.assertTrue(self.a.created_at <= self.a.updated_at)
        temp = self.a.updated_at
        self.a.save()
        self.assertNotEqual(self.a.updated_at, temp)

    def test_dict(self):
        """test to_dict"""
        # print('\nin dict')
        self.assertIsInstance(self.a, BaseModel)
        self.assertIsInstance(self.a.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()

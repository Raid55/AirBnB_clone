#!/usr/bin/env python3
"""testing the base"""
import unittest
from models.base_model import BaseModel
import re
import datetime


a = BaseModel()
b = BaseModel()


class test_BaseModel(unittest.TestCase):
    """tests for BaseModel class #3"""

    def test_existance(self):
        """test for existance of variables"""
        print("\nIn existance")
        m = ""
        for k in a.__dict__:
            m = m + " " + k
        i = re.search('id', m)
        k = re.search('created_at', m)
        j = re.search('updated_at', m)
        self.assertIsNotNone(i)
        self.assertIsNotNone(k)
        self.assertIsNotNone(j)

    def test_format(self):
        """test str format"""
        print("\nIn format")
        """check format of str output"""
        self.assertRegex(a.__str__(), '\[.*\]\s+\(.*\)\s+\{.*\}')

    def test_id(self):
        """test id format"""
        print("\nIn id")
        """check uuid format"""
        self.assertRegex(a.id, '\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
        """check id randomness, compare ids"""
        self.assertFalse(a.id == b.id)

    def test_instance(self):
        """test instance variables"""
        print("\nIn instance")
        """check each if each variable isinstance str"""
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)

    def test_time(self):
        """test time"""
        print("\nIn time")
        """check ISO8601 format"""
        pattern = r'\d{4}-\d{2}-\d{2}[T]\d{2}:\d{2}.\d{2}.\d{6}'
        self.assertRegex(a.created_at, pattern)
        self.assertRegex(a.updated_at, pattern)
        """False: created >= update"""
        self.assertFalse(a.created_at >= a.updated_at)
        """save updated value, call save, compare new update to previous"""
        placeholder = a.updated_at
        c = a.save()
        self.assertTrue(a.updated_at > placeholder)


if __name__ == '__main__':
    unittest.main()

import datetime
import os
import subprocess
import time
import unittest

class randomTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.year = 2022
        cls.month = 10
        cls.day = 31

    @classmethod
    def tearDownClass(cls):
        pass

    def test_year(self):
        self.assertEqual(self.year, 2022)

    def test_month(self):
        self.assertEqual(self.month, 10)

    def test_day(self):
        self.assertEqual(self.day, 31)

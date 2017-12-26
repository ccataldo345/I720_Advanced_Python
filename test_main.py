import unittest
from datetime import datetime, timedelta

from project import get_last_value_date

today = datetime.now()
yesterday = (today - timedelta(1)).strftime('%Y-%m-%d')

class LastValueDateTestCase(unittest.TestCase):
    def test_value(self):
        result = get_last_value_date()
        self.assertEqual(yesterday, result)

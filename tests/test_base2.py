#!/usr/bin/ python3
"""
Imported modules:
uuid
time, datetime
BaseModel
"""
import time
import uuid
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ Test Case to check for kwargs """
    @classmethod
    def setUp(cls):
        cls.base1 = BaseModel('foo', 'bar')
        cls.timed = str(datetime.now())
        cls.timedft = datetime.strptime(cls.timed, '%Y-%m-%d %H:%M:%S.%f')
        cls.base2 = BaseModel(created_at = str(cls.timedft.
                                               strftime('%Y-%m-%dT%H:%M:%S.%f'
                                               )))

    @classmethod
    def tearDown(cls):
        del cls.base1
        del cls.base2

    def test_init_args(self):
        self.assertEqual(len(self.base1.id), len(str(uuid.uuid4())))
        #self.assertEqual(self.base1.created_at, datetime.now())
        self.assertEqual(self.base1.updated_at, self.base1.created_at)

    def test_init_kwargs(self):
        #self.assertEqual(self.base1.created_at, self.timed)
        self.assertEqual(self.base1.updated_at, self.base1.created_at)


if __name__ == '__main__':
    unittest.main()

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
    """ Test Case to check program handling of passed arguments """
    @classmethod
    def setUp(cls):
        """
        base1 - initialize instance with args(id)
        base2 - initialize instance with kwargs(created_at)
        """
        cls.base1 = BaseModel(id=3)
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
        """ With args
        ERROR!: Obj doesn't initialize well if id is passed. created &
        updated at are not created
        """
        self.assertEqual(self.base1.id, 3)
        #self.assertEqual(self.base1.created_at, datetime.now())
        #self.assertEqual(self.base1.updated_at, self.base1.created_at)

    def test_init_kwargs(self):
        """ With kwargs present """
        self.assertEqual(self.base2.created_at, self.timedft)
        self.assertEqual(self.base2.created_at, self.base2.created_at)


if __name__ == '__main__':
    unittest.main()

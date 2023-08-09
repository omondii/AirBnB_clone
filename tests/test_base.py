#!/usr/bin/python3
"""
unittest module and models,base module  are imported
models.base allo access and test the functionality of a base class
"""
import time
import uuid
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """defines a test case class"""

    @classmethod
    def setUp(self):
       """initialize object"""
       self.base1 = BaseModel()
       self.name = "My First Model"
       self.my_number = 89

    @classmethod
    def tearDown(self):
        """delete created instances from memory"""
        del self.base1

    def test_str_name(self):
        """return error is name is a int"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel(89, 89)

    def test_float_name(self):
        """return error if name is a float"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel(89.9, 89)

    def test_bol_name(self):
        """return error is name is a boolean"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel(False, 89)

    def test_complex_name(self):
        """check name is a string"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel(1j, 89)

    def test_my_number(self):
        """check my_number is a string"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel("My First Model", "89")

    def test_my_number(self):
        """check is my_number is a float"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel("My First Model", 89.9)

    def test_my_number(self):
        """check if mu_number is a boolean"""
        with self.assertRaises(TypeError) as error:
            b = BaseModel("My First Model", False)

    def test_uuid(self):
        """check for unique id using uuid.uuid4()"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id), len(str(uuid.uuid4())))

    def test_created_at(self):
        """check the created time is correct"""
        self.assertIsInstance(self.base1.created_at, datetime)

    def test_updated_at(self):
        """check if updated time is correct"""
        self.assertIsInstance(self.base1.updated_at, datetime)

    def test_str(self):
        """check object representation"""
        expected_str = ("[BaseModel] ({}) {}".format(self.base1.id,
                                                     self.base1.__dict__))
        self.assertEqual(str(self.base1), expected_str)

    def test_save(self):
        """check the updated time is correct"""
        first_value = self.base1.updated_at
        time.sleep(2)
        self.base1.save()
        second_value = self.base1.updated_at
        self.assertGreater(second_value, first_value)

    def test_dict(self):
        """check if the method return a dictionary"""
        expected_str = ({"my_number": self.base1.my_number,
                 "name": self.base1.name,
                 "__class__": "BaseModel",
                 "updated_at": self.base1.updated_at.isoformat(),
                 "id": self.base1.id,
                 "created_at": self.base1.created_at.isoformat()})
        self.assertEqual((self.base1.to_dict()), expected_str)
if __name__ == '__main__':
    unittest.main()

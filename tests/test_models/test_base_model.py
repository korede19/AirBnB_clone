#!/usr/bin/python3
""" This is a test module for BaseModel Class"""


from models.base_model import BaseModel
from models import base_model
import pep8
import datetime
import unittest
import os


class TestBaseModel(unittest.TestCase):
    """Class for test the BaseModel class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(BaseModel.__doc__) > 0)
        for fn in dir(BaseModel):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(BaseModel):
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )

    def test_pep8(self):
        """ Test for pep8 stylecode """
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        file_base = 'models/base_model.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def setUp(self):
        """setUp Method"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """tearDown Method"""
        pass

    def test_init(self):
        """ Method to test the initialization of instances """
        self.assertIs(type(self.base1.id), str)
        self.assertIs(type(self.base1.created_at), datetime.datetime)
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertEqual(self.base1.created_at, self.base1.updated_at)
        self.assertEqual(self.base2.created_at, self.base2.updated_at)
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)
        dict_test = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                     'created_at': '2017-09-28T21:03:54.052298',
                     '__class__': 'BaseModel', 'my_number': 89,
                     'updated_at': '2017-09-28T21:03:54.052302',
                     'name': 'Holberton'}
        base3 = BaseModel(**dict_test)
        self.assertEqual(base3.id, dict_test.get("id"))
        self.assertIs(type(base3.created_at), datetime.datetime)

    def test_str(self):
        """ Method to test __str__ method """
        output = "[BaseModel] ({}) {}".\
            format(self.base1.id, self.base1.__dict__)
        self.assertEqual(str(self.base1), output)
        self.base1.name = "Holberton"
        self.base1.my_number = 89
        output = "[BaseModel] ({}) {}".\
            format(self.base1.id, self.base1.__dict__)
        self.assertEqual(str(self.base1), output)

    def test_to_dict(self):
        """ Method to test to_dict method """
        keys = ['id', 'created_at', 'updated_at', '__class__']
        dict_b1 = self.base1.to_dict()
        self.assertCountEqual(keys, dict_b1)
        self.base1.name = "Holberton"
        self.base1.my_number = 89
        new_d = self.base1.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        keys = ['id',
                'created_at',
                'updated_at',
                '__class__',
                'name',
                'my_number']
        dict_b1 = self.base1.to_dict()
        self.assertCountEqual(keys, dict_b1)

    def test_save(self):
        """ Method to test to   save method """
        date_old = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(date_old, self.base1.updated_at)
        date_old = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(date_old, self.base1.updated_at)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exe)

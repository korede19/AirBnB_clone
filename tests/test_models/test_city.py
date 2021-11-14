#!/usr/bin/python3
""" This is a test module for City Class"""


from models.city import City
from models import city
import pep8
import unittest
import os


class TestCity(unittest.TestCase):
    """Class for test the City class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(city.__doc__) > 0)
        self.assertTrue(len(City.__doc__) > 0)
        for fn in dir(City):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(City):
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
        file_base = 'models/city.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_city is an instance of BaseModel'''
        my_city = City()
        self.assertIsInstance(my_city, City)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/city.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/city.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/city.py', os.X_OK)
        self.assertTrue(exe)

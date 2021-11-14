#!/usr/bin/python3
""" This is a test module for Amenity Class"""


from models.amenity import Amenity
from models import amenity
import pep8
import unittest
import os


class TestAmenity(unittest.TestCase):
    """Class for test the Amenity class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(amenity.__doc__) > 0)
        self.assertTrue(len(Amenity.__doc__) > 0)
        for fn in dir(Amenity):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(Amenity):
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
        file_base = 'models/amenity.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_model is an instance of BaseModel'''
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(exe)

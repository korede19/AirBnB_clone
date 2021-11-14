#!/usr/bin/python3
""" This is a test module for User Class"""


from models.user import User
from models import user
import pep8
import unittest
import os


class TestUser(unittest.TestCase):
    """Class for test the User class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(user.__doc__) > 0)
        self.assertTrue(len(User.__doc__) > 0)
        for fn in dir(User):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(User):
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
        file_base = 'models/user.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_user is an instance of BaseModel'''
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/user.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/user.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/user.py', os.X_OK)
        self.assertTrue(exe)

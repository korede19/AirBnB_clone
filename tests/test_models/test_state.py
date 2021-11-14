#!/usr/bin/python3
""" This is a test module for State Class"""


from models.state import State
from models import state
import pep8
import unittest
import os


class TestState(unittest.TestCase):
    """Class for test the State class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(state.__doc__) > 0)
        self.assertTrue(len(State.__doc__) > 0)
        for fn in dir(State):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(State):
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
        file_base = 'models/state.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_state is an instance of BaseModel'''
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/state.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/state.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/state.py', os.X_OK)
        self.assertTrue(exe)

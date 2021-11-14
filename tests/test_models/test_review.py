#!/usr/bin/python3
""" This is a test module for Review Class"""


from models.review import Review
from models import review
import pep8
import unittest
import os


class TestReview(unittest.TestCase):
    """Class for test the Review class"""

    def test_docstring(self):
        """ Method to test doctring module, class and func """
        self.assertTrue(len(review.__doc__) > 0)
        self.assertTrue(len(Review.__doc__) > 0)
        for fn in dir(Review):
            self.assertTrue(len(fn.__doc__) > 0)

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in dir(Review):
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
        file_base = 'models/review.py'
        check = style.check_files([file_base])
        self.assertEqual(check.total_errors, 0, msg)

    def test_is_an_instance(self):
        '''check if my_review is an instance of BaseModel'''
        my_review = Review()
        self.assertIsInstance(my_review, Review)

    def test_permissions(self):
        """ Test for check the permissions """
        read = os.access('models/review.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/review.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/review.py', os.X_OK)
        self.assertTrue(exe)

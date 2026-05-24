#!/usr/bin/python3
"""Unit tests for User."""
import os
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Tests for User class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_inherits_from_base_model(self):
        self.assertIsInstance(User(), BaseModel)

    def test_email_is_class_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_class_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_class_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_class_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_email_default_empty(self):
        self.assertEqual("", User.email)

    def test_password_default_empty(self):
        self.assertEqual("", User.password)

    def test_first_name_default_empty(self):
        self.assertEqual("", User.first_name)

    def test_last_name_default_empty(self):
        self.assertEqual("", User.last_name)

    def test_to_dict_class_name(self):
        u = User()
        self.assertEqual(u.to_dict()["__class__"], "User")

    def test_str_contains_class_name(self):
        u = User()
        self.assertIn("[User]", str(u))


if __name__ == "__main__":
    unittest.main()

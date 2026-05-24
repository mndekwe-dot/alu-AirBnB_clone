#!/usr/bin/python3
"""Unit tests for State."""
import os
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Tests for State class."""

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
        self.assertIsInstance(State(), BaseModel)

    def test_name_is_class_str(self):
        self.assertEqual(str, type(State.name))

    def test_name_default_empty(self):
        self.assertEqual("", State.name)

    def test_to_dict_class_name(self):
        s = State()
        self.assertEqual(s.to_dict()["__class__"], "State")

    def test_str_contains_class_name(self):
        s = State()
        self.assertIn("[State]", str(s))


if __name__ == "__main__":
    unittest.main()

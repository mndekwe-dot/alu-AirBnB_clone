#!/usr/bin/python3
"""Unit tests for City."""
import os
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Tests for City class."""

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
        self.assertIsInstance(City(), BaseModel)

    def test_state_id_is_class_str(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_is_class_str(self):
        self.assertEqual(str, type(City.name))

    def test_state_id_default_empty(self):
        self.assertEqual("", City.state_id)

    def test_name_default_empty(self):
        self.assertEqual("", City.name)

    def test_to_dict_class_name(self):
        c = City()
        self.assertEqual(c.to_dict()["__class__"], "City")

    def test_str_contains_class_name(self):
        c = City()
        self.assertIn("[City]", str(c))


if __name__ == "__main__":
    unittest.main()

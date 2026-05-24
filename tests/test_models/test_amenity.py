#!/usr/bin/python3
"""Unit tests for Amenity."""
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Tests for Amenity class."""

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
        self.assertIsInstance(Amenity(), BaseModel)

    def test_name_is_class_str(self):
        self.assertEqual(str, type(Amenity.name))

    def test_name_default_empty(self):
        self.assertEqual("", Amenity.name)

    def test_to_dict_class_name(self):
        a = Amenity()
        self.assertEqual(a.to_dict()["__class__"], "Amenity")

    def test_str_contains_class_name(self):
        a = Amenity()
        self.assertIn("[Amenity]", str(a))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit tests for Place."""
import os
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Tests for Place class."""

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
        self.assertIsInstance(Place(), BaseModel)

    def test_city_id_is_class_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_class_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_class_str(self):
        self.assertEqual(str, type(Place.name))

    def test_description_is_class_str(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_class_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_class_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_class_int(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_class_int(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_class_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_class_float(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_class_list(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_to_dict_class_name(self):
        p = Place()
        self.assertEqual(p.to_dict()["__class__"], "Place")

    def test_str_contains_class_name(self):
        p = Place()
        self.assertIn("[Place]", str(p))


if __name__ == "__main__":
    unittest.main()

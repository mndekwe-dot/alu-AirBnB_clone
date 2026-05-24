#!/usr/bin/python3
"""Unit tests for Review."""
import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Tests for Review class."""

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
        self.assertIsInstance(Review(), BaseModel)

    def test_place_id_is_class_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_class_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_class_str(self):
        self.assertEqual(str, type(Review.text))

    def test_place_id_default_empty(self):
        self.assertEqual("", Review.place_id)

    def test_user_id_default_empty(self):
        self.assertEqual("", Review.user_id)

    def test_text_default_empty(self):
        self.assertEqual("", Review.text)

    def test_to_dict_class_name(self):
        r = Review()
        self.assertEqual(r.to_dict()["__class__"], "Review")

    def test_str_contains_class_name(self):
        r = Review()
        self.assertIn("[Review]", str(r))


if __name__ == "__main__":
    unittest.main()

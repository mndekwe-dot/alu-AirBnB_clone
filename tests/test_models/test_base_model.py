#!/usr/bin/python3
"""Unit tests for BaseModel."""
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Tests for BaseModel instantiation."""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_str_representation(self):
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIn("[BaseModel]", bm_str)
        self.assertIn(bm.id, bm_str)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_class_key_not_stored(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(
            id="345", created_at=dt_iso,
            updated_at=dt_iso, __class__="BaseModel"
        )
        self.assertNotIn("__class__", bm.__dict__)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)

    def test_no_args_sets_id(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))

    def test_no_args_sets_created_at(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "created_at"))

    def test_no_args_sets_updated_at(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "updated_at"))


class TestBaseModel_save(unittest.TestCase):
    """Tests for BaseModel save method."""

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

    def test_one_save_updates_updated_at(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated = bm.updated_at
        bm.save()
        self.assertLess(first_updated, bm.updated_at)

    def test_two_saves_update_correctly(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated = bm.updated_at
        bm.save()
        second_updated = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(first_updated, second_updated)
        self.assertLess(second_updated, bm.updated_at)

    def test_save_creates_file(self):
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_id_in_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_save_with_arg_raises(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Tests for BaseModel to_dict method."""

    def test_to_dict_returns_dict(self):
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Test"
        bm.my_number = 42
        d = bm.to_dict()
        self.assertIn("name", d)
        self.assertIn("my_number", d)

    def test_to_dict_created_at_is_str(self):
        bm = BaseModel()
        self.assertEqual(str, type(bm.to_dict()["created_at"]))

    def test_to_dict_updated_at_is_str(self):
        bm = BaseModel()
        self.assertEqual(str, type(bm.to_dict()["updated_at"]))

    def test_to_dict_datetime_format(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d["created_at"], bm.created_at.isoformat())
        self.assertEqual(d["updated_at"], bm.updated_at.isoformat())

    def test_to_dict_class_name(self):
        bm = BaseModel()
        self.assertEqual(bm.to_dict()["__class__"], "BaseModel")

    def test_to_dict_not_same_as_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg_raises(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_roundtrip_via_dict(self):
        bm1 = BaseModel()
        bm_dict = bm1.to_dict()
        bm2 = BaseModel(**bm_dict)
        self.assertEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.created_at, bm2.created_at)
        self.assertEqual(bm1.updated_at, bm2.updated_at)
        self.assertIsNot(bm1, bm2)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit tests for FileStorage."""
import os
import json
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Tests for FileStorage instantiation."""

    def test_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_arg_raises(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_is_FileStorage(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Tests for FileStorage public methods."""

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
        FileStorage._FileStorage__objects = {}

    def test_all_returns_dict(self):
        self.assertIsInstance(storage.all(), dict)

    def test_all_with_arg_raises(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_adds_object(self):
        bm = BaseModel()
        storage.new(bm)
        self.assertIn("BaseModel." + bm.id, storage.all())

    def test_new_with_none_raises(self):
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save_creates_file(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_writes_valid_json(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)

    def test_save_contains_object(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn("BaseModel." + bm.id, data)

    def test_reload_from_file(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = "BaseModel." + bm.id
        self.assertIn(key, storage.all())

    def test_reload_no_file_no_exception(self):
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload() raised an exception: {}".format(e))

    def test_reload_with_arg_raises(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_all_classes_stored(self):
        bm = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        for obj in [bm, u, s, c, a, p, r]:
            storage.new(obj)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel." + bm.id, all_objs)
        self.assertIn("User." + u.id, all_objs)
        self.assertIn("State." + s.id, all_objs)
        self.assertIn("City." + c.id, all_objs)
        self.assertIn("Amenity." + a.id, all_objs)
        self.assertIn("Place." + p.id, all_objs)
        self.assertIn("Review." + r.id, all_objs)

    def test_reload_creates_correct_type(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = "BaseModel." + bm.id
        self.assertIsInstance(storage.all()[key], BaseModel)


if __name__ == "__main__":
    unittest.main()

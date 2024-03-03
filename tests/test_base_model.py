#!/usr/bin/python3
"""
Test differents behaviors
of the Base class
"""


import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A class to test the Base Class
    """


    def setUp(self):
        """
        Setup method to create an instance of BaseModel before each test.
        """
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """
        Test whether the id attribute of BaseModel is a string.
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test whether the created_at attribute of BaseModel is a datetime object.
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test whether the updated_at attribute of BaseModel is a datetime object.
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test whether calling the save method updates the updated_at attribute.
        """
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_contains_class_name(self):
        """
        Test whether the dictionary returned by to_dict contains the __class__ key with the class name.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at_and_updated_at(self):
        """
        Test whether the dictionary returned by to_dict contains the created_at and updated_at keys.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_created_at_updated_at_format(self):
        """
        Test whether the datetime strings in the dictionary returned by to_dict match the ISO format.
        """
        obj_dict = self.base_model.to_dict()
        created_at_str = obj_dict['created_at']
        updated_at_str = obj_dict['updated_at']
        self.assertEqual(datetime.fromisoformat(created_at_str), self.base_model.created_at)
        self.assertEqual(datetime.fromisoformat(updated_at_str), self.base_model.updated_at)

    def test_init_with_dict_representation(self):
        """
        Creates a dictionary representation of a BaseModel instance with custom attributes.
        It then recreates a BaseModel instance from this dictionary representation and checks
        if the attributes are correctly set.
        """
        base_model_dict = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': '2024-03-02T12:00:00.000000',
            'updated_at': '2024-03-02T12:00:00.000000',
            'custom_attribute': 'test_value'
        }
        recreated_model = BaseModel(**base_model_dict)
        self.assertEqual(recreated_model.id, 'test_id')
        self.assertEqual(recreated_model.custom_attribute, 'test_value')
        self.assertIsInstance(recreated_model.created_at, datetime)
        self.assertIsInstance(recreated_model.updated_at, datetime)
        self.assertEqual(recreated_model.created_at, datetime(2024, 3, 2, 12, 0))
        self.assertEqual(recreated_model.updated_at, datetime(2024, 3, 2, 12, 0))

    def test_init_with_empty_dict(self):
        """
        creates an empty dictionary representation and recreates a BaseModel instance from it.
        It then checks if the default attributes (id, created_at, updated_at) are correctly set.
        """
        empty_dict = {}

        # Recreate a BaseModel instance from the empty dictionary representation
        recreated_model = BaseModel(**empty_dict)

        # Check if the attributes are correctly set
        self.assertIsInstance(recreated_model.id, str)
        self.assertIsInstance(recreated_model.created_at, datetime)
        self.assertIsInstance(recreated_model.updated_at, datetime)
        self.assertEqual(recreated_model.created_at, recreated_model.updated_at)

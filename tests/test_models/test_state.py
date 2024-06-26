#!/usr/bin/python3
"""
Unit Test for State Class
"""
import unittest
from datetime import datetime
import models
import json
import os
from models.state import State

State = models.state.State
BaseModel = models.base_model.BaseModel
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class TestStateDocs(unittest.TestCase):
    """Class for testing State docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   State Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nState Class from Models Module\n'
        actual = models.state.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'State class handles all application states'
        actual = State.__doc__
        self.assertEqual(expected, actual)


class TestStateInstances(unittest.TestCase):
    """Testing for State class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  State Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """Initialize a new state for testing"""
        self.state = State()

    def test_instantiation(self):
        """Check if State is properly instantiated"""
        self.assertIsInstance(self.state, State)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_instantiation_no_updated(self):
        """Check if State instantiation does not have updated attribute"""
        my_str = str(self.state)
        actual = 0
        if 'updated_at' not in my_str:
            actual += 1
        self.assertEqual(1, actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_updated_at(self):
        """Check if save function adds updated_at attribute"""
        initial_time = self.state.updated_at
        self.state.save()
        updated_time = self.state.updated_at
        self.assertNotEqual(initial_time, updated_time)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_to_json(self):
        """Check if to_json returns a serializable dict object"""
        self.state_json = self.state.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.state_json)
        except Exception:
            actual 0
        self.assertEqual(1, actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_json_class(self):
        """Check if to_json includes class key with value State"""
        self.state_json = self.state.to_json()
        actual = None
        if self.state_json['__class__']:
            actual = self.state_json['__class__']
        expected = 'State'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """Add name attribute"""
        self.state.name = "betty"
        if hasattr(self.state, 'name'):
            actual = self.state.name
        else:
            actual = ''
        expected = "betty"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

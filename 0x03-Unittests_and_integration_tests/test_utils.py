#!/usr/bin/env python3
""" Parametrerize a unit test
"""

from unittest.mock import patch, Mock
from parameterized import parameterized
import unittest
from utils import (access_nested_map, memoize, get_json)


class TestAccessNestMap(unittest.TestCase):
    """ Inherits from the parent class
    """
    @parameterized.expand([
        ({"a"}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, seted_map, path, expected_result):
        """ Method to test that the method returns as it supposed
        """
        self.assertEqual(access_nested_map(map, path, expected_result))

    @parameterized.expand([
        ({}, ("a"), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_result):
        """ Method test raises exceptions
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_result, e.exception)

#!/usr/bin/env python3
""" Write the first unit test for utils.access_nested_map
"""

from parameterized import parameterized
from unittest.mock import Mock, patch
import unittest
from unittest import mock
from utils import access_nested_map, memoize, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Method to test that the method return what it is supposed
        """
        self.assertEqual(access_nested_map(map, path), expected_output)

#!/usr/bin/env python3
""" Parameterize a unit test
"""

from parameterized import parameterized
from unittest.mock import Mock, patch, mock
import unittest
from utils import access_nested_map, memoize, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Return output test
        """
        self.assertEqual(access_nested_map(map, path), expected_output)

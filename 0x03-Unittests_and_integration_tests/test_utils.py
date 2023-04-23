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

    @parameterized.expand([
        ({}, ("a"), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, unexpected_output):
        """ Return the unexpected or wrong output
        """
        with self.assertRaises(KeyError) as error:
            self.assertEqual(access_nested_map(map, path)
                             (unexpected_output, error.exception))


class TestGetJson(unittest.TestCase):
    """ Mock HTTP calls to test utils.get_json return expected result
    """
    @parameterized.expand([
        ("http://example.com", {"playload": True}),
        ("https://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Method to test that returns the expected output
        """
        Mock_res = Mock()
        Mock_res.json.return_value = test_payload
        with patch('requests.get', return_value=Mock_res):
            expected_response = get_json(test_url)
            self.assertEqual(expected_response, test_payload)
            Mock_res.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Parameterize and patch
    """
    def test_memoize(self):
        """ Method tests memoize function
        """

        class TestClass:
            """ Tests with memoize
            """

            def a_method(self):
                """ Method Returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Method returns memoized property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test_class = TestClass()
            expected_return = test_class.a_property
            expected_return = test_class.a_property

            self.assertEqual(expected_return, 42)
            mock.assert_called_once()

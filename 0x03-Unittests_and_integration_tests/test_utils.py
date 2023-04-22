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
        output = access_nested_map(map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test Raises exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """ Mock Http calls
    """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test the output is equal test_payload
        """
        # set mock response to have return value of test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that mocked method called once per input
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Method for testing memoization
    """

    def test_memoize(self):
        """ Method Tests memoize function
        """

        class TestClass:
            """ Test class of a function
            """

            def a_method(self):
                """ Method return 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()

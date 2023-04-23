#!/usr/bin/env python3
""" Parameterize and patch as decorators
"""

import json
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, propertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Implement the test_org method
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, output, patch):
        """ Returns the correct value
        """
        test_class = GithubOrgClient(output)
        test_class.org()
        patch.assert_called_once_with(f'https://api.github.com/orgs/{output}')

#!/usr/bin/env python3
""" Parameterize and patch as decorators
"""

import json
import unittest
from fixtures import TEST_PAYLOAD
import utils
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, call, propertyMock, Mock
import client
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Implement the test_org method
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, output, patch):
        """ Returns the correct value
        """
        test_class = GithubOrgClient(output)
        test_class.org()
        patch.assert_called_once_with(f'https://api.github.com/orgs/{input}')

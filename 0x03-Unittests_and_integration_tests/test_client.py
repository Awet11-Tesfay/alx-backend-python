#!/usr/bin/env python3
""" Parameterize and patch as decorators
"""

from fixtures import TEST_PAYLOAD
import requests
import client
from unittest import TestCase
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock, call
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized_class, parameterized
import utils


class TestGithubOrgClient(TestCase):
    """ Implement the test_org
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, mock, patch):
        """ With the expected argument and not exectued
        """
        patch.return_value = mock
        a = GithubOrgClient(org)
        self.assertEqual(a.org, mock)
        patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """ Turns methods into properties
        """
        output = "www.yes.com"
        payload = {"repos_url": output}
        mock = 'client.GithubOrgClient.org'
        with patch(mock, PropertyMock(return_value=payload)):
            client = GithubOrgClient("a")
            self.assertEqual(client._public_repos_url, output)

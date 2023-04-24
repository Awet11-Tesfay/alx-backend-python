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

    @patch('client.get_json')
    def test_public_repos(self, get_json):
        """ Return value of your choice
        """
        haile = {"name": "Haile", "license": {"key": "a"}}
        awet = {"name": "Awet", "license": {"key": "b"}}
        hari = {"name": "Hari"}
        mock = 'client.GithubOrgClient._public_repos_url'
        get_json.return_value = [haile, awet, hari]
        with patch(mock, PropertyMock(return_value="www.yes.com")) as x:
            a = GithubOrgClient("a")
            self.assertEqual(a.public_repos(), ['Haile', 'Awet', 'Hari'])
            self.assertEqual(a.public_repos("a"), ['Haile'])
            self.assertEqual(a.public_repos("c"), [])
            self.assertEqual(a.public_repos(45), [])
            get_json.assert_called_once_with("www.yes.com")
            x.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, input, license, output):
        """ Parameterize the test with the ff inputs
        """
        self.assertEqual(GithubOrgClient.has_license(input, license), output)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'appache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """ Implement setUpclass and tearDownClass
    """

    @classmethod
    def setUpClass(self):
        """ Should mock requests.get to return payloads
        """
        input = TEST_PAYLOAD[0][0]
        output = TEST_PAYLOAD[0][1]
        mock = Mock()
        mock.json = Mock(return_value=input)
        self.mock = mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=output)
        self.repos_mock = repos_mock

        self.patcher = patch('requests.get')
        self.get = self.patcher.start()

        rep = {self.org_payload["repos_url"]: repos_mock}
        self.get.side_effect = lambda y: rep.get(y, mock)

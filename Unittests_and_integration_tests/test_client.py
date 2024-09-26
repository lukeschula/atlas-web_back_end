#!/usr/bin/env python3
""" declare the TestGithubOrgClient class and implement test_org method """
import unittest
from unittest import mock
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from parameterized import parameterized_class
from urllib.error import HTTPError
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ child class of unittest.TestCase class methods """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """ test GithubOrgClient.org and returns the correct value """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get_json.return_value)
        mock_get_json.assert_called_once

    def test_public_repos_url(self):
        """ method to unit-test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "atlas"}) as mock_org:
            test_json = {"repos_url": "atlas"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            self.assertEqual(test_return,
                             mock_org.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "atlas"}])
    def test_public_repos(self, mock_get_json):
        """ unit-test GithubOrgClient.public_repos method """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value={"https://api.github.com/"}) as mock_v:
            test_client = GithubOrgClient("atlas")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["atlas"])
            mock_get_json.assert_called_once
            mock_v.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ to unit-test GithudOrgClient.has_license """
        test_client = GithubOrgClient("atlas")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(test_return, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ a child class of unittest.TestCase
    integration test """
    @classmethod
    def setUpClass(cls):
        """ setup patch """
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ tear down patch """
        cls.get_patcher.stop()

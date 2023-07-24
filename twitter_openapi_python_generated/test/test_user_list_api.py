# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import twitter_openapi_python_generated
from twitter_openapi_python_generated.api.user_list_api import UserListApi  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException


class TestUserListApi(unittest.TestCase):
    """UserListApi unit test stubs"""

    def setUp(self):
        self.api = twitter_openapi_python_generated.api.user_list_api.UserListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_followers(self):
        """Test case for get_followers

        """
        pass

    def test_get_followers_you_know(self):
        """Test case for get_followers_you_know

        """
        pass

    def test_get_following(self):
        """Test case for get_following

        """
        pass

    def test_get_tweet_favoriters(self):
        """Test case for get_tweet_favoriters

        """
        pass

    def test_get_tweet_retweeters(self):
        """Test case for get_tweet_retweeters

        """
        pass


if __name__ == '__main__':
    unittest.main()
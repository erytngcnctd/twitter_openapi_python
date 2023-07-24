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
import datetime

import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.tweet_card import TweetCard  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestTweetCard(unittest.TestCase):
    """TweetCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TweetCard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetCard`
        """
        model = twitter_openapi_python_generated.models.tweet_card.TweetCard()  # noqa: E501
        if include_optional :
            return TweetCard(
                legacy = twitter_openapi_python_generated.models.tweet_card_legacy.Tweet_card_legacy(
                    binding_values = [
                        twitter_openapi_python_generated.models.tweet_card_legacy_binding_values_inner.Tweet_card_legacy_binding_values_inner(
                            key = '', 
                            value = twitter_openapi_python_generated.models.tweet_card_legacy_binding_values_inner_value.Tweet_card_legacy_binding_values_inner_value(
                                boolean_value = True, 
                                scribe_key = '', 
                                string_value = '', 
                                type = '', ), )
                        ], 
                    name = '', 
                    url = '', ), 
                rest_id = ''
            )
        else :
            return TweetCard(
        )
        """

    def testTweetCard(self):
        """Test TweetCard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
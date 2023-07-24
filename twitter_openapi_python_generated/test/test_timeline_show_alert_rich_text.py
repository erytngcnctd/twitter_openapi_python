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
from twitter_openapi_python_generated.models.timeline_show_alert_rich_text import TimelineShowAlertRichText  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestTimelineShowAlertRichText(unittest.TestCase):
    """TimelineShowAlertRichText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TimelineShowAlertRichText
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineShowAlertRichText`
        """
        model = twitter_openapi_python_generated.models.timeline_show_alert_rich_text.TimelineShowAlertRichText()  # noqa: E501
        if include_optional :
            return TimelineShowAlertRichText(
                entities = [
                    None
                    ], 
                text = ''
            )
        else :
            return TimelineShowAlertRichText(
        )
        """

    def testTimelineShowAlertRichText(self):
        """Test TimelineShowAlertRichText"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
import unittest

import pytest
from exceptions import SomethingWentWrongWithUrl
from utils import OpenAIAPIUtil, ComplianceContentUtil
from apps import app


class TestComplianceContentUtil(unittest.TestCase):
    def test_fetch_url_text(self):
        url = "https://stripe.com/docs/treasury/marketing-treasury"
        content = ComplianceContentUtil.fetch_url_text(url)
        self.assertIsInstance(content, str)
        self.assertIn("Marketing Treasury-based services", content)

    def test_bad_url(self):
        url = "https://stripe.com/docs/treasury/marketing-treasuryasdf"
        with pytest.raises(SomethingWentWrongWithUrl):
            content = ComplianceContentUtil.fetch_url_text(url)


class TestOpenAPIUtil(unittest.TestCase):
    def test_base_case(self):
        compliance_url = "https://stripe.com/docs/treasury/marketing-treasury"
        pitch_url = "https://www.joinguava.com/"
        compliance = ComplianceContentUtil.fetch_url_text(compliance_url)
        pitch = ComplianceContentUtil.fetch_url_text(pitch_url)
        # util = OpenAIAPIUtil()
        # result = util.analyze_marketing_pitch(compliance, pitch)
        # self.assertIn(result, "duadf")


class TestAPIs(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_invalid_payload(self):
        data = {"web": "test"}
        response = self.app.post("/v1/compliance-issues/", json=data)
        self.assertEqual(response.status_code, 400)

    def test_valid_payload(self):
        data = {"web_page": "https://www.joinguava.com/"}
        response = self.app.post("/v1/compliance-issues/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("content", response.json())
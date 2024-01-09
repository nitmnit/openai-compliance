import unittest

import pytest
from exceptions import SomethingWentWrongWithUrl
from utils import OpenAIAPIUtil, HtmlContentUtil
import config
from apps import app


class TestHtmlContentUtil(unittest.TestCase):
    def test_fetch_url_text(self):
        url = "https://stripe.com/docs/treasury/marketing-treasury"
        content = HtmlContentUtil.fetch_url_text(url)
        self.assertIsInstance(content, str)
        self.assertIn("Marketing Treasury-based services", content)

    def test_bad_url(self):
        url = "https://stripe.com/docs/treasury/marketing-treasuryasdf"
        with pytest.raises(SomethingWentWrongWithUrl):
            content = HtmlContentUtil.fetch_url_text(url)


class TestOpenAPIUtil(unittest.TestCase):
    def test_base_case(self):
        pitch_url = "https://www.joinguava.com/"
        compliance = HtmlContentUtil.fetch_url_text(config.COMPLIANCE_URL)
        pitch = HtmlContentUtil.fetch_url_text(pitch_url)
        util = OpenAIAPIUtil()
        result = util.analyze_marketing_pitch(compliance, pitch)
        self.assertIn("banking", result)


class TestAPIs(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_invalid_payload(self):
        data = {"web": "test"}
        response = self.app.post("/v1/compliance-issues/", json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_url(self):
        data = {"web_page": "test api"}
        response = self.app.post("/v1/compliance-issues/", json=data)
        self.assertEqual(response.status_code, 400)

    def test_valid_payload(self):
        data = {
            "web_page": "https://www.joinguava.com/",
            "guidelines_url": "https://stripe.com/docs/treasury/marketing-treasury",
        }
        response = self.app.post("/v1/compliance-issues/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("content", response.json)

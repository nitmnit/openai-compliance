import os
from openai import OpenAI
from bs4 import BeautifulSoup
import requests
from inscriptis import get_text

from exceptions import SomethingWentWrongWithUrl


class OpenAIAPIUtil:
    INSTRUCTION = """
    You are highly skilled Lawyer specializing in Marketing Compliance Regulations.
    You are given compliance guidelines at the end of these instructions. You will be given marketing idea by user.
    Your job is to find all the sentences in the marketing idea which don't follow the guidelines. When in doubt, point them out.
    Following are the guidelines:
    {guidelines}
    """

    def __init__(self) -> None:
        self.client = OpenAI(max_retries=1)

    def analyze_marketing_pitch(self, guidelines: str, pitch: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": self.INSTRUCTION.format(guidelines=guidelines)
                },
                {
                    "role": "user",
                    "content": pitch
                }
            ]
        )
        return response.choices[0].message.content


class ComplianceContentUtil:
    def fetch_policy_text(url: str) -> str:
        response = requests.get(url)
        if not response.ok:
            raise SomethingWentWrongWithUrl(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article', id="content")
        return get_text(article.prettify())

    def fetch_url_text(url: str) -> str:
        response = requests.get(url)
        if not response.ok:
            raise SomethingWentWrongWithUrl(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        return get_text(soup.prettify())


class ComplianceUtil:
    @staticmethod
    def find_compliance(compliance_url, web_page_url):
        compliance = ComplianceContentUtil.fetch_policy_text(compliance_url)
        pitch = ComplianceContentUtil.fetch_url_text(web_page_url)
        util = OpenAIAPIUtil()
        result = util.analyze_marketing_pitch(compliance, pitch)
        return result

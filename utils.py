import os
from openai import OpenAI
from bs4 import BeautifulSoup
import requests
from inscriptis import get_text

from exceptions import SomethingWentWrongWithUrl


class OpenAIAPIUtil:
    """
    Utility to communicate with OpenAI APIs
    """

    INSTRUCTION = """
    You are highly skilled Lawyer specializing in Marketing Compliance Regulations.
    You are given compliance guidelines at the end of these instructions. You will be given marketing idea by user.
    Your job is to find all the sentences in the marketing idea which don't follow the guidelines. When in doubt, point them out.
    Following are the guidelines:
    {guidelines}
    """

    def __init__(self) -> None:
        self.client = OpenAI(max_retries=1)

    def analyze_marketing_pitch(self, guidelines: str, pitch: str) -> str:
        """
        get feedback from chatgpt on the marketing pitch

        Args:
            guidelines (str): compliance guidelines
            pitch (str): marketing pitch/idea

        Returns:
            str: chatgpt feedback on the pitch w.r.t. the guidelines
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": self.INSTRUCTION.format(guidelines=guidelines),
                },
                {"role": "user", "content": pitch},
            ],
        )
        return response.choices[0].message.content


class HtmlContentUtil:
    """
    Handle transformations for HTML URL to make it readable for AI Assistants
    """

    def fetch_policy_text(url: str) -> str:
        """
        Fetch compliance guidelines from given URL
        Args:
            url (str): guidelines source URL

        Raises:
            SomethingWentWrongWithUrl: invalid URL or URL not reachable

        Returns:
            str: content of the guidelines
        """
        response = requests.get(url)
        if not response.ok:
            raise SomethingWentWrongWithUrl(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find("article", id="content")
        return get_text(article.prettify())

    def fetch_url_text(url: str) -> str:
        response = requests.get(url)
        if not response.ok:
            raise SomethingWentWrongWithUrl(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        return get_text(soup.prettify())


class ComplianceUtil:
    """
    Communicates with OpenAI APIs and passes transformed text to get the compliance feedback.
    """

    @staticmethod
    def find_compliance(compliance_url, web_page_url):
        """
        For given urls, get compliance feedback from OpenAI APIs

        Args:
            compliance_url (str): URL to fetch compliance from
            web_page_url (_type_): URL to test compliance against

        Returns:
            str: ChatGPT feedback on the compliance
        """
        compliance = HtmlContentUtil.fetch_policy_text(compliance_url)
        pitch = HtmlContentUtil.fetch_url_text(web_page_url)
        util = OpenAIAPIUtil()
        result = util.analyze_marketing_pitch(compliance, pitch)
        return result

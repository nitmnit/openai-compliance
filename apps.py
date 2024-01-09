# save this as app.py
from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schema import ComplianceIssuesV2Schema

from utils import ComplianceUtil

app = Flask(__name__)


@app.route("/v1/compliance-issues/", methods=["POST"])
def find_compliance_issues():
    """
    Payload:
    {
        "web_page": "<test url>",
        "guidelines_url": "<guidelines page url>"
    }
    Returns:
    {
        "content": "<ChatGPT Feedback>"
    }
    """
    json_data = request.get_json()
    app.logger.info(f"request: /v2/compliance-issues/, payload: {json_data}")
    try:
        data = ComplianceIssuesV2Schema().load(json_data)
    except ValidationError as err:
        return err.messages, 400
    results = {
        "content": ComplianceUtil.find_compliance(
            data.get("guidelines_url"), data.get("web_page")
        )
    }
    app.logger.info(
        f"response: /v1/compliance-issues/, payload: {data}, response: {results}"
    )
    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)
